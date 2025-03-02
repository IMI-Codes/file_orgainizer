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
music = list

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
        print(file_t)
# account for file types that are not in the re
# if isfile is true but not pattern claim it get the file type with .?
""" videos = list()
for item in dir_contents:
    if isfile(item) == True:
        video = video_pattern.search(item)
        if video != None:
            videos.append(item)

print(videos)

# patterns


animes = dict()


for vid in videos:
    pahe_video = pahe_check_pattern.search(vid)
    fz_video = fz_pattern.search(vid)
    if pahe_video != None:
        anime = pahe_check_pattern.search(vid)
        if anime != None:
            anime_name = anime.group(1)
            anime_name = dub_check.sub(r"", anime_name)  # returns the name without dub
            if anime_name in animes:
                animes[anime_name] += 1
            else:
                animes[anime_name] = 1
    elif fz_video != None:
        print(fz_video)


print(animes)
# other videos name
# go to videos and return only the folders

# handle files to check if there's videos with no folder
vid_dir_folders = list()
for value in vid_dir_contents:
    if isdir(value) == False:
        continue
    else:
        vid_dir_folders.append(value)

# cross check names in folders
# make a folder for movies,animes,series also pass my watchlist so it can it tell which is which
for name in animes:
    if name not in vid_dir_folders:
        name = str(name)
        mkdir(name)
        # create a new directory and add the anime to that folder
    else:
        pass  # add the anime to that folder get file name and pass move here


# use ep count and copy or 2 to identify duplicates
# add logic to sort and create folder for each season if more than one
 """
