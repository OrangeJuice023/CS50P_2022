# Gets the desired mathematical expression from user and splits the value
math_expression = input("Expression: ").split(" ")

# Converts the math expression into variables
first, second, third = math_expression

# Floats the assigned variables
new_first = float(first)
new_third = float(third)

# Executes the mathematical operation
if second == "+":
    output = new_first + new_third
elif second == "-":
    output = new_first - new_third
elif second == "*":
    output = new_first * new_third
elif second == "/":
    output = new_first / new_third
print(output)
