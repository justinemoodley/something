import os

root_path = os.getcwd() + "\\Test"

for current, subdirectories, files in os.walk(root_path):
    # Displays the name of the current directory
    print("Current directory:", current[len(root_path) - 5:])

    # Displays the names of all the sub-directories in the current directory
    for current_subdir in subdirectories:
        print("Subdirectory:", current_subdir)

    # Displays the names of all the files in the current directory
    for current_file in files:
        print("File:", current_file)

    print()
