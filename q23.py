#!/usr/bin/env python3
import sys
import cmath
#Find the permuations of a string (By using recursion helper)

def main():
    str_word = input("Enter a string: ").strip()
    if not (type(str_word) == str and str_word):
        sys.stderr.write("Please input a valid string!")
        exit(1)
    # Find the permuations of a string
    print("The permuations of a string[%s]: " % (str_word))
    displayPermuation(str_word)

def displayPermuation(s):
    return displayPermuationHelper("", s)

def displayPermuationHelper(s1, s2):
    print("displayPermuationHelper(%s, %s)" % (s1, s2))
    if not s2:
        print(s1)
    else:
        for idx in range(0, len(s2)):
            displayPermuationHelper(s1 + s2[idx], s2.replace(s2[idx], ''))

main() # Call the main function