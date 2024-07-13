# Disk Analyzer Documentation

## Overview
A disk utility tool script designed to traverse a given directory, calculate the size of each file and directory within it, and convert these sizes into a user-specified unit (KB, MB, GB, or TB).

## Dependencies
- **Python 3.x**: The core programming language used.
- **os module**: For interacting with the operating system, particularly for directory traversal and file size calculation.
- **shutil module**: Used for zipping and unzipping of files.

## Features
- **Directory Traversal**: Efficiently navigates through a specified directory, including all subdirectories, to gather information about file and directory sizes.
- **Size Calculation**: Accurately calculates the size of files and directories in bytes.
- **Unit Conversion**: Offers the ability to convert the calculated sizes from bytes to a more readable format specified by the user (KB, MB, GB, or TB).

## Constants
- `BYTES_PER_UNIT` (int): A global constant set to 1024, representing the number of bytes in a kilobyte (KB), used as the base for conversion to other units.

## Usage
This tool is designed to be executed from the command line. Users will be prompted to enter the path of the directory they wish to analyze or the file they wish to compress/decompress. Following the prompts, the tool will perform the requested operation and display the results or status to the user.

Note: This tool does not require any prior installation of external Python packages beyond the standard library.
