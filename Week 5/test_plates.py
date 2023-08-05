from plates import is_valid

def main():
    # Call the case functions
    test_case01()
    test_case02()
    test_case03()
    test_case04()
    test_case05()

# Checks if the plate case allows a maximum of 6 characters and a minimum of 2 characters
def test_case01():
    assert is_valid("b") == False
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("hello, world") == False
    assert is_valid("cs50") == True
    assert is_valid("Ilove") == True

# Check if the case error observes that the plates must start with at least two letters
def test_case02():
    assert is_valid("60LUKA") == False
    assert is_valid("BILLCLINTON") == False
    assert is_valid("my") == True
    assert is_valid("00") == False
    assert is_valid("67") == False


# Checks if the case error observes that numbers cannot be used in the middle of plate
def test_case03():
    assert is_valid("css500") == True
    assert is_valid("cs.,50") == False

# The first number can not be 0
def test_case04():
    assert is_valid("mv32") == True
    assert is_valid("DZWB04") == False


# Checks if the case error observes that no puncs are allowed
def test_case05():
    assert is_valid("PI32") == True
    assert is_valid("DZW.,B04") == False

if __name__ == "__main__":
    main()
