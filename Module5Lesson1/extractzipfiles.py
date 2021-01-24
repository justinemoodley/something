import zipfile

with zipfile.ZipFile('myarchive.zip', 'r') as zipfile:
    zipfile.extract('file1.txt')
    the_path = 'Extraction'
    zipfile.extractall(path=the_path)