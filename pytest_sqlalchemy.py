# -*- coding: utf-8 -*-
import os

from sqlalchemy import create_engine
from sqlalchemy.engine.url import make_url
from sqlalchemy.exc import ProgrammingError
import logging
import pytest

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    group = parser.getgroup('sqlalchemy')
    group.addoption(
        '--test-db-prefix',
        action='store',
        dest='test_db_prefix',
        default='test',
        help='Define a prefix for the test database that is created'
    )

    parser.addini('test_db_prefix', 'Prefix for test database')
    parser.addini('drop_existing_test_db', 'Drop existing test database for each session')
    

@pytest.fixture(scope='session')
def test_db_prefix():
    return 'test_'


@pytest.fixture(scope='session')
def database_url():
    return os.environ['DATABASE_URL']


@pytest.fixture(scope='session')
def test_database_url(test_db_prefix, database_url):
    test_url = make_url(database_url)
    test_url.database = test_db_prefix + test_url.database
    return test_url


@pytest.fixture(scope='session')
def test_db(database_url, test_database_url):
    engine = create_engine(database_url)
    conn = engine.connect()
    conn.execution_options(autocommit=False)
    conn.execute('ROLLBACK')

    try:
        conn.execute(f"DROP DATABASE {test_database_url.database}")
    except ProgrammingError:
        pass
    finally:
        conn.execute('ROLLBACK')

    logger.debug('Creating Test Database {}'.format(test_database_url.database))

    conn.execute("CREATE DATABASE {}".format(test_database_url.database))

    conn.close()
    engine.dispose()


@pytest.fixture(scope='session')
def sqlalchemy_base():
    raise ValueError('Please supply sqlalchemy_base fixture')


@pytest.fixture(scope='session')
def sqlalchemy_session_class():
    raise ValueError('Please supply sqlalchemy_session_class fixture')


@pytest.fixture(scope='session')
def engine(test_database_url):
    return create_engine(test_database_url)


@pytest.yield_fixture(scope='session')
def tables(engine, sqlalchemy_base, test_db):
    sqlalchemy_base.metadata.create_all(engine)
    yield
    sqlalchemy_base.metadata.drop_all(engine)


@pytest.yield_fixture(scope='function')
def db_session(engine, tables, sqlalchemy_session_class):
    sqlalchemy_session_class.remove()
    with engine.connect() as connection:
        transaction = connection.begin_nested()
        sqlalchemy_session_class.configure(bind=connection)
        session = sqlalchemy_session_class()

        session.begin_nested()

        yield session

        session.close()
        transaction.rollback()

