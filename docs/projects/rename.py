import os


# Define the function to rename the files and folders
def rename_files_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        # Renaming files
        for name in files:
            if "-" in name:
                try:
                    os.rename(
                        os.path.join(root, name),
                        os.path.join(root, name.replace("-", "_")),
                    )
                except PermissionError:
                    print(
                        f"Permission denied to rename the file: {os.path.join(root, name)}"
                    )
        # Renaming directories
        for name in dirs:
            if "-" in name:
                try:
                    os.rename(
                        os.path.join(root, name),
                        os.path.join(root, name.replace("-", "_")),
                    )
                except PermissionError:
                    print(
                        f"Permission denied to rename the directory: {os.path.join(root, name)}"
                    )


# Call the function to rename files and folders in the current working directory
rename_files_folders(os.getcwd())
