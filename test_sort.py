from sort import Sort_Files

downloads_dir = Sort_Files('Downloads')
doc_dir = Sort_Files('Documents')
pictures_dir = Sort_Files('Pictures')
music_dir = Sort_Files('Music')
video_dir = Sort_Files('Videos')

downloads_path = downloads_dir.get_path()
pictures_path = pictures_dir.get_path()
doc_path = doc_dir.get_path()

# downloads_dir.create_dir('test_dir')
# downloads_dir.move_file('sample1.heic', pictures_path)

# pictures_dir.create_dir('auto_sorted_img')

files = downloads_dir.get_files_list()

# добавить обработку ошибок try exept на файлы которых нет в коде и всякую другую хуйню
# вывести список форматов в отдельный конфиг
for file in files:
    if file.suffix.lower() in ['.heic', '.jpg', '.png', '.webp', '.jpeg']:
        downloads_dir.move_file(file, pictures_path)
        print(f"\n{file} moved succesully")
    if file.suffix.lower() in ['.xlsx', '.txt', '.pdf', '.csv', '.xls']:
        downloads_dir.move_file(file, doc_path)
        print(f"\n{file} moved succesully")


# files = list(downloads_dir.glob('*.xlsx'))
# print(files)

# for file in get_path('Downloads').glob('*.xlsx'):
#     print(file)