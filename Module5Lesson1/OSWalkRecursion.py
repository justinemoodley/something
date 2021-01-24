import os


def Contents(current_path):
    print(current_path[len(root_path) - 5:])

    for current, subdirectories, files in os.walk(current_path):
        # Ensures that the subdirectories and files are listed
        # in alphabetical order.  Sort() sorts the structure by string
        # values.
        subdirectories.sort()
        files.sort()
        # Calls the Contents function for each subdirectory
        # in the current directory
        for current_subdir in subdirectories:
            # Adds the sub-directory name to the overall current
            # path.  The complete path is always required by
            # the Contents function.
            next_path = os.path.join(current_path, current_subdir)

            # Only calls Contents if the path is valid
            if os.path.exists(next_path):
                Contents(next_path)

        # Displays the names of all the files in the current directory
        # along with the name of the current path.  This shows exactly
        # where the file finds itself in the directory structure

        for current_file in files:
            full_file_path = os.path.join(current_path, current_file)

            # Only displays the file name if the path is valid
            if os.path.exists(full_file_path):
                print(full_file_path[len(root_path) - 5:])


root_path = os.getcwd() + "/Test"
Contents(root_path)
