from os import chdir, listdir, walk
from os.path import isdir, isfile, join
from re import compile
from others.global_vars_ import file_types


# VERIFIED FUNCTIONS
def change_dir(path: str):
    chdir(path)
    dir_contents = listdir()
    return dir_contents


def dir_file_and_folders(dir_contents: list, base_path: str):
    folders = list()
    files = list()
    for item in dir_contents:
        isFolder = isdir(item)
        isFiletype = isfile(item)
        if isFolder == True:
            folder_path = join(base_path, item)
            folders.append(folder_path)
        if isFiletype == True:
            file_path = join(base_path, item)
            files.append(file_path)
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
    determine_collection = type(files)
    unknown_types = dict()
    file_name_cat = dict()
    if determine_collection == dict:
        for f in files:
            ext = files[f]  # type: ignore
            if ext in file_types:
                file_name_cat[f] = file_types[ext]
            else:
                unknown_types[f] = ext
    else:
        f, f_ext = get_extension_file_name(files)  # type: ignore
        if f_ext in file_types:
            return f, file_types[f_ext]
        else:
            return {
                "Message": "Unknown File Type",
                "file_name": f,
                "file_extension": f_ext,
            }
    if file_name_cat and unknown_types:

        return file_name_cat, unknown_types
    elif file_name_cat:
        return file_name_cat
    elif unknown_types:
        return unknown_types
