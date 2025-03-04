from os import mkdir, makedirs
from os.path import isfile, isdir, join
from re import compile, search
from variable import Downloads_Dir
from helper import (
    file_patterns,
    extension_check,
    file_types,
    folders,
    files_details,
    video,
    picture,
    script,
    document,
    music,
)
from shutil import move
from datetime import datetime


timestamp = datetime.now()
print(timestamp)

contents = Downloads_Dir()
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

# handling unknown file extensions
for f in contents:
    if isfile(f) == True and not f in files_details:
        extension_group = extension_check.search(f)
        if extension_group != None:
            extension = extension_group.group(1)
            if extension == "ini":
                continue
            else:
                # save the file extension to a file and name #with date and time
                data = f"file extension : {extension}\nlast_run:{timestamp}\n"
                try:
                    fhand = open("logs.txt", "a")
                    fhand.write(data)
                except:
                    fhand = open("logs.txt", "x")
                    fhand.write(data)
                if "unknown" in folders:
                    # unknown exists
                    # move file to unknown
                    final_path = join(r"C:\Users\rouge\Downloads", f)
                    unknown_dir = r"C:\Users\rouge\Downloads\unknown"
                    move(final_path, unknown_dir)
                    pass  # print(extension, f)
                else:
                    mkdir("unknown")
                    # create new folder called unknown
                    # move file to unknown

        # send a update about the file to update the regex and to check unknown folder
# handle folders that are in the downloads dir
# handle everything in downloads dir before moving to any other dir
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

# videos dir


# handle files to check if there's videos with no folder
# cross check names in folders
# make a folder for movies,animes,series also pass my watchlist so it can it tell which is whichs
# use ep count and copy or 2 to identify duplicates
# add logic to sort and create folder for each season if more than one
# add logs of when last the script ran
