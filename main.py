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

# handle everything in downloads dir before moving to any other dir
timestamp = datetime.now()
downloads_path = r"C:\Users\rouge\Downloads"
contents = change_dir(downloads_path)

documents_path = r"C:\Users\rouge\OneDrive\Documents"
logs_path = join(documents_path, r"CustomSystemLogs\file_organizer_logs")

# sorting folders and files
folders, files = dir_file_and_folders(contents)

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
if check_path == False:
    pass  # makedirs(logs_path) get this to work
else:
    fhand = open(log_file, "a")

# handling the folder in each dir
get_files_from_folders(folders)

# handling the folder in download better still logic for handling folder and their content in each directory(videos dir documents dir pictures dir)
# make a folder for movies,animes,series also pass my watchlist so it can it tell which is whichs
# use ep count and copy or 2 to identify duplicates and deleting them
# add logic to sort and create folder for each season if more than one
# add logs of when last the script ran for each run and the changes made
# send a update about the file to update the regex and to check unknown folder
# handle
# that are in the downloads dir

# decouple the pattern searching into a function that is all the search for file extension should be done by a function
