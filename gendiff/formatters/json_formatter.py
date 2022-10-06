import json


def reformate(tree: dict):
    """
    Reformates in json formate
    """
    return json.dumps(tree, indent=2)
