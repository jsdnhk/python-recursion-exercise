#!/usr/bin/env python3
# Find the MI addition by recursion
# m(i) = 1/3 + 2/5 + 3/7 + ... + i/2i+1

from fractions import Fraction
import sys

def main():
    print("Calculate the result of m(i) = 1/3 + 2/5 + 3/7 + ... + i/2i+1")
    i = eval(input("Enter the i: "))
    if not (type(i) == int and i > 0):
        sys.stderr.write("Please input a non-zero positive integer!")
        exit(1)
    # Find and display the Highest Common Factor
    print("The result with i=%s => %s" % (i, str(mi(i))))

# The function for finding the mi, return class instance Fraction
def mi(i):
    if (i <= 1):
        return Fraction(1, 3)
    else:
        return Fraction(i, 2 * i + 1) + mi(i - 1)


main() # Call the main function