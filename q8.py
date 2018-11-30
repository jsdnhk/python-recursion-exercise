#!/usr/bin/env python3
import sys
#Show the reverse of an integer

def main():
    i = eval(input("Enter an integer to reverse: "))
    if not (type(i) == int and i >= 0):
        sys.stderr.write("Please input a positive integer!")
        exit(1)
    # Find and display the Highest Common Factor
    print("The reverse number of [%s] => %s" % (i, reverseDisplay(i)))

def reverseDisplay(value):
    if (value == 0): #Base case
        return 0
    else:
        return ((value % 10) * (10 ** (len(str(value)) - 1))) + reverseDisplay(value // 10)


main() # Call the main function