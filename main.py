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


# ||||||||||||| DOWNLOADS DIRECTORY |||||||||||||||
unknown_dir_path = join(downloads_path, "unknown")
staging_dir_path = join(downloads_path, "staging")

# CONTENTS OF THE DOWNLOADS DIRECTORY

folders, files = dir_file_and_folders(contents, downloads_path)

# MANUALLY DELETE UNKNOWN AND STAGING

if unknown_dir_path and staging_dir_path in folders:
    folders.remove(unknown_dir_path)
    folders.remove(staging_dir_path)

# GETTING ALL FILES IN THE SUBFOLDER AND MERGING ALL FILES TOGETHER
all_files = get_files_from_folders(folders, downloads_path) + files

file_name_and_extension = get_extension_file_name(all_files)


determine_cat(file_name_and_extension)  # type: ignore
