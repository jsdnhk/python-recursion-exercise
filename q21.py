#!/usr/bin/env python3
#Find the decimal from the binary
import sys

def main():
    str_bin = input("Enter the binary number: ").strip()
    if not (type(str_bin) == str and len([c for c in str_bin if c in ('0','1')]) == len(str_bin)):
        sys.stderr.write("Please input a +ve binary number")
        exit(1)
    print("The decimal from the binary[%s] is: %s" % (str_bin, binaryToDecimal(str_bin)))

def binaryToDecimal(binaryString):
    return binaryToDecimalHelper(binaryString, 0)

def binaryToDecimalHelper(binaryString, low):  #return int
    if low == len(binaryString): #Base case
        return 0
    else:
        int_b = int(binaryString[(len(binaryString) - 1) - low]) * 2 ** low
        return int_b + binaryToDecimalHelper(binaryString, low + 1)

main() # Call the main function