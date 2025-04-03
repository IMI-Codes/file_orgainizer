from Directory import Directory
from os.path import exists

download_dir = Directory("downloads", r"C:\Users\rouge\Downloads")
document_dir = Directory("documents", r"C:\Users\rouge\OneDrive\Documents")

print(document_dir.get_files_in_sub_folders())
