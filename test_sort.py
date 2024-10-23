from sort import Sort_Files
from pathlib import Path
import json

downloads_dir = Sort_Files('Downloads')
doc_dir = Sort_Files('Documents')
pictures_dir = Sort_Files('Pictures')
music_dir = Sort_Files('Music')
video_dir = Sort_Files('Videos')

downloads_path = downloads_dir.get_path()
pictures_path = pictures_dir.get_path()
doc_path = doc_dir.get_path()
exe_path = downloads_dir.get_path()

with open('file_formats.json') as file:
    file_formats = json.load(file)

print(pictures_path)
downloads_dir.sort_files(pictures_path, file_formats['image_formats'], 'auto_sort')
downloads_dir.sort_files(doc_path, file_formats['document_formats'])

