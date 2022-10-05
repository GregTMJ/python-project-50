from gendiff.formatters.compare import reformate


def test_reformate():
    """
    Testing in the script works correctly
    :return: assertion return
    """
    sample: dict = {'children': [{'key': 'date_of_birth',
                                  'type': 'deleted',
                                  'value': '14-06-1996'},
                                 {'key': 'name', 'type': 'unchanged', 'value': 'Greg'},
                                 {'children': [{'key': 'age', 'type': 'unchanged', 'value': 26},
                                               {'key': 'height',
                                                'type': 'changed',
                                                'value1': 183,
                                                'value2': 178},
                                               {'key': 'weight', 'type': 'added', 'value': 85}],
                                  'key': 'person_data',
                                  'type': 'nested'},
                                 {'key': 'surname',
                                  'type': 'changed',
                                  'value1': 'Saliba',
                                  'value2': 'Alexandrov'}],
                    'type': 'root'}
    reformatted_sample: str = reformate(sample)
    assert reformatted_sample == """{
  - date_of_birth: 14-06-1996
    name: Greg
    person_data: {
        age: 26
      - height: 183
      + height: 178
      + weight: 85
    }
  - surname: Saliba
  + surname: Alexandrov
}"""
