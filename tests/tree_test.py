from gendiff.tree import make_tree


def test_tree_maker():
    """
    Tests the function make_tree
    :return: no returns, only assert values
    """
    sample_1: dict = {
        "name": "Greg",
        "surname": "Saliba",
        "date_of_birth": "14-06-1996",
        "person_data": {
            "age": 26,
            "height": 183
        }
    }
    sample_2: dict = {
        "name": "Greg",
        "surname": "Alexandrov",
        "person_data": {
            "age": 26,
            "height": 178,
            "weight": 85
        }
    }
    func_result = make_tree(sample_1, sample_2)
    assert func_result == {'children': [{'key': 'date_of_birth',
                                         'type': 'deleted',
                                         'value': '14-06-1996'},
                                        {'key': 'name', 'type': 'unchanged',
                                         'value': 'Greg'},
                                        {'children': [
                                            {'key': 'age',
                                             'type': 'unchanged',
                                             'value': 26},
                                            {'key': 'height',
                                             'type': 'changed',
                                             'value1': 183,
                                             'value2': 178},
                                            {'key': 'weight',
                                             'type': 'added',
                                             'value': 85}],
                                            'key': 'person_data',
                                            'type': 'nested'},
                                        {'key': 'surname',
                                         'type': 'changed',
                                         'value1': 'Saliba',
                                         'value2': 'Alexandrov'}],
                           'type': 'root'}
