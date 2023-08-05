# Initiates a list of months
list_mos = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# Initiates a looping sequence
while True:

    # Gets information from user
    date_input = input("Date: ")
    try:
        # Splits the date
        m_input, d_input, y_input = date_input.split("/")

        checker = (int(m_input) >= 1 and int(m_input) <= 12) and (int(d_input) >= 1 and int(d_input) <= 31)

        # Check if the moths and days fit
        if checker:

            # Breaks out of the loop
            break

    except:

        try:

            # Splits the inputted date and removes comma from the day format
            oldvalue_date = date_input.split(" ")
            old_i_m, old_i_d, y_input = oldvalue_date


            # Iterates through the list to find the number of the month
            for n in range(len(list_mos)):
                if old_i_m == list_mos[n]:
                    m_input = n + 1

            # Removes comma from day input
            oldday = old_i_d.replace(",","")
            d_input = oldday

            # Check if the moths and days fit
            if (int(m_input) >= 1 and int(m_input) <= 12) and (int(d_input) >= 1 and int(d_input) <= 31):

                # Breaks out of the loop
                 break
        except:
            # Next line
            print()
            pass

# Adds a 0 prefix if month and day is less than ten
# Then prints the result
print(f"{y_input}-{int(m_input):02}-{int(d_input):02}")
