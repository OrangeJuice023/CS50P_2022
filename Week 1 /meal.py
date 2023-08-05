def main():
    ...# Gets the known time from user
    known_time_user = input('What time is it? ').strip()

    # Function call for time converter
    real_time_converted = convert(known_time_user)

    # Determines if break by looking if the value is between 7:00 and 8:00
    if 7 <= real_time_converted <= 8:
                print("breakfast time")

    # Determines if break by looking if the value is between 12:00 and 13:00
    elif real_time_converted >= 12 and real_time_converted <= 13:
                print("lunch time")
    # Determines if break by looking if the value is between 18:00 and 19:00
    elif 18 <= real_time_converted <= 19:
                print("dinner time")
    else:
           pass



def convert(real_time_converted):
    ...# Gets the value of hour and minute
    known_hours , known_minutes = real_time_converted.split(":")
       # Converts the time and hours into a floating point value and returns them
    raw_minute = float(known_minutes) / 60
    final_minute = raw_minute
    # Returns the value to the main function
    raw_hours = float(known_hours)
    final_hours = raw_hours
    return final_hours + final_minute


if __name__ == "__main__":
    main()
