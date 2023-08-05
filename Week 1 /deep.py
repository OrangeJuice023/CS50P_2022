# Gets the input from the user
input_to_question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

# Types out "Yes" if the following conditions were met: "42", "Forty Two", "forty-two"
if input_to_question == "forty-two" or input_to_question == "forty two":
    print("Yes")
elif input_to_question == "42":
    print("Yes")

# Otherwise print no
else:
    print("No")
