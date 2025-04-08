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

    """ def get_files_in_sub_folders(self):
        # run vscode as admin or run script as admin
        sub_dir_files = list()
        parent_sub_folders = self.dir_sub_folders
        for value in parent_sub_folders:
            if getsize(value) == 0:
                try:
                    rmtree(value)
                except:
                    send2trash(value)
            elif getsize(value) != 0:
                for folders, subfolders, filenames in walk(value):
                    if len(filenames) == 0:
                        continue  # print(folders, filenames)
                    elif len(filenames) == 1:
                        return join(folders, filenames[0])
                    elif len(filenames) > 1:
                        for value in filenames:
                            file_path = join(folders, value)
                            sub_dir_files.append(file_path)
        return sub_dir_files """
