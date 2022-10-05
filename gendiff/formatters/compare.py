"""
Reformats the tree to get the differences by adding '+'
'-' or nothing in the begining.
"""


def build_indent(depth):
    """
    On each depth we have tabs to add before adding the value
    :return: number of tabs for the current depth
    """
    return " " * (depth * 4 - 2)


def stringify(data, depth) -> str:
    """
    Same functional as JSONStringify in JS but implemented in Python
    """
    if isinstance(data, bool):
        return 'true' if data else 'false'
    if data is None:
        return 'null'
    if isinstance(data, dict):
        parts: list = []
        for key in data:
            indent = build_indent(depth + 1)
            parts.append(f"{indent}  {key}: {stringify(data[key], depth + 1)}")
        output = '\n'.join(parts)
        return f"{{\n{output}\n{build_indent(depth)}  }}"
    return data


def reformate(tree: dict) -> str:
    """
    reformating the tree to get the differences
    :return: string that displays differences
    """
    return node_reformate(tree)


def node_reformate(node, depth=0) -> str:
    """
    starts comparing children inside the root nodes
    :return: string of comparisions
    """
    children = node.get('children')
    indent = build_indent(depth)
    if node['type'] == 'root':
        lines = map(lambda child: node_reformate(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'
    elif node['type'] == 'added':
        return f"{indent}+ {node['key']}: {node['value']}"
    elif node['type'] == 'deleted':
        return f"{indent}- {node['key']}: {node['value']}"
    elif node['type'] == 'changed':
        results: list = [
                f"{indent}- {node['key']}: {node['value1']}",
                f"{indent}+ {node['key']}: {node['value2']}"
                ]
        return '\n'.join(results)
    elif node['type'] == 'unchanged':
        return f"{indent}  {node['key']}: {node['value']}"
    elif node['type'] == 'nested':
        lines = map(lambda child: node_reformate(child, depth + 1), children)
        result = '\n'.join(lines)
        return f"{indent}  {node['key']}: {{\n{result}\n{indent}  }}"
    else:
        raise Exception(f"Unknown type: {node['type']}")

