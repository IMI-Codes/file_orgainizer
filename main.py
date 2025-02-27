from os import chdir, getcwd, listdir, mkdir
from os.path import exists
from shutil import move
from re import compile, search, I


dir_name = r"C:\Users\rouge\Downloads"
pahe_pattern = compile(r"^(animepahe)_(\w+)_-_(\d{1,4})_(\d{3,4}p)", I)

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


# checks all folder for content


# save when last it run to a file  and when last the file was updated
