# Prints the initial amount value
print("Amount due: 50")


# Initiate  global variable
ad = 50
ca = 0

# Deliberately start a loop

while True:
    added_coins = int(input("Insert Coin: "))

    # Start a conditional statement
    if added_coins in [25, 10, 5]:

        # Subtract the value from the initial amount due
        ad -= added_coins
        # Add the value from the initial amount due
        ca += added_coins

    # Starts a conditional statement for money owed
    if ca >= 50:
        print("Changed owed: ", ca - 50)
        break
    else:
        print("Amount due: ", ad)
