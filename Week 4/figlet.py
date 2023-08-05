# imports the libraries
import sys
import random
from pyfiglet import Figlet


# define the figlet function
figlet = Figlet()

# extract a list of fonts
data_fonts = figlet.getFonts()


# command line argument checker
if len(sys.argv) == 1:
    cmd_check = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    cmd_check = False
else:
    sys.exit("Error in the command line")

# receives the font logic
if cmd_check == False:
    try:
        figlet.setFont(font = sys.argv[2])
    except:
        print("Invalid Usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts(data_fonts))







# gets inputted text from user
gets_text = input("User, please input: ")

# prints the final text
print(figlet.renderText(gets_text))
