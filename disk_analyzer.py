
"""
Author : Baibhab Adhikari
Github : https://github.com/Baibhab-Adhikari

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
        return f"{size_bytes / BYTES_PER_UNIT} KB"
    if choice == 'b':
        return f"{size_bytes / (BYTES_PER_UNIT ** 2)} MB"
    if choice == 'c':
        return f"{size_bytes / (BYTES_PER_UNIT ** 3)} GB"
    if choice == 'd':
        return f"{size_bytes / (BYTES_PER_UNIT ** 4)} TB"

# set directory PATH for analysis and initial testing of the program
PATH = "/Users/baibhabb/Documents/Notes_Diagrams"


# Dictionaries to store sizes
size_dir = {}
size_file = {}

# Traverse the directory tree
for dirpath, dirnames, filenames in os.walk(PATH):
    TOTAL_DIR_SIZE = 0
    # Calculate size_bytes of each file
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_size = os.path.getsize(file_path)
        size_file[file_path] = file_size
        TOTAL_DIR_SIZE += file_size
    # Store the total size_bytes of the directory
    size_dir[dirpath] = TOTAL_DIR_SIZE

# unit conversion:
CHOOSE = "wrong"

while CHOOSE.strip().lower() not in "abcd":
    CHOOSE = input("Please CHOOSE the conversion unit : \n'a' for bytes to KB\n'b' for bytes to MB\n'c' for bytes to GB\n'd' for bytes to TB\n")
print("Converted file sizes in user chosen unit:")
print("---------------------------------------------------------------------------------------------------------")
print("Directories: ")
print("---------------------------------------------------------------------------------------------------------")
for dirpath, size in size_dir.items():
    print(f"{dirpath}: {converter(size, CHOOSE)}")
print("---------------------------------------------------------------------------------------------------------")
print("Files: ")
print("---------------------------------------------------------------------------------------------------------")
for filepath, size in size_file.items():
    print(f"{filepath}: {converter(size, CHOOSE)}")
