import sys
import csv


def main():

    # Checks the command line for inputs
    command_line_checker()
    # for new csv file
    newcsv = []


    # Open the file and create a new csv file
    try:
        with open(sys.argv[1]) as openfile:
            observer = csv.DictReader(openfile)
            for iterate in observer:
                splitter = iterate["name"].split(",")
                newcsv.append({"first" : splitter[1].lstrip(), "last": splitter[0], "house": iterate["house"]})
        with open(sys.argv[2], "w") as newfile:
            inputter = csv.DictWriter(newfile, fieldnames=["first", "last", "house"])
            inputter.writerow({"first": "first", "last": "last", "house": "house"})
            for iterate in newcsv:
                inputter.writerow({"first": iterate["first"], "last": iterate["last"], "house": iterate["house"]})


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
    if sys.argv[1][-3:] == ".csv":
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
