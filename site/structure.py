import os


# Function to generate the navigation structure as a dictionary
def generate_nav_dict(directory, parent_path=""):
    nav_dict = {}
    # Iterate over all items in the directory
    for item in sorted(os.listdir(directory)):
        full_path = os.path.join(directory, item)
        # Check if it's a directory and recurse
        if os.path.isdir(full_path):
            sub_dict = generate_nav_dict(full_path, f"{parent_path}{item}/")
            if sub_dict:  # if the subdirectory has content, add it to the dict
                nav_dict[item.replace("-", " ").capitalize()] = sub_dict
        elif item.endswith(".md"):  # Check if it's a markdown file and add to dict
            nav_dict[
                item.replace("-", " ").replace(".md", "").capitalize()
            ] = f"{parent_path}{item}"
    return nav_dict


# Function to convert the nested dictionary to the mkdocs nav format
def dict_to_mkdocs_nav(nav_dict, indent=0):
    mkdocs_nav = ""
    indent_str = "    " * indent
    for key, value in nav_dict.items():
        if isinstance(value, dict):
            # Sub-dictionary, need to recurse
            mkdocs_nav += f"{indent_str}- {key}:\n{dict_to_mkdocs_nav(value, indent+1)}"
        else:
            # String, add as file path
            mkdocs_nav += f"{indent_str}- {key}: {value}\n"
    return mkdocs_nav


# Get the directory structure starting from 'areas'
areas_nav_dict = generate_nav_dict(
    "./areas"
)  # Replace with the path to your 'areas' directory

# Convert the dictionary to mkdocs format
mkdocs_nav = dict_to_mkdocs_nav(areas_nav_dict)

# Print the result
print("nav:")
print(mkdocs_nav)
