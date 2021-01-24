import os
import shutil
#
# root_path = os.getcwd()
# # creates the new directory
# os.mkdir(root_path + '\\X')
#
# # # This will not work since the D directory does not exist
# os.mkdir(root_path + '\\Y\1')
#
# # # Creates the entire path
# os.makedirs(root_path + '\\Y\A')
#
# # # Removes the single directory
# os.rmdir(root_path + '\\X')
#
# # # Removes entire path
# shutil.rmtree(root_path + '\\Y')



files = ['A file 3-1.png', 'A file A-1.png']
for f in files:
    shutil.copy(f, '\\Users\Justine\PycharmProjects\Test\J')


