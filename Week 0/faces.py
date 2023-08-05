# main code that prints the final output

def main():

    #gets the user input with converted emoji
    emoji_with_text = input("Dear user, enter here your text:")

    #gets the converter code
    final = convert(emoji_with_text)

    #prints the text with converted emoji
    print(final)

def convert(emoji_with_text):

    #converts the happy emoji text to happy emoji
    user_text1 = emoji_with_text.replace(":)", "🙂")

    #converts the sad emoji text to sad emoji
    user_text2 = user_text1.replace(":(", "🙁")

    #return string
    return user_text2

#call the main function
main()
