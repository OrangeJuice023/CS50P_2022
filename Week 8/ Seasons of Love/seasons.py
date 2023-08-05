# import necessary libraries
from datetime import date, datetime, timedelta, time
import inflect
import sys
import re

p = inflect.engine()

# initialize the main code
def main():

    received_date = input("Date of Birth: ")
    try:
        year, month, day = date_chckr(received_date)
    except:
        sys.exit("Invalid Date")


    print(calc_date(year, month, day))




def date_chckr(received_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", received_date):
        year, month, day = received_date.split("-")
        return year, month, day

def calc_date(year, month, day):
    date_frmt = date(int(year), int(month), int(day))
    curr_date = date.today()
    time_dff = curr_date - date_frmt
    calculated = int(time_dff.total_seconds() / 60)
    output_msg = p.number_to_words(calculated, andword="")
    return output_msg.capitalize() + " minutes"

if __name__ == "__main__":
    main()
