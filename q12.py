#!/usr/bin/env python3
import sys
import cmath
#Find the greatest number inside a list of numbers (By using recursion helper)

def main():
    list_num = eval(input("Enter a list of numbers to find the greatest: "))
    if not (type(list_num) == list and len([num for num in list_num if isinstance(num, int)]) == len(list_num)):
        sys.stderr.write("Please input a list of all integers!")
        exit(1)
    # Find the greatest number of a list
    print("The greatest number inside a list of numbers\n%s\n=> %s" % (str(list_num), findGreatestNum(list_num)))

def findGreatestNum(list_num):
    return findGreatestNumHelper(list_num, len(list_num))

def findGreatestNumHelper(list_num, high):
    if high == 0: #Base case
        return list_num[high]
    else:
        return max(list_num[high - 1], findGreatestNumHelper(list_num, high - 1))

main() # Call the main function