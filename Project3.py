####################
# ECE 2524 Project 3
#
# Name: Clay Ashby
# File: Project3.py
# Description: This file allows the user to enter a file path, along with whether the user
#              wants to see the owner file permissions and file sizes.
#              The program display all directories and files in the given path and sorts
#              them respectively.
# Version: 1
####################

import os       # Required library in order to access files and directories in a filesystem

# Asking the user for inputs
path = input("Enter the directory you wish to list files and directories from: ")
while path[-1] != "/" and path[-1] != "\\":
    print("Invalid input: Ensure the file path ends in '\\' for Windows or '/' for Linux machines")
    path = input("Enter the directory you wish to list files and directories from: ")
permissions = input("Would you like to see owner file permissions as well? y/n: ")
# Validating permissions input
while permissions != "y" and permissions != "n":
    permissions = input("Invalid input: Would you like to see owner file permissions as well? y/n: ")
size = input("Would you like to see the file sizes? y/n: ")
# Validating size input
while size != "y" and size != "n":
    size = input("Invalid input: Would you like to see the file sizes? y/n: ")
# Creating a list of files and directories
direc = os.listdir(path)
# Printing out the directories first
print("\nDirectories: ")
for files in direc:
    if os.path.isdir(path+files):
        print(files)
# Printing out the files second along with permissions/size if wanted
print("\nFiles: ")
for files in direc:
    if os.path.isfile(path+files):
        print(files)
        if size == "y":
            n = os.stat(path + files).st_size
            if n < 1024:
                print("   Size: "+str(round(n, 2))+" bytes")
            elif 1024 <= n < 1048576:
                print("   Size: "+str(round((n/1024), 2))+" KB")
            elif 1048576 <= n < 1073741824:
                print("   Size: " + str(round((n/1048576), 2))+" MB")
            else:
                print("   Size: " + str(round((n/1073741824), 2))+" GB")
        if permissions == "y":
            if os.access(path + files, os.R_OK):  # Testing if the file is readable
                print("   r", end="")
            else:
                print("   -", end="")
            if os.access(path + files, os.W_OK):  # Testing if the file is writable
                print("w", end="")
            else:
                print("-", end="")
            if os.access(path + files, os.X_OK):  # Testing if the file is executable
                print("x", end="")
            else:
                print("-", end="")
            print("")