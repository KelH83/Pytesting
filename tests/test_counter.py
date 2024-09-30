from lib.counter import *

def test_counter():
    count = Counter()
    count.add(3)
    result = count.report()
    assert result == "Counted to 3 so far."