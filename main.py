from os import chdir, getcwd, listdir
from os.path import exists


dirs = [
    r"C:\Users\rouge\Videos",
    r"C:\Users\rouge\OneDrive\Documents",
    r"C:\Users\rouge\Downloads",
]
dir_name = r"C:\Users\rouge\Downloads"
if dir_name:
    valid_dir = exists(dir_name)
    if valid_dir == True:
        chdir(dir_name)
else:
    raise Exception
current_dir = getcwd()
print(listdir(current_dir))
# check for files anime

# check for folders and content


# save when last it run to a file  and when last the file was updated
