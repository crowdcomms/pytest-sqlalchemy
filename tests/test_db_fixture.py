from example_app.db import User

def test_create_user(db_session):
    user = User(name='The User')
    db_session.add(user)
    db_session.flush()
    assert db_session.query(User).count() == 1

def test_tests_run_in_transactions(db_session):
    assert db_session.query(User).count() == 0