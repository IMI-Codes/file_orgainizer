from os import listdir, chdir, walk
from os.path import isfile, isdir, exists, join, getsize
from shutil import rmtree, move

from send2trash import send2trash


class Directory:

    def __init__(self, dir_name: str, dir_path: str) -> None:
        # get dirname for file path
        if exists(dir_path) == True:
            self.directory_name = dir_name
            self.directory_path = dir_path
            self.num_of_files = 0
            self.num_of_sub_folders = 0
            self.dir_files = list()
            self.dir_sub_folders = list()
            self.get_dir_contents()
        else:
            raise Exception

    def get_dir_name(self):
        return self.directory_name

    def get_dir_path(self):
        return self.directory_path

    def get_num_of_files(self):
        return self.num_of_files

    def get_num_of_sub_folder(self):
        return self.num_of_sub_folders

    def get_dir_files(self):
        if len(self.dir_files) != 0:
            return self.dir_files
        else:
            return None

    def get_dir_sub_folders(self):
        if len(self.dir_sub_folders) != 0:
            return self.dir_sub_folders
        else:
            return None

    def get_dir_contents(self):
        dir_path = self.directory_path
        chdir(dir_path)
        dir_content = listdir()
        for value in dir_content:
            value = join(self.directory_path, value)
            if isfile(value) == True:
                self.num_of_files += 1
                self.dir_files.append(value)
            elif isdir(value) == True:
                self.num_of_sub_folders += 1
                self.dir_sub_folders.append(value)
        return

    def move_file(self, source, destination):
        move(source, destination)

    def get_sub_files(self):
        sub_files = list()
        sub_folders = self.dir_sub_folders
        for f in sub_folders:
            for base_path, sub_f, files in walk(f):
                if len(files) == 0:
                    continue
                else:
                    """if len(files) != 1
                    print(val1, val2, val3)
                    print(exists(join(val1, val3[0])))
                    """
