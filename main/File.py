from os.path import basename
from re import compile, search
from mimetypes import guess_type


class File:

    def __init__(self, f_name_path: str) -> None:
        self.f_name_full_path = f_name_path
        self.f_name = basename(f_name_path)
        self.file_type = None
        self.extension = None
        self.determine_file_type()
        self.get_extension()
        if self.file_type is not None:
            self.determine_exact_type()

    def determine_file_type(self):
        file_name = self.f_name
        file_type, secondary_name = guess_type(file_name)
        if file_type != None and len(file_type) != 0:
            self.file_type = file_type
        else:
            return None

    def get_extension(self):
        pass

    def determine_exact_type(self):
        pass
