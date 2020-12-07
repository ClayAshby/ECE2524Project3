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
direc = os.listdir(path)
print("Directories: ")
for files in direc:
    if os.path.isdir(path+files):
        print(files)
print("\nFiles: ")
for files in direc:
    if os.path.isfile(path+files):
        print(files)
        if permissions == "y":
            if os.access(path + files, os.R_OK):  # Testing if the file is readable
                print("\tr", end="")
            else:
                print("\t-", end="")
            if os.access(path + files, os.W_OK):  # Testing if the file is writable
                print("w", end="")
            else:
                print("-", end="")
            if os.access(path + files, os.X_OK):  # Testing if the file is executable
                print("x", end="")
            else:
                print("-", end="")
            print("")