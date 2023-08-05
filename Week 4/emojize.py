# imports the emojize library
import emoji

# gets import from user
u_info = input("User ,Input your emoji: ").lower()

# stores the emoji selected
emoji_stored = emoji.emojize(u_info, language="alias")

# prints the emoji
print("Emoji: ", emoji_stored)
