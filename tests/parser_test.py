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
    assert yaml_data == {'common': {'setting1': 'Value 1', 'setting2': 200,
                                    'setting3': True, 'setting6':
                                        {'key': 'value', 'doge': {'wow': ''}}
                                    },
                         'group1': {'baz': 'bas', 'foo': 'bar', 'nest':
                                    {'key': 'value'}},
                         'group2': {'abc': 12345, 'deep': {'id': 45}}}
    assert data_type == dict
