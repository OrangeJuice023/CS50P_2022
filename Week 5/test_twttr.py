# import the function from another file
from twttr import shorten

def main():
    # call the test function
    test_deleter()

# test strings
def test_deleter():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"
    assert shorten("HELLO") == "HLL"
    assert shorten("TwItTeR") == "TwtTR"

# test numbers
def test_no():
    assert shorten("24") == "24"

# tests symbols and punctuations
def test_punc():
    assert shorten(",._-") == ",._-"

    
if __name__ == "__main__":
    main()
