# Initialize an empty dictionary
g_item = {}

# Initialize a loop
while True:

    # Initiates a try statement
    try:
        # Get input from user
        a_item = input().lower()

    # Initiates the error catcher
    except EOFError:
        print()
        break

    # Iterates and checks every item
    if a_item in g_item:

        # If avaible, then add it to the total count
        g_item[a_item] += 1

    # Otherwise add the item for the first time
    else:
        g_item[a_item] = 1

sorted_item = sorted(g_item.keys())
# Prints the available items in alphabetical order
for selector in sorted_item:
    print(g_item[selector], selector.upper())
