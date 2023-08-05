# imports from the bank file
from bank import value

def main():

    # Call test functions
    test_call_1_0()
    test_call_2_20()
    test_call_3_100()

# Test first case
def test_call_1_0():
    assert value("hello si") == 0
    assert value("Hello") == 0
    assert value("Hello SI") == 0
    assert value("HELLOUR") == 0

# Test second case
def test_call_2_20():
    assert value("hlak") == 20
    assert value("hey") == 20
    assert value("hauf") == 20
    assert value("hoy") == 20

# Test third case
def test_call_3_100():
    assert value("tra g?") == 100
    assert value("ano na boss?") == 100

if __name__ == "__main__":
    main()
