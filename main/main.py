from Directory import Directory
from File import File


dir_1 = Directory("downloads_dir", r"C:\Users\rouge\Downloads")
dir_2 = Directory("documents_dir", r"C:\Users\rouge\OneDrive\Documents")


dir_1.get_sub_files()

# dir_2.get_sub_files()
