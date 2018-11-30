#!/usr/bin/env python3
import sys
import cmath
#Find the count of specific char inside a list of char (By using recursion helper)

def main():
    chars = eval(input("Enter a list of char: "))
    ch = input("Enter a char to find: ")
    if not (type(chars) == list and len([char.strip() for char in chars if isinstance(char, str) and len(char.strip()) == 1]) == len(chars)):
        sys.stderr.write("Please input a list of char!")
        exit(1)
    elif not (type(ch) == str and len(ch.strip()) == 1):
        sys.stderr.write("Please input a valid char!")
        exit(1)
    # Find the count of lower case chars inside a list of char
    chars = [char.strip() for char in chars if isinstance(char, str) and len(char.strip()) == 1]
    ch = ch.strip()
    print("The count of the char[%s] inside a list of char\n%s\n=> %s" % (ch, str(chars), count(chars, ch)))

def count(chars, ch):
    return countHelper(chars, ch, len(chars))

def countHelper(chars, ch, high):
    if high == 0: #Base case
        return 0
    else:
        if ord(chars[high - 1]) == ord(ch):
            return 1 + countHelper(chars, ch, high - 1)
        else:
            return countHelper(chars, ch, high - 1)

main() # Call the main function