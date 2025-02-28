from os import chdir, getcwd, listdir
from os.path import isfile
from re import compile, search, I

downloads_dir = r"C:\Users\rouge\Downloads"
# change to  Downloads
chdir(downloads_dir)
# get a list of all files and folders
dir_contents = listdir()
# filter out and return only the videos
video_pattern = compile(r"\.(mkv|mp4|webm)$")

videos = list()
for item in dir_contents:
    if isfile(item) == True:
        video = video_pattern.search(item)
        if video != None:
            videos.append(item)

# get names of the videos

# go to videos and return only the folders
