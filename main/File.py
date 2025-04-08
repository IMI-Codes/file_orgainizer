from os.path import basename
from re import compile, search
from mimetypes import guess_type


class File:

    def __init__(self, f_name_path: str) -> None:
        self.f_name_full_path = f_name_path
        self.f_name_ext = basename(f_name_path)
        self.file_type = None
        self.determine_file_type()

    def determine_file_type(self):
        pass
