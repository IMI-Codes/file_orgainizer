from os import chdir, getcwd, listdir, mkdir
from os.path import exists, isdir, join
from shutil import move
from re import compile, search, I


dir_name = r"C:\Users\rouge\Downloads"
pahe_pattern = compile(
    r"^(animepahe)_(\w+)_-_(\d{1,4})_(\d{3,4}p)", I
)  # modify for anime with season numbers
# pattern for all anime
# account for eps with eng_dub and remove it
holder = dict()
if dir_name:
    valid_dir = exists(dir_name)
    if valid_dir == True:
        chdir(dir_name)
else:
    raise Exception
current_dir = getcwd()

# check for all files and folders in the directory
directory_content = listdir(current_dir)
for value in directory_content:
    data = pahe_pattern.search(value)
    # print(data)
    if data != None:
        anime_name = data.group(2)
        anime_name_ep = f"{data.group(2)} {data.group(3)}"
        print(anime_name_ep)
        if anime_name in holder:
            holder[anime_name] += 1
        else:
            holder[anime_name] = 1

chdir(r"C:\Users\rouge\Videos")
directories_and_files = listdir()
base_path = getcwd()
for value in holder:
    if value in directories_and_files and isdir(value) == True:
        del holder[value]  # this means there is a
        # add episode to folder and or return folder name
    else:
        f_path = join(base_path, value)
        mkdir(f_path)

# also check if there are episode here too

# check for any videos with similar names but increasing counts

# checks all folder for content


# save when last it run to a file  and when last the file was updated
