from os import chdir, getcwd, listdir, mkdir, makedirs
from os.path import isfile, isdir, join
from re import compile, search, I, sub
from variable import Downloads_Dir
from helper import file_patterns
from helper import file_types
from helper import extension_check

video = list()
picture = list()
document = list()
script = list()
music = list()
cat_holder = [video, picture, document, script, music]
contents = Downloads_Dir()
folders = list()
files_details = dict()

for value in contents:
    if isdir(value) == True:
        folders.append(value)
    for pattern in file_patterns:

        search_pattern = pattern.search(value)

        if search_pattern == None:
            continue
        else:
            file_type = search_pattern.group(1)
            fname = value
            files_details[fname] = file_type

# try the logic to catch unknown pattern here
# this catches files that are not there #get the extension type and send a reminder to add save to a file until it is added this to run after the re has gone through
for f in contents:
    if isfile(f) == True and not f in files_details:
        extension = extension_check.search(f)
        if extension_check != None:
            pass


# next step
for file_name in files_details:
    # handle videos
    file_t = files_details[file_name]
    if files_details[file_name] in file_types:
        if file_t in file_types:
            cat = file_types[file_t]
            if cat == "video":
                video.append(file_name)
            elif cat == "picture":
                picture.append(file_name)
            elif cat == "document":
                document.append(file_name)
            elif cat == "script":
                script.append(file_name)
            elif cat == "music":
                music.append(file_name)


# handle files to check if there's videos with no folder

# cross check names in folders
# make a folder for movies,animes,series also pass my watchlist so it can it tell which is whichs
# use ep count and copy or 2 to identify duplicates
# add logic to sort and create folder for each season if more than one
