from pathlib import Path
import os, shutil

class Sort_Files:

    def __init__ (self, specific_path):

        self.specific_path = specific_path

    def get_path(self, dir_name=''):
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

# for file in get_path('Downloads').glob('*.xlsx'):
#     print(file)
