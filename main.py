from os import chdir, getcwd, listdir, mkdir
from os.path import isfile, isdir
from re import compile, search, I, sub

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
pahe_check_pattern = compile(r"^animepahe", I)
anime_name_pattern = compile(r"_(\w+)_-_", I)
dub_check = compile(r"_eng_dub", I)
animes = dict()
for vid in videos:
    pahe_video = pahe_check_pattern.search(vid)
    if pahe_video != None:
        anime = anime_name_pattern.search(vid)
        if anime != None:
            anime_name = anime.group(1)
            # account for dubs too
            anime_name = dub_check.sub(r"", anime_name)  # returns the name without dub
            if anime_name in animes:
                animes[anime_name] += 1
            else:
                animes[anime_name] = 1

print(animes)
# other videos name
# go to videos and return only the folders
videos_dir = r"C:\Users\rouge\Videos"
chdir(videos_dir)

vid_dir_contents = listdir()
# handle files to check if there's videos with no folder
vid_dir_folders = list()
for value in vid_dir_contents:
    if isdir(value) == False:
        continue
    else:
        vid_dir_folders.append(value)

# cross check names in folders
for name in animes:
    if name not in vid_dir_folders:
        dir_name = name
        mkdir(dir_name)
        # create a new directory and add the anime to that folder
    else:
        pass  # add the anime to that folder


# use ep count and copy or 2 to identify duplicates
