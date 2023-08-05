# Initiate a food directory
f_dir = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


# Set a starting amount to 0
start_amt = 0

# Initiate a loop sequence
while True:

    # Initiate a try statement
    try:

        # Gets information from user
        s_item = input("Item: ").title()


    # If errors are detected
    except EOFError:

        # Initiate the print function and get out of the loop
        print()
        break

    # Iterates through the dictionary to check if its available
    if s_item in f_dir:

        # Add the item price to the starting amount
        start_amt += f_dir[s_item]

        # Print the total calculated amount
        print("Total: $", "{:.2f}".format(start_amt), sep ="")
