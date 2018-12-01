#!/usr/bin/env python3
# Find the file numbers of a directory
import os

def main():
    path = input("Enter a directory or a file: ").strip()

    try:
        print("The number of the files in [%s]: %s" % (path, getFiles(path)) )
    except:
        print("Directory or file does not exist")

def getFiles(path):
    count = 0
    if os.path.isfile(path):    #base case
        return 1
    else:    #if path is dir
        files = os.listdir(path)     #all files and dirs
        for file in files:
            count += getFiles(os.path.join(path, file))
    return count

main()
