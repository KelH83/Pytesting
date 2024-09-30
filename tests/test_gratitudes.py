from lib.gratitudes import *

def test_gratitudes():
    grat = Gratitudes()
    grat.add("your family")
    result = grat.format()
    assert result == "Be grateful for: your family"
    grat.add("your pets")
    extended_result = grat.format()
    assert extended_result == "Be grateful for: your family, your pets"