import sys
from os.path import splitext
from PIL import Image, ImageOps
import os

# global argument variable
global_arg = sys.argv



def main():
    # calls the cmd checker function
    command_line_checker()
    # extensions
    file_ext = [".jpg", "jpeg", "png."]
    first_file_ext = splitext(global_arg [1])
    second_file_ext = splitext(global_arg [2])
    opened_img = Image.open("shirt.png")
    opened_img_size = opened_img.size

    if first_file_ext[1] == second_file_ext[1] and first_file_ext[1] in file_ext:
        try:
            presented_img = Image.open(global_arg[1])
        except FileNotFoundError:
            sys.exit("File does not exit")

        # width and height of the image
        presented_img = ImageOps.fit(presented_img, opened_img_size)
        presented_img.paste(opened_img, opened_img)
        presented_img.save(global_arg[2])

    elif first_file_ext[1] != second_file_ext[1]:
        sys.exit("Not Same Extensions")

    else:
        sys.exit("Invalid output")


def command_line_checker():
    # store sys.argv in a variable
    arg_input = len(sys.argv)

    # Check how many elements in the command line
    if arg_input != 3:
        sys.exit("Too few or Too many arguments.")



if __name__ == "__main__":
    main()
