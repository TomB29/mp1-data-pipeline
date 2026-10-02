# data_loaders.py
from pathlib import Path
import logging
import pandas as pd
import json
import yaml
#mp1-part2.md 2026-09-23
#3 / 6
# Do not call logging.basicConfig() here.
# Use the logging configuration from Part 1.
logger = logging.getLogger(__name__)
def load_csv(filepath):
    """Load a CSV file into a DataFrame.
    filepath is a Path object.
    """
    dataframeobj = pd.read_csv(filepath)
    rows = len(dataframeobj.index)
    logger.info("Loaded CSV file: %s", filepath, f" ({rows} row(s))")
    return dataframeobj


def load_json(filepath):
    """Load a JSON file into a Python object (dict or list).
    filepath is a Path object.
    """
    with open(filepath, "r") as file:
        data = json.load(file)
    logger.info("Loaded JSON file: ", filepath)
    return data
    
def load_yaml(filepath):
    """Load a YAML file into a Python object.
    filepath is a Path object.
    """
    with open(filepath, "r") as f:
        config_yamlobj = yaml.safe_load(f)
    logger.info("Yaml File Loaded %s", filepath)
    return config_yamlobj

def load_data(filepath):
    """Load a file based on its extension.
    filepath is a string, such as 'fixtures/sample.csv'
    """
    # split filepath at . -> return csv, json, yaml
    split_char = filepath.split()
    if split_char[-1] == "csv":
        load_csv(filepath)
    elif split_char[-1] == "json":
        load_json(filepath)
    elif split_char[-1] == yaml:
        load_yaml(filepath)
    else:
        logger.error(filepath, " is not in a supported file type%s")
        raise ValueError("Unsuported file type - %s", filepath)

