<<<<<<< Updated upstream
from os import mkdir, chdir, getcwd, walk, listdir, makedirs
from os.path import isfile, isdir, join, getsize, exists
=======
from os import mkdir, chdir, walk, listdir
from os.path import isfile, isdir, join
>>>>>>> Stashed changes
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
documents_path = r"C:\Users\rouge\OneDrive\Documents"
logs_path = join(documents_path, r"CustomSystemLogs")

str_time_stamp = str(timestamp).split()
c_date, c_time = str_time_stamp
new_c_time = c_time.replace(":", "-").replace(".", "-")

# |||||||||||| CREATING A LOG FILE FOR EACH TIME THE CODE RUNS |||||||||||||||||||||||








# Create a log file immediately the code starts to run
# check if the dir is there
# create a custom log for that date and time


# |||||||||||||| VARIABLES ||||||||||||||||
downloads_path = r"C:\Users\rouge\Downloads"
contents = change_dir(downloads_path)


# r"CustomSystemLogs/file_organizer_logs"


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


sorted_files = determine_cat(file_name_and_extension)  # type: ignore

if type(sorted_files) == tuple:
    sorted_files_cat, unknown_f_types = sorted_files
elif type(sorted_files) == dict:
    if "Message" in sorted_files:
        unknown_f_types = sorted_files
    else:
        sorted_files_cat = sorted_files

if unknown_f_types:  # type: ignore
    for f in unknown_f_types:
        pass
        # move(f, unknown_dir_path)  # type: ignore

# move the files to the there respective directories
# move the unknown to the unknown dir
# move all the known to the staging dir
# Update the logs files
# 1. Unknown files
# 2. Files moved and to which directory


# clean up downloads directory

<<<<<<< Updated upstream
# VIDEOS DIRECTORY
=======

for cat in cat_holder:
    if len(cat) == 0:
        continue
    else:
        print(cat, "\n\n")

# videos dir
# documents dir
# pictures dir
# handle files to check if there's videos with no folder
# cross check names in folders
# make a folder for movies,animes,series also pass my watchlist so it can it tell which is whichs
# use ep count and copy or 2 to identify duplicates
# add logic to sort and create folder for each season if more than one
# add logs of when last the script ran for each run and the changes made
# send a update about the file to update the regex and to check unknown folder
# handle
# that are in the downloads dir
# handle everything in downloads dir before moving to any other dir
# decouple the pattern searching into a function that is all the search for file extension should be done by a function
>>>>>>> Stashed changes
