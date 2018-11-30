#!/usr/bin/env python3
#Find the binary from the decimal
import sys

def main():
    int_dec = eval(input("Enter the decimal number: "))
    if not (type(int_dec) == int and int_dec >= 0):
        sys.stderr.write("Please input a +ve decimal number")
        exit(1)
    print("The binary from the decimal[%s] is: %s" % (int_dec, decimalToBinary(int_dec)))

def decimalToBinary(value):
    if value == 0: #Base case
        return ''
    else:
        return decimalToBinary(value // 2) + str(value % 2)

main() # Call the main function