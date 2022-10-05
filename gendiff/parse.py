"""
Script that helps indentify if the file is a yaml or a json
then loads the information from it to a variable
"""
import json
import yaml


def parse(data, extension: str) -> dict:
    """
    Function to load/parse the information from the file
    :param data: file name
    :param extension: the file's extension
    :return: the information as a Python dictionary
    """
    if extension == 'json':
        return json.load(data)
    elif extension in ('yml', 'yaml'):
        return yaml.safe_load(data)
    else:
        raise Exception(f'This format {extension} is unknown to the program')
