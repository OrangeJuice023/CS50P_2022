import sys
import csv


def main():

    # Checks the command line for inputs
    command_line_checker()


    # Open the file and create a new csv file
    try:
        with open(sys.argv[1]) as openfile:
            observer = csv.DictReader(openfile)
            with open(sys.argv[2], "w") as readfile:
                iterator = csv.DictWriter(readfile, fieldnames=["first", "last", "house"])
                iterator.writeheader()
                for iterate in observer:
                    iterate["first"] = iterate.pop("name")
                    username, name = iterate["first"].split(",")
                    iterate["first"] = name
                    iterate["last"] = username
                    iterator.writerow(iterate)

    # Observe if the file can be open, if not then the file could not be read
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")



def command_line_checker():

    # store sys.argv in a variable
    arg_input = len(sys.argv)

    # Check how many elements in the command line
    if arg_input != 3:
        sys.exit("Too few or Too many arguments.")

    # Check if the file is CSV
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
