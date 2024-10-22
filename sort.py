from pathlib import Path
import os, shutil

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

    def get_files_list(self):
        files =  list(self.get_path().glob('*'))
        return files
    
# добавить обработку ошибок try exept на файлы которых нет в коде и всякую другую хуйню
# вывести список форматов в отдельный конфиг
# разобраться с todo
    def sort_img_files(self, dest_path):
        for file in self.get_files_list():
            if file.suffix.lower() in ['.heic', '.jpg', '.png', '.webp', '.jpeg']:
                self.move_file(file, dest_path)
                print(f"\n{file} moved succesully")

    def sort_doc_files(self, dest_path):
        for file in self.get_files_list():
            if file.suffix.lower() in ['.xlsx', '.txt', '.pdf', '.csv', '.xls', '.zip']:
                self.move_file(file, dest_path)
                print(f"\n{file} moved succesully")

    def sort_exe_files(self, dir_name, dest_path):
            self.create_dir(dir_name)
            for file in self.get_files_list():
                if file.suffix.lower() in ['.exe']:
                    self.move_file(file, dest_path / dir_name)
                    print(f"\n{file} moved succesully")
        




# files = list(get_path('Downloads').glob('*.xlsx'))

# for file in get_path('Downloads').glob('*.xlsx'):
#     print(file)

