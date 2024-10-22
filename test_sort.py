from sort import Sort_Files

downloads_dir = Sort_Files('Downloads')
doc_dir = Sort_Files('Documents')
pictures_dir = Sort_Files('Pictures')
music_dir = Sort_Files('Music')
video_dir = Sort_Files('Videos')

downloads_path = downloads_dir.get_path()
pictures_path = pictures_dir.get_path()
doc_path = doc_dir.get_path()
exe_path = downloads_dir.get_path()

# downloads_dir.create_dir('test_dir')

# pictures_dir.create_dir('auto_sorted_img')

downloads_dir.sort_img_files(pictures_path)
downloads_dir.sort_doc_files(doc_path)
downloads_dir.sort_exe_files('exe_files', exe_path)