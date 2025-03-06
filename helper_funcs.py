from os import chdir, listdir


def Downloads_Dir():
    downloads_dir = r"C:\Users\rouge\Downloads"
    chdir(downloads_dir)
    dir_contents = listdir()
    return dir_contents


def Videos_Dir():
    videos_dir = r"C:\Users\rouge\Videos"
    chdir(videos_dir)
    dir_contents = listdir()
    return dir_contents


def file_extension_parse(file_name):
    # list of patterns
    # list of categories

    # loop through list of pattern and cats

    pass
