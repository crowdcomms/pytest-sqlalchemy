from example_app.db import User

def test_create_user(db_session):
    user = User(name='The User')
    db_session.add(user)
    db_session.flush()
    assert db_session.query(User).count() == 1

def test_update_object(db_session):
    user = User(name='The User')
    db_session.add(user)
    db_session.flush()
    assert db_session.query(User).count() == 1

    user.name = 'Bongo'
    db_session.commit()

    db_session.query(User).filter(User.name=='Bongo').one()

def test_tests_run_in_transactions(db_session):
    assert db_session.query(User).count() == 0