from lib.report_length import *

def test_report_length():
    empty_string = report_length('')
    assert empty_string == "This string was 0 characters long."
    five_chars = report_length('hello')
    assert five_chars == "This string was 5 characters long."
    twenty_chars = report_length('hello, who are you? ')
    assert twenty_chars == "This string was 20 characters long."