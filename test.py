from Directory import Directory
from File import File

download_dir = Directory("downloads", r"C:\Users\rouge\Downloads")
document_dir = Directory("documents", r"C:\Users\rouge\OneDrive\Documents")
desktop_dir = Directory("desktop", r"C:\Users\rouge\OneDrive\Desktop")


dir_fs = download_dir.get_dir_files()
for value in dir_fs:  # type: ignore
    print(File(value))
