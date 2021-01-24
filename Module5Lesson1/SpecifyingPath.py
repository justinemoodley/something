import os

root_path = "c:/users/username"
print(root_path)

root_path = os.path.join("c:", "users", "username")
print(root_path)

root_path = os.getcwd()
print(root_path)

os.chdir("/home")
root_path = os.getcwd()
print(root_path)

