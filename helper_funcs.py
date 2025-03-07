from os import chdir, listdir
from os.path import isdir, isfile


def change_dir(path: str):
    chdir(path)
    dir_contents = listdir()
    return dir_contents


def dir_file_and_folders(dir_contents: list):
    folders = list()
    files = list()
    for item in dir_contents:
        isFolder = isdir(item)
        isFiletype = isfile(item)
        if isFolder and isFolder == True:
            folders.append(item)
        elif isFiletype and isFiletype == True:
            files.append(item)
    return folders, files


def file_type(value: list | str):
    valueType = type(value)
    if valueType == list:
        for f in value:
            pass
    else:
        pass
