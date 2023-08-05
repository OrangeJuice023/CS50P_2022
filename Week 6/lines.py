import sys

def main():

    # observe command line argument inputs
    observe_input()

    # observe the effect of opening a file
    try:
        with open(sys.argv[1]) as file:
            start_iterate = 0
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip() != "":
                    start_iterate +=1
        print(start_iterate)

    except FileNotFoundError:
        sys.exit("File not found")



# the function in observing cmd arg
def observe_input():
    if len(sys.argv) != 2:
        sys.exit("Too few or Too many arguments.")

    # observe if it is a python file
    if sys.argv[1][-2:] != "py":
        sys.exit("Not a python file")

if __name__ == "__main__":
    main()
