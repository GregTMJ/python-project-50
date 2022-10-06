"""
Follows the format given by the user or by default
"""
from gendiff.formatters import stylish
from gendiff.formatters import plain
from gendiff.formatters import json_formatter


def select_format(tree: dict, command_format: str):
    """
    Sets the format for the output of the tree
    """
    if command_format == 'stylish':
        return stylish.reformate(tree)
    elif command_format == 'plain':
        return plain.reformate(tree)
    elif command_format == 'json':
        return json_formatter.reformate(tree)
    else:
        raise Exception(f"The format {command_format} is unknown")
