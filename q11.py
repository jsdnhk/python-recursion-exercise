#!/usr/bin/env python3
import sys
#Show the reverse of a string(By using recursion helper)

def main():
    s = input("Enter a string to reverse: ")
    if not (type(s) == str and len(s.strip()) > 0):
        sys.stderr.write("Please input a valid string!")
        exit(1)
    # Find and display the Highest Common Factor
    s = str(s).strip()
    print("The reverse string of [%s] => %s" % (s, reverseDisplay(s)))

def reverseDisplay(value):
    return reverseDisplayHelper(value, len(value))

def reverseDisplayHelper(s, high):
    if high == 0: #Base case
        return ''
    else:
        return s[high - 1] + reverseDisplayHelper(s, high - 1)

main() # Call the main function