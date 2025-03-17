from os import chdir, listdir, walk
from os.path import isdir, isfile, join
from re import compile
from global_vars_ import file_types


# VERIFIED FUNCTIONS
def change_dir(path: str):
    chdir(path)
    dir_contents = listdir()
    return dir_contents


# ||||||||||||||||| FUNCTIONS TO BE MODIFIED ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


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


def get_files_from_folders(folders: list, dir_path: str):
    files_paths = list()
    for f in folders:
        for folders, subfolders, filenames in walk(f):
            for filename in filenames:
                base_path = join(folders, filename)  # type: ignore
                final_path = join(dir_path, base_path)
                files_paths.append(final_path)
    return files_paths


def sort_files():
    pass


def get_extension_file_name(
    value: list | str,
):  # -> str | dict[Any, Any] | tuple[list[Any] | str, Any]:
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
        return file_name, file_ext


def determine_cat(files: dict | str):

    file_name_category = dict()
    unknown_exts = dict()
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
            if f not in file_name_category:
                unknown_exts[f] = ext
        if len(unknown_exts) != 0:
            return file_name_category, unknown_exts
        else:
            return file_name_category
        # if category can't be decided return a message that the extension type is unknown and should be updated check if the file name is in file_name_category else flag the extension type

    else:
        # for a str
        file_name, ext = file_type(files)  # type: ignore
        category = None

        for value in file_types:
            for e in file_types[value]:
                if e == ext:
                    # determine category
                    category = value
                    # return a tuple of file_name and category
                    return file_name, category
        if category == None:
            return f"Unknown Extension Type {ext}, {file_name}"
