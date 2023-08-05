from validator_collection import validators

def main():
    print(check(input("What's your email address? ")))

def check(inputted_email):

    try:
        checking = validators.email(inputted_email)
        return "Valid"
    except:
        return "Invalid"





if __name__ == "__main__":
    main()
