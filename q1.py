#!/usr/bin/env python3
import sys

def main():
    i = eval(input("Enter the integer to sum the digits: "))
    if not (type(i) == int and i >= 0):
        sys.stderr.write("Please input a positive integer!")
        exit(1)
    # Find and display the Highest Common Factor
    print("The sum of the digits of [%s] => %s" % (i, sumDigits(i)))

def sumDigits(n):
    if (n == 0): #Base case
        return 0
    else:
        return (n % 10) + sumDigits(n // 10)


main() # Call the main function