from os import mkdir, chdir, getcwd, walk, listdir, makedirs
from os.path import isfile, isdir, join, getsize, exists
from re import compile, search
from helper_funcs import (
    dir_file_and_folders,
    change_dir,
    get_extension_file_name,
    determine_cat,
    get_files_from_folders,
)
from global_vars_ import *
from shutil import move
from datetime import datetime

timestamp = datetime.now()
downloads_path = r"C:\Users\rouge\Downloads"
contents = change_dir(downloads_path)
documents_path = r"C:\Users\rouge\OneDrive\Documents"
logs_path = join(documents_path, r"CustomSystemLogs\file_organizer_logs")


# STARTING FROM THE DOWNLOADS DIRECTORY


# CONTENTS OF THE DOWNLOADS DIRECTORY


folders, files = dir_file_and_folders(contents)
# MANUALLY DELETE UNKNOWN AND STAGING
# WALKING THROUGH FOLDERS AND RETURNING THE FILES WITHIN THE FOLDERS

get_files_from_folders(folders, downloads_path)
""" 


# create logic for walking through the folders and return the file paths for any files

# returning the file_name and file_extensions
f_types = get_extension_file_name(files)


# returning known and unknown file types
file_cats, unknown = determine_cat(f_types)  # type: ignore
if "desktop.ini" in unknown:
    del unknown["desktop.ini"]  # type: ignore
# handling unknown file types
# check if the path to the logs folders exist
# save whenever the script runs and changes made account for the desktop.ini save to a file flag unknowns and move them to the unknown folder
check_path = exists(logs_path)
log_file = join(logs_path, r"logs.txt")

print(logs_path)
if check_path == False:
    makedirs(logs_path, exist_ok=True)
else:
    print("already exists")

# handling the folder in each dir
# this get the file_path for every file in every folder in downloads
folder_files = get_files_from_folders(folders, downloads_path)
 """
