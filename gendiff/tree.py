"""
Script that transforms the 2 dicts into a tree
"""


def build(old_node: dict, new_node: dict) -> list:
    """
    helps add items to the tree in the needed order
    """
    result: list = []
    keys = set(old_node.keys() | new_node.keys())
    for key in sorted(keys):
        if key not in new_node:
            result.append({
                "key": key,
                "type": "deleted",
                "value": old_node[key]
            })
        elif key not in old_node:
            result.append({
                "key": key,
                "type": "added",
                "value": new_node[key]
            })
        elif isinstance(old_node[key], dict) \
                and isinstance(new_node[key], dict):
            result.append({
                "key": key,
                "type": "nested",
                "children": build(old_node[key], new_node[key])
            })
        elif old_node[key] != new_node[key]:
            result.append({
                "key": key,
                "type": "changed",
                "value1": old_node[key],
                "value2": new_node[key]
            })
        else:
            result.append({
                "key": key,
                "type": "unchanged",
                "value": old_node[key]
            })
    return result


def make_tree(node1: dict, node2: dict) -> dict:
    """
    Generates a tree
    """
    return {
        "type": "root",
        "children": build(node1, node2)
    }
