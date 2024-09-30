from lib.greet import *

def test_greet_returns_correct_message():
    result = greet('Kelly')
    assert result == 'Hello, Kelly!'