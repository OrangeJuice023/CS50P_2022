def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(strin):
    puncs = [".", " ", "!", "?"]
    two = 2
    six = 6


    # The plate must always start with two letters
    if strin[0:1].isalpha() == False:
        return False

    # All vanity plates must contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(strin) < two or len(strin) > six:
        return False

    # Vanity plates have can have numbers but cannot be used in the middle of a plate; they must come at the end.
    i = 0
    while i < len(strin):
        if strin[i].isalpha() == False:
            if strin[i] == "0":
                return False
            else:
                break
        i += 1


    # No punctuations are allowed
    for p in strin:
        if p in puncs:
            return False

    # If the tests are all valid, return True
    return True


main()
