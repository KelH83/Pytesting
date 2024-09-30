import pytest
from lib.password_checker import *

def test_password_checker():
    password = PasswordChecker()
    result = password.check("Abc123Def")
    assert result == True
    with pytest.raises(Exception) as e:
        password.check("enter")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."