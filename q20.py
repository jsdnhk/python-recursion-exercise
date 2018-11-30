#!/usr/bin/env python3
#Find the heximal from the decimal
import sys

def main():
    int_dec = eval(input("Enter the decimal number: "))
    if not (type(int_dec) == int and int_dec >= 0):
        sys.stderr.write("Please input a +ve decimal number")
        exit(1)
    print("The heximal from the decimal[%s] is: %s" % (int_dec, decimalToHex(int_dec)))

def decimalToHex(value):
    if value == 0: #Base case
        return ''
    else:
        remindar = value % 16
        str_hex_digit = ''
        if remindar in range(0, 10):
            str_hex_digit = str(remindar)
        elif remindar == 10:
            str_hex_digit = 'A'
        elif remindar == 11:
            str_hex_digit = 'B'
        elif remindar == 12:
            str_hex_digit = 'C'
        elif remindar == 13:
            str_hex_digit = 'D'
        elif remindar == 14:
            str_hex_digit = 'E'
        elif remindar == 15:
            str_hex_digit = 'F'
        return decimalToHex(value // 16) + str_hex_digit

main() # Call the main function