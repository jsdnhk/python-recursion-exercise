#!/usr/bin/env python3
import sys
#Find the string count of a string

def main():
    s = input("Enter a string to search: ")
    a = input("Enter a string to look: ")
    if not (type(s) == str and len(s.strip()) > 0):
        sys.stderr.write("Please input a valid string!")
        exit(1)
    elif not (type(a) == str and len(a.strip()) > 0):
        sys.stderr.write("Please input a valid string!")
        exit(1)
    # Find and display the Highest Common Factor
    s, a = str(s).strip(), str(a).strip()
    print("The count of the part[%s] inside a string[%s] => %s" % (a, s, count(s, a)))

def count(s, a):
    return countHelper(s, a, len(s))

def countHelper(s, a, high):
    if high <= 0:
        return 0
    else:
        if s[0:high].endswith(a):
            return 1 + countHelper(s, a, high - len(a))
        else:
            return countHelper(s, a, high - 1)

main() # Call the main function