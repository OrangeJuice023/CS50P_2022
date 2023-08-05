import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # initiate a global variable
    um_fnder = re.findall(r'\b([U|u]m)\b', s, re.IGNORECASE)
    len_cnt = um_fnder
    return len(len_cnt)


...


if __name__ == "__main__":
    main()
