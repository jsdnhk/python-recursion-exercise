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
    if not s: #Base case 1
        return 0
    elif not a: #Base case 2
        return 0
    else:
        if s.startswith(a):
            return 1 + count(s[len(a):len(s)], a)
        else:
            return count(s[1:len(s)], a)

main() # Call the main function