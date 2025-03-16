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
folders.remove("holder")
holder_dir_path = join(downloads_path, "holder")

folders.remove("staging")
staging_dir_path = join(downloads_path, "staging")


# WALKING THROUGH FOLDERS AND RETURNING THE FILES WITHIN THE FOLDERS
# ALL FILES IN ANY OTHER FOLDER IN THE DOWNLOADS DIR
get_files_from_folders(folders, downloads_path)
