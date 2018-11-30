#!/usr/bin/env python3
# Find the HCF(Highest Common Factor)/GCD(Greatest Common Divisor) by recursion
import sys

def main():
    int1 = eval(input("Enter the 1st integer: "))
    int2 = eval(input("Enter the 2st integer: "))
    if type(int1) != int or type(int2) != int:
        sys.stderr.write("Please input a non-zero positive integer!")
        exit(1)
    elif int1 <= 0 or int2 <= 0:
        sys.stderr.write("Please input a non-zero positive integer!")
        exit(1)
    # Find and display the Highest Common Factor
    print("The Highest Common Factor of %s and %s => %s" % (int1, int2, hcf(int1, int2)))

# The function for finding the Highest Common Factor
def hcf(int1, int2):
    int1, int2 = [int2, int1] if int1 < int2 else [int1, int2]
    if (int1 % int2 == 0):
        return int2
    else:
        return hcf(int2, int1 % int2)
    return None     #impossible!


main() # Call the main function