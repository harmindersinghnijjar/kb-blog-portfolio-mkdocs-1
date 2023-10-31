import os
import logging

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a log file
log_filename = 'empty_file_deletion.log'
file_handler = logging.FileHandler(log_filename, mode='a')
log_format = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] [%(pathname)s:%(lineno)d] - %(message)s - '
                               '[%(process)d:%(thread)d]')
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

# Create a console handler to log to the console
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

# Define the directory path to start the search
directory_path = r'C:\Users\Harminder Nijjar\Desktop\blog\kb-blog-portfolio-mkdocs-master'

# Function to check if a file is empty
def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

# Function to delete empty files in a directory and its subdirectories
def delete_empty_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_file_empty(file_path):
                logger.info(f"Deleted empty file: {file_path}")
                try:
                    os.remove(file_path)
                except Exception as e:
                    logger.error(f"Error deleting file {file_path}: {str(e)}")

# Call the function to delete empty files in the specified directory and its subdirectories
try:
    delete_empty_files(directory_path)
except Exception as e:
    logger.error(f"Error while deleting empty files: {str(e)}")
