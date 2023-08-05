# Initiate a loop using a while logic
while True:

    # Get a fractional fuel gauge but should be strictly a number
    f_gauge = input("Fraction: ")

    # Finds if the is composed of acceptable value
    accept_ix = f_gauge.find("/")

    try:
        # Splits the fuel gauge value and converts to an int
        num_gauge = int(f_gauge[:accept_ix])
        den_gauge = int(f_gauge[accept_ix+1:])

        #Calculates the percentage
        split = num_gauge / den_gauge

        if num_gauge > den_gauge:
            continue
        break

    except (ValueError, ZeroDivisionError):
        continue

# Converts the decimal to percent
percentile = int(split * 100)

# If less than 1, print E
if percentile <= 1:
    print("E")

# If greater than 99, print F
elif percentile >= 99:
    print("F")

# Otherwise, just print the percent
else:
    print(str(percentile) + "%")
