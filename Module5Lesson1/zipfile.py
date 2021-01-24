import zipfile

with zipfile.ZipFile('myarchive.zip', 'r') as zipfile:
      for current in zipfile.namelist():
          print(current)
