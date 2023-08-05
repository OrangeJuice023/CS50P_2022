import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #initiate global variables
    prpr_frmt = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)

    if prpr_frmt:

        # initiate global variable

        grouped_up = prpr_frmt.group
        meridian = 12

        # Check for value errors
        if grouped_up(2):
            if int(grouped_up(2)) >= 60:
                raise ValueError

        if grouped_up(5):
            if int(grouped_up(5)) >= 60:
                raise ValueError

        # take into account the first place in the time place value
        hour_1st = int(grouped_up(1))
        if grouped_up(3) == "PM" and hour_1st != meridian:
            hour_1st += 12
        elif grouped_up(3) == "AM" and hour_1st == meridian:
            hour_1st -= 12
        if grouped_up(2) == None:
            first_place_time = f"{hour_1st:02}:00"
        else:
            first_place_time = f"{hour_1st:02}:{grouped_up(2)}"

        # take into account the second place in the time place value
        hour_2nd = int(grouped_up(4))
        if grouped_up(6) == "PM" and hour_2nd != meridian:
            hour_2nd += 12
        elif grouped_up(6) == "AM" and hour_1st == meridian:
            hour_2nd -= 12
        if grouped_up(5) == None:
            second_place_time = f"{hour_2nd:02}:00"
        else:
            second_place_time = f"{hour_2nd:02}:{grouped_up(5)}"


        # after getting data from each place value, return it in a 24 hour format
        prpr_frmt = f"{first_place_time} to {second_place_time}"
        return prpr_frmt

    else:
        raise ValueError



if __name__ == "__main__":
    main()
