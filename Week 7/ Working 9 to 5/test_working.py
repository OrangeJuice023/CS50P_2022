from working import convert
import pytest

checker = pytest.raises
def main():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()

def test_case_1():
    with checker(ValueError):
        assert convert("9-00 AM to 5-00PM")

def test_case_2():
    with checker(ValueError):
        assert convert("9:70 AM to 9:70PM")
    with checker(ValueError):
        assert convert("9AM to 8PM")
    with checker(ValueError):
        assert convert("9:00 to 17:00")
    with checker(ValueError):
        assert convert("9 AM - 8 PM")
    with checker(ValueError):
        assert convert("13 AM to  25 PM")
    with checker(ValueError):
        assert convert("11:00 AM, 14:00 PM")
    with checker(ValueError):
        assert convert("12:70 PM to 8 PM")


def test_case_3():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_case_4():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("8 AM to 12 PM") == "08:00 to 12:00"

if __name__ == "__main__":
    main()
