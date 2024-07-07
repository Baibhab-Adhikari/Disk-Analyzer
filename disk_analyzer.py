"""
Author : Baibhab Adhikari
Github : https://github.com/Baibhab-Adhikari

A script to analyze disk space usage in a given directory.

This script traverses a given directory, calculates the size of each file and directory,
and converts these sizes to a user-specified unit (KB, MB, GB, or TB).
"""
# imports
import os

BYTES_PER_UNIT = 1024  # global const

def converter(size_bytes, choice):
    """
    Converts a file size from bytes to a specified unit.

    Parameters:
    size_bytes (int, float): The size of the file in bytes.
    choice (str): The unit to convert to. Should be one of the following:
                  'a' for kilobytes (KB),
                  'b' for megabytes (MB),
                  'c' for gigabytes (GB),
                  'd' for terabytes (TB).


    """
    if choice == 'a':
        return f"{size_bytes / BYTES_PER_UNIT:.3f} KB"
    if choice == 'b':
        return f"{size_bytes / (BYTES_PER_UNIT ** 2):.3f} MB"
    if choice == 'c':
        return f"{size_bytes / (BYTES_PER_UNIT ** 3):.3f} GB"
    if choice == 'd':
        return f"{size_bytes / (BYTES_PER_UNIT ** 4):.3f} TB"
    else:
        return f"{size_bytes} Bytes"

# set directory PATH for analysis and initial testing of the program
PATH = "/Users/baibhabb/Documents/REAPER Media"


# Dictionaries to store sizes
size_dir = {}
size_file = {}

# Traverse the directory tree
for dirpath, dirnames, filenames in os.walk(PATH):
    total_dir_size = 0
    # Calculate size_bytes of each file
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        # error handling
        try:
            file_size = os.path.getsize(file_path)
        except OSError:
            print(f"Could not access file: {file_path}")  
            file_size = 0
        size_file[file_path] = file_size
        total_dir_size += file_size
    # Store the total size_bytes of the directory
    size_dir[dirpath] = total_dir_size

# unit conversion:
choose = "wrong"

while choose.strip().lower() not in "abcd":
    choose = input("Please choose the conversion unit : \n'a' for bytes to KB\n'b' for bytes to MB\n'c' for bytes to GB\n'd' for bytes to TB\n")
print("Converted file sizes in user chosen unit:")
print("---------------------------------------------------------------------------------------------------------")
print("Directories: ")
print("---------------------------------------------------------------------------------------------------------")
for dirpath, size in size_dir.items():
    print(f"{dirpath}: {converter(size, choose)}")
print("---------------------------------------------------------------------------------------------------------")
print("Files: ")
print("---------------------------------------------------------------------------------------------------------")
for filepath, size in size_file.items():
    print(f"{filepath}: {converter(size, choose)}")
