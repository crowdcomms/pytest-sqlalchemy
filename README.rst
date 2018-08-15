=================
pytest-sqlalchemy
=================

.. image:: https://img.shields.io/pypi/v/pytest-sqlalchemy.svg
    :target: https://pypi.org/project/pytest-sqlalchemy
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-sqlalchemy.svg
    :target: https://pypi.org/project/pytest-sqlalchemy
    :alt: Python versions

.. image:: https://travis-ci.org/bharling/pytest-sqlalchemy.svg?branch=master
    :target: https://travis-ci.org/bharling/pytest-sqlalchemy
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/bharling/pytest-sqlalchemy?branch=master
    :target: https://ci.appveyor.com/project/bharling/pytest-sqlalchemy/branch/master
    :alt: See Build Status on AppVeyor

SqlAlchemy convenience stuff for pytest

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

* Provides basic utility fixtures to aid in testing projects with sqlalchemy
* Allows you to wrap test cases in sqlalchemy transactions much like django's TestCase class


Requirements
------------

* pytest, sqlalchemy, psycopg2 ( all installed during setup process )


Installation
------------

You can install "pytest-sqlalchemy" via `pip`_ from `GitHub`_

.. code-block:: shell

    $ pip install -e git+https://github.com/crowdcomms/pytest-sqlalchemy.git#egg=pytest-sqlalchemy


Usage
-----

The plugin will create a completely new test database that lasts as long as the test session and is destroyed at the end.
You can execute each test case in an isolated transaction by including the ``db_session`` fixture, eg:

.. code-block:: python

    def test_create_foo(db_session):
        foo = Foo(name="bar")
        db_session.add(foo)
        db_session.commit()
        assert db_session.query(Foo).count()

The transaction is automatically rolled back at the end of the test function giving you a clean slate for the next test.

You need to define a couple of fixtures to be able to use the plugin, this is mostly to 'patch' your existing Session and Base classes to use the testing database. This is probably the most tricky bit of the plugin as sqlalchemy usage in projects can vary somewhat

Required fixtures
^^^^^^^^^^^^^^^^^
``sqlalchemy_base_class``

You must set this to your base class that you use for defining models in your project, eg:

.. code-block:: python

    # my_project/tests/conftest.py

    from my_project.database import Base

    @pytest.fixture(scope='session')
    def sqlalchemy_base():
        return Base

``sqlalchemy_session_class``

Use this fixture to supply your project's sqlalchemy Session factory, eg:

.. code-block:: python

    # my_project/database.py

    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import scoped_session, sessionmaker

    Base = declarative_base()
    Session = scoped_session(sessionmaker())

    ...

    # my_project/tests/conftest.py

    from my_project.database import Session

    @pytest.fixture(scope='session')
    def sqlalchemy_session_class():
        return Session

If your project uses a different way to obtain a sqlalchemy session, then you'll need to figure out some other way to configure that session to use the test database, possibly by mocking it in individual test cases.

Optional Fixtures
^^^^^^^^^^^^^^^^^

``database_url``

This defaults to ``os.environ['DATABASE_URL']`` but is designed to be overridden to supply an alternative. The plugin will attempt to connect to whatever database is specified and create another database alongside the original, prefixed with ``test_``

``test_db_prefix``

If you don't like ``test_`` as a prefix for your testing database, return something else here.

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.
