"""
Generating the difference inside the 2 files
"""
from gendiff import formatter
from gendiff.parse import parse
from gendiff.tree import make_tree


def get_data_from_file(file: str) -> dict:
    """
    Mediocre function between extracting and giving the data from file
    :param file: the file path
    :return: a parsed Python dict
    """
    return parse(open(file), file.split('.')[-1])


def generate_diff(path1: str, path2: str,
                  formate_name: str = 'stylish') -> str:
    """
    Compare the two files and prints the differences
    params: path1: old file version
    params: path2: new file version
    returns: difference between them
    """
    old_data: dict = get_data_from_file(path1)
    new_data: dict = get_data_from_file(path2)
    diff_tree: dict = make_tree(old_data, new_data)
    return formatter.select_format(diff_tree, formate_name)
