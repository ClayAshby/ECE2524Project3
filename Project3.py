####################
# ECE 2524 Project 3
#
# Name: Clay Ashby
# File: Project3.py
# Description: This file allows the user to list directories...
# Version: 1
####################

import os       # Required library in order to access files and directories in a filesystem

# Asking the user for input
path = input("Enter the directory you wish to begin listing files from: ")
permissions = input("Would you like to see owner file permissions as well? y/n: ")
while permissions != "y" and permissions != "n":
    permissions = input("Invalid input: Would you like to see owner file permissions as well? y/n: ")
for root, directories, files in os.walk(path, topdown=True):
    for directory in directories:
        print(os.path.join(path, directory))
    for file in files:
        print(os.path.join(path, file))
        if permissions == "y":
            if os.access(path+file, os.R_OK):      # Testing if the file is readable
                print("\tr", end="")
            else:
                print("\t-", end="")
            if os.access(path+file, os.W_OK):      # Testing if the file is writable
                print("w", end="")
            else:
                print("-", end="")
            if os.access(path+file, os.X_OK):      # Testing if the file is executable
                print("x", end="")
            else:
                print("-", end="")
            print("\n")