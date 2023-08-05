from numb3rs import validate

def main():
    test_no_frmt()
    test_true_range()

def test_no_frmt():
    assert validate("123.123.123.123") == True
    assert validate("1.2.3.4") == True
    assert validate("1") == False



def test_true_range():
    assert validate("1233.123.123.123") == False
    assert validate("Isweartogod") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.1.512") == False
    assert validate("255.255.255.255") == True
    assert validate("mario") == False
