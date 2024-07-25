import os


def rename_to_lowercase_with_hyphens(current_directory):
    skipped_paths = []

    for root, dirs, files in os.walk(current_directory, topdown=False):
        # Rename files
        for name in files:
            try:
                new_name = name.lower().replace(" ", "-")
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
            except PermissionError:
                skipped_paths.append(os.path.join(root, name))
            except Exception as e:
                print(f"Error renaming file {name}: {e}")

        # Rename directories
        for name in dirs:
            try:
                new_name = name.lower().replace(" ", "-")
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
            except PermissionError:
                skipped_paths.append(os.path.join(root, name))
            except Exception as e:
                print(f"Error renaming directory {name}: {e}")

    return skipped_paths


# Run the function and capture the skipped paths
skipped = rename_to_lowercase_with_hyphens(".")

# Print the skipped paths, if any
if skipped:
    print("The following paths could not be renamed due to permission errors:")
    for path in skipped:
        print(path)
