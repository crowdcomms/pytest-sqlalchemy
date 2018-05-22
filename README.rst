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

You can install "pytest-sqlalchemy" via `pip`_ from `GitHub`_::

    $ pip install -e git+https://github.com/crowdcomms/pytest-sqlalchemy.git#egg=pytest-sqlalchemy


Usage
-----

You need to provide a couple of fixtures to inject your sqlalchemy Base and Session classes ( the ones your regular app uses ). eg::

    # my_project/tests/conftest.py
    
    from my_app.db import Base, Session

    @pytest.fixture(scope='session')
    def sqlalchemy_base():
        return Base

    @pytest.fixture(scope='session')
    def sqlalchemy_session():
        return Session


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.
