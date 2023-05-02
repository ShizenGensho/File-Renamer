
import os
import sys
import shutil
import logging

# Setup logging
logging.basicConfig(filename='renamer.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def rename_files():
    # Get the directory path and the old and new strings
    dir_path = input("Enter the directory path: ")
    old_str = input("Enter the string to replace: ")
    new_str = input("Enter the replacement string: ")

    logging.info(f"Renaming files in directory {dir_path} from '{old_str}' to '{new_str}'")

    # Iterate over the files in the directory
    for filename in os.listdir(dir_path):
        # Check if the old string is in the filename
        if old_str in filename:
            # Replace the old string with the new string
            new_filename = filename.replace(old_str, new_str)
            old_path = os.path.join(dir_path, filename)
            new_path = os.path.join(dir_path, new_filename)
            # Rename the file
            os.rename(old_path, new_path)
            logging.info(f"Renamed file {filename} to {new_filename}")

    print("Done")

# Run the program
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    rename_files()
    run_again = input("Do you want to rename more files? (y/n) ")
    if run_again.lower() != "y":
        break

logging.info("Program exited")
