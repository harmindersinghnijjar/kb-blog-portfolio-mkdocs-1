import os
import logging

# Set up logging to capture events when the script runs and any possible errors
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define the log file path and format
log_file_path = "area_script.log"
log_format = logging.Formatter(
    "%(asctime)s - %(name)s - [%(levelname)s] [%(pathname)s:%(lineno)d] - %(message)s - [%(process)d:%(thread)d]"
)

# Create a file handler for writing log messages to a file
file_handler = logging.FileHandler(log_file_path, mode="a")
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

# Create a console handler for writing log messages to the console
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

# Define the root directory (current directory)
root_directory = os.getcwd()


# Function to create a Markdown skeleton for an area and its sub-areas
def create_area_skeleton(area_name, sub_areas):
    # Initialize the Markdown content
    markdown_content = f"# {area_name}\n\n"

    # Add sub-areas if any
    if sub_areas:
        markdown_content += "## Sub-Areas\n\n"
        for sub_area in sub_areas:
            markdown_content += f"- [{sub_area}](./{sub_area.replace(' ', '_')}.md)\n"

    return markdown_content


try:
    # Iterate through subdirectories (areas) in the current directory
    for root, dirs, files in os.walk(root_directory):
        for directory in dirs:
            area_directory = os.path.join(root, directory)

            # Skip hidden directories (those starting with '.')
            if not directory.startswith("."):
                # Create a Markdown file for the area
                area_file_path = os.path.join(
                    area_directory, f"{directory.replace(' ', '_')}.md"
                )

                with open(area_file_path, "w", encoding="utf-8") as md_file:
                    # Extract sub-areas (subdirectories) within the area directory
                    sub_areas = [
                        subdir
                        for subdir in os.listdir(area_directory)
                        if os.path.isdir(os.path.join(area_directory, subdir))
                    ]

                    md_content = create_area_skeleton(directory, sub_areas)
                    md_file.write(md_content)

    logger.info("Skeleton structure created successfully.")
except Exception as e:
    logger.error(f"An error occurred: {str(e)}", exc_info=True)
