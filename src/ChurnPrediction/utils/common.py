#Utils folder is the one where we mention all the common functionality required in our project. Instead of calling 
#function every where we define all the classes and function in the utls folder files and use them

import os
from box.exceptions import BoxValueError
import yaml
from src.ChurnPrediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


#reads a YAML file using PyYAML library and returns its content in a ConfigBox object.
@ensure_annotations #Decorator: @ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Purpose: Reads a YAML file and returns its content wrapped in a ConfigBox.
    Arguments: path_to_yaml: Path to the YAML file to be read.
    Raises:
    ValueError: If the YAML file is empty.
    Exception: For any other unexpected errors during the file reading process.
    Returns:
    ConfigBox: An object of type ConfigBox containing the content of the YAML file

    """
    try:
        with open(path_to_yaml) as yaml_file:
            #open and load the content of the YAML file using yaml.safe_load
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    #If the YAML file is empty (BoxValueError is presumably a custom exception for this case), it raises a ValueError with an appropriate message.
    except BoxValueError:
        raise ValueError("yaml file is empty")
    #If any other exception occurs during the file reading process, it re-raises that exception.
    except Exception as e:
        raise e
    


@ensure_annotations
#Creates directories based on the provided paths.
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    #It takes a list of directory paths and attempts to create each directory. 
    for path in path_to_directories:
        #exist_ok=True argument ensures that the function doesn't raise an error if the directory already exists.
        os.makedirs(path, exist_ok=True)
        #logs a message indicating the directory creation using the logger.
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
#handles the task of saving a dictionary as JSON to a given file path, while also logging information about the saved file path.
def save_json(path: Path, data: dict):
    """
    Purpose: Saves JSON data to a file specified by the path.
    Arguments:
    path: Path to the JSON file where the data will be saved.
    data: Dictionary object to be saved as JSON.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
#load JSON data from a specified file path and transform it into a ConfigBox object, 
def load_json(path: Path) -> ConfigBox:
    """
    Purpose: Loads JSON data from a file and returns it as a ConfigBox object, possibly for easier attribute access.
    Arguments:
    path: Path to the JSON file to be loaded.
    Returns:
    ConfigBox: An object that may contain the loaded JSON data as class attributes.
    """
    # opens the specified JSON file using open(path)
    with open(path) as f:
        #read and parse the JSON content from the file
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
# save binary data to a specified file path using the joblib library
def save_bin(data: Any, path: Path):
    """
    Purpose: Saves binary data to a file.
    Arguments:
    data: Data to be saved as binary.
    path: Path to the binary file where the data will be saved.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Purpose: Loads binary data from a file.
    Arguments:
    path: Path to the binary file to be loaded.
    Returns:
    Any: The object stored in the binary file.
    """
    #After successfully loading the binary data, it logs a message using the logger, indicating  path from which the binary file was loaded.
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str:
    """
    Purpose: Retrieves the size of a file in kilobytes.
    Arguments:
    path: Path to the file for which the size needs to be calculated.
    Returns:
    str: Size of the file in kilobytes as a string.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"