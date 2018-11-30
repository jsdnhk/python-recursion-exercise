#!/usr/bin/env python3
import sys
#Show the reverse of a string

def main():
    s = input("Enter a string to reverse: ")
    if not (type(s) == str and len(s.strip()) > 0):
        sys.stderr.write("Please input a valid string!")
        exit(1)
    # Find and display the Highest Common Factor
    s = str(s).strip()
    print("The reverse string of [%s] => %s" % (s, reverseDisplay(s)))

def reverseDisplay(value):
    if not value: #Base case
        return ''
    else:
        return value[-1] + reverseDisplay(value[0:-1])


main() # Call the main function