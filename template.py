import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "ChurnPrediction"


list_of_files = [
    #needed for github actions
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]


# Loop through the list of files
for filepath in list_of_files:
    # Convert the filepath to a Path object
    filepath = Path(filepath)
    # Extract directory and filename from the filepath
    filedir, filename = os.path.split(filepath)

    # Check if the file's directory is not empty (not the current directory)
    if filedir != "":
        # Create the directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        # Log creation of directory for the file
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Check if the file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file if it doesn't exist or is empty
        with open(filepath, "w") as f:
            pass  # Placeholder, no content added to the file
            # Log creation of an empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        # Log if the file already exists
        logging.info(f"{filename} already exists")