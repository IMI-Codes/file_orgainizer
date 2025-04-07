from os.path import basename
from re import compile, search


class File:

    def __init__(self, f_name_path: str) -> None:
        self.f_name_full_path = f_name_path
        self.f_name_ext = basename(f_name_path)
