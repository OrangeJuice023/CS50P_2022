# Gets the greeting of the user
greeting = input("Greeting: ").strip().lower()

# If the user says "hello", print $0
if "hello" in greeting:
    print("$0")
# If the user says a greeting with an "h", print $20
elif greeting[0] == "h":
    print("$20")

# If it does not start with letter "h"
else:
    print("$100")
