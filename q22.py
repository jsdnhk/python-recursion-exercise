#!/usr/bin/env python3
#Find the decimal from the hexadecimal
import sys
HEX_DICT = \
    {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

def main():
    str_hex = input("Enter the hexadecimal number: ").strip().upper()
    if not (type(str_hex) == str and len([c for c in str_hex if c in HEX_DICT.keys()]) == len(str_hex)):
        sys.stderr.write("Please input a +ve hexadecimal number")
        exit(1)
    print("The decimal from the hexadecimal[%s] is: %s" % (str_hex, hexToDecimal(str_hex)))

def hexToDecimal(hexString):
    return hexToDecimalHelper(hexString, 0)

def hexToDecimalHelper(hexString, low):  #return int
    if low == len(hexString): #Base case
        return 0
    else:
        ch_hex = hexString[(len(hexString) - 1) - low]
        int_hex = int(HEX_DICT[ch_hex]) * 16 ** low
        return int_hex + hexToDecimalHelper(hexString, low + 1)

main() # Call the main function