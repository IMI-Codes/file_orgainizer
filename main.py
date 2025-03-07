from os import mkdir, chdir, getcwd, walk, listdir
from os.path import isfile, isdir, join, getsize, exists
from re import compile, search
from helper_funcs import dir_file_and_folders, change_dir
from global_vars_ import *
from shutil import move
from datetime import datetime


timestamp = datetime.now()
downloads_path = r"C:\Users\rouge\Downloads"
contents = change_dir(downloads_path)

# sorting folders and files
folders, files = dir_file_and_folders(contents)

""" 

    for pattern in file_patterns:
        search_pattern = pattern.search(value)
        if search_pattern == None:
            continue
        else:
            file_type = search_pattern.group(1)
            fname = value
            files_details[fname] = file_type
 """

# return to this


# try the logic to catch unknown pattern here
# this catches files that are not there #get the extension type and send a reminder to add save to a file until it is added this to run after the re has gone through

# handling unknown file extensions
""" for f in contents:
    if isfile(f) == True and not f in files_details:
        extension_group = extension_check.search(f)
        if extension_group != None:
            extension = extension_group.group(1)
            if extension == "ini":
                continue
            else:
                # save the file extension to a file and name #with date and time
                data = f"file extension : {extension}\nlast_run: {timestamp}\n"
                # desktop = chdir(r"C:/Users/rouge/OneDrive/Desktop")
                fhand_path = r"C:/Users/rouge/OneDrive/Desktop/log.txt"
                try:
                    fhand = open(fhand_path, "a")
                    fhand.write(data)
                except:

                    fhand = open(fhand_path, "x")
                    fhand.write(data)
                if "unknown" not in folders:
                    # unknown exists
                    # move file to unknown
                    mkdir("unknown")
                else:
                    final_path = join(r"C:.Users.rouge.Downloads", f)
                    unknown_dir = r"C:.Users.rouge.Downloads.unknown"
                    move(final_path, unknown_dir)
                    # create new folder called unknown
                    # move file to unknown


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


# downloads dir
# handling any folder in the downloads dir
# folders and subfolder should be saved to file that is the file structure should be saved the main thing we're after is the files
files_to_holder = dict()
for folder in folders:
    if folder == "unknown":
        continue
    else:
        base_path = join(r"C:/Users/rouge/Downloads", folder)
        for foldernName, subfolders, fileNames in walk(base_path):

            for subfolder in subfolders:

                for fileName in fileNames:
                    # get the file and file_path
                    # modify to account for empty directories and merge with the moving logic to move and then delete the directory
                    folder_path = foldernName
                    file_name = fileName
                    file_name_path = join(folder_path, file_name)
                    files_to_holder[file_name] = file_name_path

# print(files_to_holder)
# move files to a directory called staging
if "staging" in folders:
    for file_name in files_to_holder:
        move(files_to_holder[file_name], r"C:/Users/rouge/Downloads/staging")
else:
    mkdir("staging")

# handling files in staging
chdir(r"C:/Users/rouge/Downloads/staging")
staging_contents = listdir()

for content in staging_contents:

    content_ext_check = extension_check.search(content)
    if content_ext_check == None:
        continue
    else:
        content_ext = content_ext_check.group(1)
        content_file_name = content
        files_details[content_file_name] = content_ext


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


for cat in cat_holder:
    if len(cat) == 0:
        continue
    else:
        print(cat, "\n\n") """

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
