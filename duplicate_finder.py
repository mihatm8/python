"""
This script looks trhough a directory structure and lists file names that are duplicates.
This is done by using the walk method, setdefault method to store the number of occurences - and then the program is rerun to create another dictionary that contains the file name as the key and the value being a list of paths of the duplicate files.
"""

import os

def find_duplicate_files(directory):
    file_list = {}
    results = {}
    
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print(f"Error: The specified directory '{directory}' does not exist.")
        return
    
    for folder, subfolder, files in os.walk('./'):
        for file in files:
            file_list.setdefault(file, 0)
            file_list[file] += 1
            
    for filename, count in file_list.items():
        paths = []
        if count > 1:
            for folder, subfolder, files in os.walk('./'):
                for file in files:
                    if filename == file:
                        paths.append(folder)
            results[filename] = paths
            
    if not results:
        print("No duplicate files found.")
    else:
        for filename, paths in results.items():
            print(filename)
            for path in paths:
                print(path)
            print("\n-----\n")

if __name__ == "__main__":
    directory = input("Enter the directory path to search for duplicate files: ")
    find_duplicate_files(directory)

