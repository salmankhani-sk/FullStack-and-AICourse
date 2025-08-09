from expt2 import login
def test_login():
    assert login("admin","1234") == True
def test_login_fail():
    assert login("user","pass") == False