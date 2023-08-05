# import the random library
import random


def main():

    # call get level() function
    i_l = get_level()
    generate_integer(i_l)


def get_level():
    # initiate a loop
    while True:

        try:

    # get the inputted level and check if it is between 1 and 3
            level = input("Please input your level: ")
            if level in ["1", "2", "3"]:
                    break
        except:
            pass
    return level

def generate_integer(inputted_level):

    intiator = 0
    for _ in range(10):
        leveler = 1

        # indexing into the get_level function, get a random integer
        if inputted_level == "1":
            integ_1 = random.randint(0,9)
            integ_2 = random.randint(0,9)

        elif inputted_level == "2":
            integ_1 = random.randint(10,99)
            integ_2 = random.randint(10,99)

        else:
            integ_1 = random.randint(100,999)
            integ_2 = random.randint(100,999)

        while True:
            print(f"{integ_1} + {integ_2} =")
            stored = input()

            if stored == str(integ_1 + integ_2):
                intiator += 1
                break
            elif stored != str(integ_1 + integ_2) and leveler != 3:
                print("EEE")
                leveler += 1
                continue
            else:
                print("EEE")
                print(f"{integ_1} + {integ_2} = {integ_1 + integ_2}")
                break

    # print the score
    print(intiator)


# end the function
if __name__ == "__main__":
    main()
