"""
Reformates the tree in a plain style
"""


def reformate(tree: dict) -> str:
    """
    reformatting the tree to get the differences
    :return: string that displays differences
    """
    return node_reformate(tree)


def node_reformate(node, ancestry: str = ''):
    """
    starts comparing children inside the root nodes
    :return: string that shows the differences
    """
    children = node.get('children')
    property_name = f"{ancestry}{node.get('key')}"
    if node['type'] == 'root':
        nodes = map(lambda child: node_reformate(child),
                    children)
        nodes_result = sum(nodes, [])
        return '\n'.join(nodes_result)
    elif node['type'] == 'nested':
        nodes = map(lambda child: node_reformate(child, f"{property_name}."),
                    children)
        return sum(nodes, [])
    elif node['type'] == 'added':
        return [f"Property '{property_name}' was added with value:"
                f" {stringify(node['value'])}"]
    elif node['type'] == 'deleted':
        return [f"Property '{property_name}' was removed"]
    elif node['type'] == 'changed':
        return [
            f"Property '{property_name}' was updated. "
            f"From {stringify(node['value1'])} to "
            f"{stringify(node['value2'])}"
        ]
    elif node['type'] == 'unchanged':
        return []
    else:
        raise Exception(f"Type {node['type']} Unknown!")


def stringify(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, list) or isinstance(value, dict):
        return "[complex value]"
    return value
