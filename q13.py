#!/usr/bin/env python3
import sys
#Find the count of upper-case letters in a string

def main():
    str_word = input("Enter a string to find the count of upper-case letters: ").strip()
    if not (type(str_word) == str and len(str_word) > 0):
        sys.stderr.write("Please input a string!")
        exit(1)
    # Find the count of upper-case letters in a string
    print("The count of upper-case letters in a string [%s] => %s" % (str(str_word), countUppercase(str_word)))

def countUppercase(s):
    return countUppercaseHelper(s, len(s))

def countUppercaseHelper(s, high):
    if high == 0: #Base case
        return 0
    else:
        return (1 if ord(s[high - 1]) in range(ord('A'),ord('Z') + 1) else 0) + countUppercaseHelper(s, high - 1)

main() # Call the main function