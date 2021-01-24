import os
from datetime import datetime

results = os.stat('\\Users\Justine\PycharmProjects\PRGModule5\Test\B\six\A file 3-1.png')
print(results)
print()
print('Size: {} bytes'.format(results.st_size))
print('Created: {}'.format(datetime.fromtimestamp(results.st_ctime)))
print('Accessed: {}'.format(datetime.fromtimestamp(results.st_atime)))
print('Modified: {}'.format(datetime.fromtimestamp(results.st_mtime)))
