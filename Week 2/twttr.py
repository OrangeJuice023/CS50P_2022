# Gets the word from the user
inputted_text = input("Input: ")

# Prints the outputted text
print("Output: ", end="")

# Initiates the list for potential vowels
all_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Starts a looping code through every letter
for lttr in inputted_text:

    # Checks every letter if they are vowel or not
    if not lttr in all_vowels:

        # Prints the letter
        print(lttr, end= "")

print()
