"""
testing the parser
"""
from gendiff.parse import parse


def test_parser():
    json_data: dict = parse(open('fixtures/file3.json', 'r'), 'json')
    yaml_data: dict = parse(open('fixtures/file2.yaml', 'r'), 'yaml')
    data_type = type(json_data)
    assert json_data == {'host': 'hexlet.io', 'timeout': 50,
                         'proxy': '123.234.53.22', 'follow': False}
    assert yaml_data == {'common': {'follow': False,
                                    'setting1': 'Value 1',
                                    'setting3': None,
                                    'setting4': 'blah blah',
                                    'setting5': {'key5': 'value5'},
                                    'setting6': {'doge': {'wow': 'so much'},
                                                 'key': 'value',
                                                 'ops': 'vops'}},
                         'group1': {'baz': 'bars', 'foo': 'bar',
                                    'nest': 'str'},
                         'group3': {'deep': {'id': {'number': 45}},
                                    'fee': 100500}}
    assert data_type == dict
