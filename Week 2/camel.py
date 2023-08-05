# Gets the user input in a CamelCase format
C_case = input ("camelCase: ")

# Removes the /n for the result of snake_case
S_case = ""

# Starts a loob to look through every letter to see the casing
for l in C_case:

    # Check if the letter is upper case
    if l.isupper():

        # Print underscores and the letter in lowercase
        S_case = S_case + "_" + l.lower()

    # Otherwise if no uppercase, just print letter
    else:
        S_case += l

print("snake_case: ", S_case)
