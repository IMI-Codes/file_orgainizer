from re import compile, I

video_pattern = compile(r"\.(mkv|mp4|webm)$")
picture_pattern = compile(r"\.(jpg|png)")
documents_pattern = compile(r"\.(pdf|txt|pptx|docx|svg)")
scripts_install_pattern = compile(r"\.(exe|py|ps1|bat)")
sounds_pattern = compile(r"\.(mp3)")

file_patterns = [
    video_pattern,
    picture_pattern,
    documents_pattern,
    scripts_install_pattern,
    sounds_pattern,
]

fz_pattern = compile(r"(\w+)_-_(\w+)_")
pahe_check_pattern = compile(r"^animepahe_(\w+)_-_", I)
# anime_name_pattern = compile(r"_(\w+)_-_", I)
dub_check = compile(r"_eng_dub", I)
