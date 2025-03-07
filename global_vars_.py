from re import compile, I

video_pattern = compile(r"\.(mkv|mp4|webm)$")
picture_pattern = compile(r"\.(jpg|png|svg)$")
documents_pattern = compile(r"\.(pdf|txt|pptx|docx|pem)$")
scripts_install_pattern = compile(r"\.(exe|py|ps1|bat)$")
sounds_pattern = compile(r"\.(mp3)$")

extension_check = compile(r"\.(\w+)$")


file_patterns = [
    video_pattern,
    picture_pattern,
    documents_pattern,
    scripts_install_pattern,
    sounds_pattern,
]

file_types = {
    "video": ["mkv", "mp4", "webm"],
    "picture": ["jpg", "png", "svg"],
    "document": ["pdf", "txt", "pptx", "docx", "pem"],
    "script": ["exe", "py", "ps1", "bat"],
    "music": ["mp3"],
}


""" 
file_types = {
    "mkv": "video",
    "mp4": "video",
    "webm": "video",
    "jpg": "picture",
    "png": "picture",
    "pdf": "document",
    "txt": "document",
    "pptx": "document",
    "docx": "document",
    "svg": "picture",
    "exe": "script",
    "py": "script",
    "ps1": "script",
    "bat": "script",
    "mp3": "music",
    "pem": "document",
} """
fz_pattern = compile(r"(\w+)_-_(\w+)_")
pahe_check_pattern = compile(r"^animepahe_(\w+)_-_", I)
# anime_name_pa ttern = compile(r"_(\w+)_-_", I)
dub_check = compile(r"_eng_dub", I)


video = list()
picture = list()
document = list()
script = list()
music = list()
cat_holder = [video, picture, document, script, music]

folders = list()
files_details = dict()
