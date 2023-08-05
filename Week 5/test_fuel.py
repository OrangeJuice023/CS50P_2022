from fuel import convert, gauge
import pytest

# define the main function
def main():
    test_first_case()
    test_second_case()
    test_third_case()


# check the first case
def test_first_case():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
        convert("cat/dog")

# check the second case
def test_second_case():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


# check the third case
def test_third_case():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

if __name__ == "__main__":
    main()
