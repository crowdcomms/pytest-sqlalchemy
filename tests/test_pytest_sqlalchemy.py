# -*- coding: utf-8 -*-

def test_db_prefix_fixture(testdir):

    testdir.makepyfile("""
        def test_dbprefix(test_db_prefix):
            assert test_db_prefix == "test_"
    """)

    result = testdir.runpytest(
        '-v'
    )

    result.stdout.fnmatch_lines([
        '*::test_dbprefix PASSED*',
    ])