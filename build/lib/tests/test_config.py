import pytest

class WrongURL(Exception):

    def __init__(self, message = "Incorrect URL") :
        self.message = message
        super().__init__(self.message)


def test_generic():
    a=5
    with pytest.raises(WrongURL):
        if a not in range(10,20):
            raise WrongURL