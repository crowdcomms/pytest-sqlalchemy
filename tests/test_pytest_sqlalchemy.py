# -*- coding: utf-8 -*-

def test_db_prefix_fixture(testdir):

    testdir.makepyfile("""
        def test_dbprefix(db_prefix):
            assert db_prefix == "test"
    """)

    result = testdir.runpytest(
        '-v'
    )

    result.stdout.fnmatch_lines([
        '*::test_dbprefix PASSED*',
    ])