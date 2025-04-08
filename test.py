from mimetypes import guess_file_type, guess_type


videos = ["test.mkv", "test.mp4", "test.webm", "test.avi", "test.mov", "test.flv"]
picture = [
    "test.jpg",
    "test.png",
    "test.svg",
    "test.jpeg",
    "test.gif",
    "test.bmp",
    "test.tif",
    "test.tiff",
    "test.webp",
]
document = [
    "test.pdf",
    "test.txt",
    "test.pptx",
    "test.docx",
    "test.pem",
    "test.docx",
    "test.xls",
    "test.xlsx",
    "test.ppt",
    "test.rtf",
    "test.odt",
    "test.ods",
    "test.odp",
    "test.md",
    "test.csv",
    "test.json",
    "test.xml",
]
scripts = [
    "test.exe",
    "test.app",
    "test.apk",
    "test.ipa",
    "test.jar",
    "test.py",
    "test.sh",
    "test.bat",
]
sound = [
    "test.mp3",
    "test.wav",
    "test.aac",
    "test.ogg",
    "test.flac",
    "test.m4a",
    "test.wma",
]


for vid in videos:
    print(guess_file_type(vid), vid, 1)
    print(guess_type(vid), vid, 2)
