import json


def generate_diff(path1: str, path2: str) -> str:
    """
    Compare the two files and prints the differences
    params: path1: old file version
    params: path2: new file version
    returns: difference between them
    """
    with open(path1, 'r') as f1:
        with open(path2, 'r') as f2:
            old_info = f1.read()
            new_info = f2.read()
            old_info: dict = json.loads(old_info)
            new_info: dict = json.loads(new_info)
            list_of_results: list = []
            for key, value in old_info.items():
                if key in new_info:
                    if new_info[key] == old_info[key]:
                        list_of_results.append(f"{key}: {value}")
                    else:
                        list_of_results.append(f"- {key}: {value}")
                        list_of_results.append(f"+ {key}: {new_info[key]}")
                else:
                    list_of_results.append(f"- {key}: {value}")
            for key, value in new_info.items():
                if key not in old_info:
                    list_of_results.append(f"+ {key}: {value}")
            result: str = '{\n'
            for item in list_of_results:
                result += f"\t{item}\n"
            result += '}'
            return result
