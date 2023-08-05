import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # declare the splitting of the digits for the IP address
    Ip_add = re.search("^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    splitter = ip.split(".")

    # start a conditional
    if Ip_add:
        for iterator in splitter:
            if int(iterator) < 0 or int(iterator) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
