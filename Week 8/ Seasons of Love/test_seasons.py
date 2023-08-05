from seasons import date_chckr

def main():
    test_case1()



def test_case1():
    assert date_chckr("March 31, 2022") == None
    assert date_chckr("2022-8-4") == None
    assert date_chckr("2022-08-04") == ("2022", "08", "04")



if __name__ == "__main__":
    main()
