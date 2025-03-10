from os import mkdir, chdir, getcwd, walk, listdir
from os.path import isfile, isdir, join, getsize, exists
from re import compile, search
from helper_funcs import dir_file_and_folders, change_dir, file_type, determine_cat
from global_vars_ import *
from shutil import move
from datetime import datetime

# handle everything in downloads dir before moving to any other dir
timestamp = datetime.now()
downloads_path = r"C:\Users\rouge\Downloads"
contents = change_dir(downloads_path)

# sorting folders and files
folders, files = dir_file_and_folders(contents)

# returning the file_name and file_extensions
print(files)
f_types = file_type(files)

print(determine_cat(f_types))
# save whenever the script runs and changes made account for the desktop.ini save to a file flag unknowns and move them to the unknown folder
# handling the folder in download better still logic for handling folder and their content in each directory(videos dir documents dir pictures dir)
# make a folder for movies,animes,series also pass my watchlist so it can it tell which is whichs
# use ep count and copy or 2 to identify duplicates and deleting them
# add logic to sort and create folder for each season if more than one
# add logs of when last the script ran for each run and the changes made
# send a update about the file to update the regex and to check unknown folder
# handle
# that are in the downloads dir

# decouple the pattern searching into a function that is all the search for file extension should be done by a function
