from os.path import basename, exists
from re import compile, search
from mimetypes import guess_type


class File:
    # create custom extension types for unknowns
    # modify so we update a text file to add new data

    def __init__(self, f_name_path: str) -> None:
        if exists(f_name_path) == True:
            self.f_name_full_path = f_name_path
            self.f_name = basename(f_name_path)
            self.file_type = None
            self.extension = None
            self.exact_file_type = None
            self.determine_file_type()
            self.get_extension()
            if self.file_type is not None:
                self.determine_exact_type()
            else:
                return None
        else:
            return None

    def get_file_name(self):
        return self.f_name

    def get_file_path(self):
        return self.f_name_full_path

    def determine_file_type(self):
        file_name = self.f_name
        file_type, secondary_name = guess_type(file_name)
        if file_type != None and len(file_type) != 0:
            self.file_type = file_type
        else:
            return None

    def get_extension(self):
        extension_pattern = compile(r"(\.)(\w+)$")
        mat = extension_pattern.search(self.f_name)
        if mat is not None:
            dot, extension = mat.groups()
            self.extension = extension
        else:
            return None

    def determine_exact_type(self):
        if self.file_type is not None:
            general_type = self.file_type
            general, exact_type = general_type.split("/")
            self.exact_file_type = exact_type
        else:
            return None

    def set_file_data(self):
        pass
