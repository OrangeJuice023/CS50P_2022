# main function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # replaces the numerical value of the money with the dollar sign to a raw float value
     d_without = d.replace("$", "")

     #returns the value the converted dollar sign to a float value
     return float(d_without)


def percent_to_float(p):
    # replaces the numerical value of the percent tip to a raw float value
    percent_without = float(p.replace("%", ""))
    p_raw = percent_without / 100

    #returns the value the converted percent tip to a float value
    return (p_raw)



#calls the main function
main()
