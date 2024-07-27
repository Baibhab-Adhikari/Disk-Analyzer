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
import zipfile
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
    print("A. Zip Directories / Files\nB. Unzip Files\nC. Analyze Disk Space\nD. Exit")

    menu_choice = input("Please enter A,B,C or D: ")
    while menu_choice.strip().lower() not in "abcd":
        menu_choice = input("Please enter the correct option! : ")

    # check input scenarios
    if menu_choice.lower() == 'a':
        PATH = input(
            "Please enter the path of your desired directory or file to zip: ")
        output_name = input(
            "Enter the name for the output zip file (without extension): ")
        output_directory = input(
            "Enter the directory where you want to save the zip file: ")
        output_path = os.path.join(output_directory, output_name)

        if os.path.isdir(PATH):
            # If PATH is a directory, use shutil.make_archive
            shutil.make_archive(output_path, 'zip', PATH)
        elif os.path.isfile(PATH):
            # If PATH is a file, use zipfile.ZipFile
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(PATH, os.path.basename(PATH))
        else:
            print("The path provided does not exist or is not valid.")

        print(f"Your file / directory is zipped as {output_path}")

    elif menu_choice.lower() == 'b':
        # Prompt user for the zip file path
        zip_path = input("Please enter the path of the zip file to unpack: ")
        # Check if the zip file exists
        if os.path.isfile(zip_path) and zip_path.endswith('.zip'):
            # Ask for the destination directory
            destination = input(
                "Enter the destination directory (leave blank to extract in the current directory): ")
            if not destination:
                # If no destination is provided, extract in the current directory
                destination = os.getcwd()
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(destination)
                print(f"Files have been extracted to {destination}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("The specified path does not point to a zip file.")

    elif menu_choice.lower() == "c":
        # prompt user for the directory path
        PATH = input(
            "Please enter the path of your desired directory to analyze: ")
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
                choose = input(
                    "Please choose the conversion unit : \n'a' for bytes to KB\n'b' for bytes to MB\n'c' for bytes to GB\n'd' for bytes to TB\n")
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
        print("Thankyou for using the Disk Utility Tool!\nExiting the program......")
        program_standby = False
        break
