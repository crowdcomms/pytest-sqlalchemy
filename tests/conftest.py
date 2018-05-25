import pytest
pytest_plugins = 'pytester'

from example_app.db import Base, session

@pytest.fixture(scope='session')
def sqlalchemy_base():
    return Base

@pytest.fixture(scope='session')
def sqlalchemy_session():
    return session
