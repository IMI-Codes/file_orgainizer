from os import listdir, chdir, walk
from os.path import isfile, isdir, exists, join, getsize
from shutil import rmtree


class Directory:

    def __init__(self, dir_name: str, dir_path: str) -> None:
        if exists(dir_path) == True:
            self.directory_name = dir_name
            self.directory_path = dir_path
            self.num_of_files = 0
            self.num_of_sub_folders = 0
            self.dir_files = list()
            self.dir_sub_folders = list()
            self.get_dir_contents()

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

    def get_files_in_sub_folders(self):
        # run vscode as admin or run script as admin
        parent_sub_folders = self.dir_sub_folders
        for value in parent_sub_folders:
            if getsize(value) == 0:
                rmtree(value)
            elif getsize(value) != 0:
                print(value)
