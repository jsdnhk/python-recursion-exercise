#!/usr/bin/env python3
"""
#Recursion Solution:
def main():
    index = eval(input("Enter an index for a Fibonacci number: "))
    # Find and display the Fibonacci number
    print("The Fibonacci number at index", index, "is", fib(index))

# The function for finding the Fibonacci number
def fib(index):
    if index == 0: # Base case
        return 0
    elif index == 1: # Base case
        return 1
    else:  # Reduction and recursive calls
        return fib(index - 1) + fib(index - 2)

main() # Call the main function
"""
def main():
    index = eval(input("Enter an index for a Fibonacci number(By Iteration): "))
    # Find and display the Fibonacci number
    print("After the loop, the Fibonacci number at index", index, "is", fib(index))

# The function for finding the Fibonacci number
def fib(index):
    f0, f1 = 0, 1
    if index == 0: # Base case
        return f0
    elif index == 1: # Base case
        return f1
    #Iterative Loop(from low->high), n >= 2
    cur_fib = 0
    prev_fib = f1
    prev_2_fib = f0
    for i in range(2, index + 1):
        cur_fib = prev_2_fib + prev_fib
        prev_2_fib = prev_fib
        prev_fib = cur_fib
    return cur_fib


main() # Call the main function
