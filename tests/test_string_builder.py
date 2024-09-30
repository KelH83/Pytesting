from lib.string_builder import *

def test_string_builder():
    string = StringBuilder()
    string.add("hello")
    size_result = string.size()
    output_result = string.output()
    assert size_result == 5
    assert output_result == "hello"