"""
Follows the format given by the user or by default
"""
from gendiff.formatters import stylish


def select_format(tree: dict, format: str):
    """
    Sets the format for the output of the tree
    """
    if format == 'stylish':
        return stylish.reformate(tree)
    elif format == 'plain':
        return plain.reformate(tree)
    elif format == 'json':
        return json_formatter.reformate(tree)
    else:
        raise Exception(f"The format {format} is unknown")
