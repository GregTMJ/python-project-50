import json


def reformate_tree(tree: dict):
    """
    Reformates in json formate
    """
    return json.dumps(tree, indent=2)
