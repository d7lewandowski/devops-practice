from hello import hello, hello2


def test_hello():
    assert "hi" == hello()


def test_hello2():
    assert "Hi" == hello2()
