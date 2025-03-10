from os import chdir, listdir
from os.path import isdir, isfile
from re import compile
from global_vars_ import file_types


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
    # modify to skip the .ini
    valueType = type(value)
    extension_check = compile(r"\.(\w+)$")
    file_and_ext = dict()
    if valueType == list:
        for f in value:
            ext = extension_check.search(f)
            if ext == None:
                return f"Not a file {value}"  # this will run if it's not a file
            else:
                file_ext = ext.group(1)
                file_name = f
                file_and_ext[file_name] = file_ext
        return file_and_ext
    else:
        ext = extension_check.search(value)  # type: ignore
        if ext == None:
            return f"Not a File, {value}"
        else:

            file_name = value
            file_ext = ext.group(1)
        return {file_name: file_ext}  # type: ignore


def determine_cat(files: dict | str) -> tuple | dict[any, any]:  # type: ignore
    file_name_category = dict()
    determine_type = type(files)
    if determine_type == dict:
        for f in files:
            ext = files[f]  # type: ignore
            for cat in file_types:
                for value in file_types[cat]:
                    # check the extensions with a dictionary of known extensions
                    if value == ext:
                        # return a category for each file name
                        category = cat
                        file_name = f
                        # return a dictionary of file_name and category
                        file_name_category[file_name] = category
        return file_name_category

        # if category can't be decided return a message that the extension type is unknown and should be updated check if the file name is in file_name_category else flag the extension type

    else:
        # for a str
        # check determine the extension type
        # determine category
        # return a tuple of file_name and category
        pass


# Inputs: dictionary or str
# Logic: look at the extension and determine the file type based of a list of existing known extensions


"""  for value in file_types:
        print(file_types[value], value)
        for value in file_types[value]:
            print(value) """
