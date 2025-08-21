import os

# Specify the directory path (current directory by default)
directory = "D:/DB/UPC/"

# List and print all files and folders in the directory
for item in os.listdir(directory):
    print(item)
