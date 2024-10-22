from pathlib import Path
import os, shutil

# sort files according to their type
# create folders for auto_sorted files
# if folder does not exist, create one

class Sort_Files:

    def __init__ (self, specific_path):

        self.specific_path = specific_path

    def get_path(self):
        gen_path = Path.home() / self.specific_path
        if gen_path.exists():
            return gen_path
        else:
            print(f'Error: no such directory {gen_path}')

    def create_dir(self, dir_name):
        Path(self.get_path() / dir_name).mkdir()

    def move_file(self, file_name, dir_name):
        shutil.move(self.get_path() / file_name, self.get_path() / dir_name  )

# подумать как соритровать обрезать путь в файле??
    def get_files_list(self):
        files =  list(self.get_path().glob('*'))
        return files
    
    # def sort_files(self):
    #     for file in self.get_files_list():
    #         if file.glob('*.heic'):
    #             self.move_file





# files = list(get_path('Downloads').glob('*.xlsx'))

# for file in get_path('Downloads').glob('*.xlsx'):
#     print(file)

