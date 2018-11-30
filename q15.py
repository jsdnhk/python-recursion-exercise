#!/usr/bin/env python3
import sys
import cmath
#Find the count of lower case chars inside a list of char (By using recursion helper)

def main():
    chars = eval(input("Enter a list of char to find the count of lower cases: "))
    if not (type(chars) == list and len([char.strip() for char in chars if isinstance(char, str) and len(char.strip()) == 1]) == len(chars)):
        sys.stderr.write("Please input a list of char!")
        exit(1)
    # Find the count of lower case chars inside a list of char
    chars = [char.strip() for char in chars if isinstance(char, str) and len(char.strip()) == 1]
    print("The count of lower case chars inside a list of char\n%s\n=> %s" % (str(chars), count(chars)))

def count(chars):
    return countHelper(chars, len(chars))

def countHelper(chars, high):
    if high == 0: #Base case
        return 0
    else:
        if (ord(chars[high - 1]) in range(ord('a'), ord('z') + 1)):
            print("return 1 + countHelper(chars, %s - 1)" % (high))
            return 1 + countHelper(chars, high - 1)
        else:
            print("return countHelper(chars, %s - 1)" % (high))
            return countHelper(chars, high - 1)

main() # Call the main function