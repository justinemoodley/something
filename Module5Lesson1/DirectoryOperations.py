import os
import shutil

from OSWalkRecursion import Contents

# """
# #root_path = os.getcwd()
# # Creates the new directory C
# # os.mkdir(root_path + "/C")
# # This will not work since the D directory does not exist
# # os.mkdir(root_path + "/D/1")
# # Creates the entire path
# # os.makedirs(root_path + "/D/1")
# # Removes the single directory
# # os.rmdir(root_path + "/C")
# # Removes the entire path
# #shutil.rmtree(root_path + "/D")
#
#
# #root_path = '\\Users\Justine\PycharmProjects\PRGModule5\Test'
# # Creates the new directory U
# os.mkdir('\\Users\Justine\PycharmProjects\PRGModule5\Test\U')
# # Uses the previously created Contents method
# # to display the directory structure
# #Contents(root_path)"""



root_path = '\\Users\Justine\PycharmProjects'
# Creates the new directory C
os.mkdir('\\Users\Justine\PycharmProjects\PRGModule5\Test\H')


import os

root_path = '\\Users\Justine\PycharmProjects\PRGModule5\Test'
# Creates the new directory C
os.makedirs('\\Users\Justine\PycharmProjects\PRGModule5\Test\J')
# Uses previously created Contents method
Contents(root_path)


