import sys
import csv
from tabulate import tabulate
def main():
    # Create the table
    command_line_checker()

    # Create a list for data
    menu = []

    # Open the file
    try:
        with open(sys.argv[1], "r") as csvfile:
            observer = csv.reader(csvfile)
            for row in observer:
                menu.append(row)

    # Observe if the file can be open, if not then the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")


    # Print table
    print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))


def command_line_checker():

    # Check how many elements in the command line
    if len(sys.argv) != 2:
        sys.exit("Too few or Too many arguments.")

    # Check if the file is CSV
    if sys.argv[1][-3:] != "csv":
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
