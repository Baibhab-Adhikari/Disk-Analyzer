"""
Disk Analyzer Documentation
===========================

Author: Baibhab Adhikari
GitHub: https://github.com/Baibhab-Adhikari

Overview
--------
A disk utility tool script designed to traverse a given directory, calculate the size of each file and directory within it, and convert these sizes into a user-specified unit (KB, MB, GB, or TB).

Dependencies
------------
- Python 3.x
- os module: For interacting with the operating system, particularly for directory traversal and file size calculation.
- shutil module: Used for zipping and unzipping of files

Features
--------
- Directory Traversal: Efficiently navigates through a specified directory, including all subdirectories, to gather information about file and directory sizes.
- Size Calculation: Accurately calculates the size of files and directories in bytes.
- Unit Conversion: Offers the ability to convert the calculated sizes from bytes to a more readable format specified by the user (KB, MB, GB, or TB).

Constants
---------
- `BYTES_PER_UNIT` (int): A global constant set to 1024, representing the number of bytes in a kilobyte (KB), used as the base for conversion to other units.

"""
# imports
import os
import shutil
# global const
BYTES_PER_UNIT = 1024  

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
    elif choice == 'b':
        return f"{size_bytes / (BYTES_PER_UNIT ** 2):.3f} MB"
    elif choice == 'c':
        return f"{size_bytes / (BYTES_PER_UNIT ** 3):.3f} GB"
    elif choice == 'd':
        return f"{size_bytes / (BYTES_PER_UNIT ** 4):.3f} TB"
    else:
        return f"{size_bytes} Bytes"

# main menu design
program_standby = True  # bool flag
# printing menu options
while program_standby:
    
    print("Welcome to Disk Utility! What do you want to perform?")
    print("A. Zip Directories\nB. Unzip Directories\nC. Analyze Disk Space\nD. Exit")

    menu_choice = input("Please enter A,B,C or D: ")
    while menu_choice.strip().lower() not in "abcd":
        menu_choice = input("Please enter the correct option! : ")
    
    # check input scenarios
    if menu_choice.lower() == 'a': 
        # prompt user for the directory path
        PATH = input("Please enter the path of your desired directory to zip: ")
        # check for existence
        if os.path.exists(PATH):
            # if path exist then zip
            try:
                output_name = input("Enter the name for the output zip file (without extension): ")  # Dynamic output name
                output_directory = input("Enter the directory where you want to save the zip file: ")  # Ask for output directory
                output_path = os.path.join(output_directory, output_name)
                shutil.make_archive(output_path, "zip", PATH)
                print(f"Your directory is zipped as {output_path}.zip")
            except Exception as e:
                print(f"An error occurred: {e}")
            
    elif menu_choice.lower() == 'b':
        # Prompt user for the path of the zip file
        zip_file_path = input("Please enter the path of your desired zip file to unzip: ")
        # Check for existence
        if os.path.exists(zip_file_path):
            # If path exists then unzip
            try:
                output_directory = input("Enter the directory where you want to unzip the files: ")  # Ask for output directory
                shutil.unpack_archive(zip_file_path, output_directory, "zip")
                print(f"Your directory is unzipped in {output_directory}")
            except shutil.ReadError:
                print("The archive is corrupted or the format is not supported.")
            except FileNotFoundError:
                print("The specified file or directory was not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("The specified zip file does not exist.")

    elif menu_choice.lower() == "c":
        # prompt user for the directory path
        PATH = input("Please enter the path of your desired directory to analyze: ")
        # check for existence
        if os.path.exists(PATH):

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
    elif menu_choice.lower() == "d":
        print("Exiting the program......")
        program_standby = False
        break