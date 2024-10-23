from pathlib import Path
import os, shutil
import json

class Sort_Files:

    def __init__ (self, specific_path):

        self.specific_path = specific_path

    def get_path(self):
        gen_path = Path.home() / self.specific_path 
        if gen_path.exists():
            return gen_path
        else:
            print(f'Error: no such directory {gen_path}')

    def create_dir(self,dest_path, dir_name):
        Path(dest_path / dir_name).mkdir()

    def move_file(self, file_name, dir_name):
        shutil.move(self.get_path() / file_name, self.get_path() / dir_name  )

    def get_files_list(self):
        files =  list(self.get_path().glob('*'))
        return files

    def sort_files(self, dest_path, file_format):
        for file in self.get_files_list():
            if file.suffix.lower() in file_format:
                self.move_file(file, dest_path)
                print(f"\n{file} moved succesully")


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
downloads_dir.sort_files(pictures_path, file_formats['image_formats'])
downloads_dir.sort_files(doc_path, file_formats['document_formats'])
