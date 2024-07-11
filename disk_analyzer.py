"""
Author : Baibhab Adhikari
Github : https://github.com/Baibhab-Adhikari

A script for a disk utility tool

This script traverses a given directory, calculates the size of each file and directory,
and converts these sizes to a user-specified unit (KB, MB, GB, or TB).
"""
# imports
import os
import shutil
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
    print("A. Zip Files\nB. Unzip Files\nC. Analyze Disk Space\nD. Exit")

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
                output_name = input("Enter the name for the output zip file: ")  # Dynamic output name
                output_path = os.path.join(PATH, output_name)
                shutil.make_archive(output_path, "zip", PATH)
                print(f"Your file / directory is zipped as {output_path}.zip")
            except Exception as e:
                print(f"An error occurred: {e}")
            
    elif menu_choice.lower() == 'b': 
        # prompt user for the directory path
        zip_file_path = input("Please enter the path of your desired directory to unzip: ")
        # check for existence
        if os.path.exists(zip_file_path):
            # if path exist then unzip
            try:
                output_name = input("Enter the name for the output zip file: ")  # Dynamic output name
                output_path = os.path.join(zip_file_path, output_name)
                shutil.unpack_archive(zip_file_path, output_path, "zip")
                print(f"Your file / directory is unzipped as {output_path}")
            except Exception as e:
                print(f"An error occurred: {e}")

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