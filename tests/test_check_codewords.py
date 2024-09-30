from lib.check_codeword import *

def test_check_codeword():
    positive_result = check_codeword("horse")
    assert positive_result == "Correct! Come in."
    almost_result = check_codeword("hope")
    assert almost_result == "Close, but nope."
    negative_result = check_codeword("please")
    assert negative_result == "WRONG!"
