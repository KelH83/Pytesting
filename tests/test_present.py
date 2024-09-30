import pytest
from lib.present import *

def test_present():
    gift = Present()
    gift.wrap("laptop")
    with pytest.raises(Exception) as e:
        gift.wrap("laptop")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
    second_gift = Present()
    with pytest.raises(Exception) as e:
        second_gift.unwrap()
    second_error_message = str(e.value)
    assert second_error_message == "No contents have been wrapped."