# import library
import inflect

p = inflect.engine()

# list their names and append Adieu, Aidue

listed_name = []

# start a while loop
while True:
    try:
        get_name = input("Type name here: ")
    except EOFError:

        # stops the loop
        print()
        break
    listed_name.append(get_name)

# Use the inflect module
goodbye = p.join(listed_name)

# append the "Adieu, adieu to + the stored names
stored = f"Adieu, adieu, to {goodbye}"
print(stored)
