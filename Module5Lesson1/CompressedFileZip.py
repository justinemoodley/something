"""import zipfile

with zipfile.ZipFile('myarchive.zip', 'r') as zipfile:
    for current in zipfile.namelist():
        print(current)"""
import zipfile

with zipfile.ZipFile('myarchive.zip', 'r') as zipfile:
      file_info = zipfile.getinfo('A file A-1.png')
      print('File size: {} bytes'.format(file_info.file_size))
      print('Compressed size: {} bytes'.format(file_info.compress_size))
      print('Last modified: {}'.format(file_info.date_time))


with zipfile.ZipFile('myarchive.zip', 'r') as zipfile:
    zipfile.extract('file1.txt')
    the_path = 'Extraction'
    zipfile.extractall(path=the_path)