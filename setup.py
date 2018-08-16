#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-sqlalchemy',
    version='0.2.0',
    author='Ben Harling',
    author_email='bharling@crowdcomms.co.uk',
    maintainer='Ben Harling',
    maintainer_email='bharling@crowdcomms.co.uk',
    license='MIT',
    url='https://github.com/bharling/pytest-sqlalchemy',
    description='SqlAlchemy convenience stuff for pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_sqlalchemy'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
        'pytest>=3.5.0', 'sqlalchemy>=1.2.7', 'psycopg2>=2.7.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'sqlalchemy = pytest_sqlalchemy',
        ],
    },
)
