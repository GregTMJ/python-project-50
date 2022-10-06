"""
testing json formatting
"""
from gendiff.parse import parse
from gendiff.tree import make_tree
from gendiff.formatters import json_formatter, stylish
from gendiff.formatters import plain

SAMPLE_1 = parse(open('fixtures/file1.json', 'r'), 'json')
SAMPLE_2 = parse(open('fixtures/file2.json', 'r'), 'json')
TREE_SAMPLE = make_tree(SAMPLE_1, SAMPLE_2)
SIMPLE_TREE_SAMPLE: dict = {'children': [
    {'key': 'date_of_birth',
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


def test_json():
    """
    Script to test our json_formatter
    """
    formatter = json_formatter.reformate(TREE_SAMPLE)
    assert formatter == """{
  "type": "root",
  "children": [
    {
      "key": "common",
      "type": "nested",
      "children": [
        {
          "key": "follow",
          "type": "added",
          "value": false
        },
        {
          "key": "setting1",
          "type": "unchanged",
          "value": "Value 1"
        },
        {
          "key": "setting2",
          "type": "deleted",
          "value": 200
        },
        {
          "key": "setting3",
          "type": "changed",
          "value1": true,
          "value2": null
        },
        {
          "key": "setting4",
          "type": "added",
          "value": "blah blah"
        },
        {
          "key": "setting5",
          "type": "added",
          "value": {
            "key5": "value5"
          }
        },
        {
          "key": "setting6",
          "type": "nested",
          "children": [
            {
              "key": "doge",
              "type": "nested",
              "children": [
                {
                  "key": "wow",
                  "type": "changed",
                  "value1": "",
                  "value2": "so much"
                }
              ]
            },
            {
              "key": "key",
              "type": "unchanged",
              "value": "value"
            },
            {
              "key": "ops",
              "type": "added",
              "value": "vops"
            }
          ]
        }
      ]
    },
    {
      "key": "group1",
      "type": "nested",
      "children": [
        {
          "key": "baz",
          "type": "changed",
          "value1": "bas",
          "value2": "bars"
        },
        {
          "key": "foo",
          "type": "unchanged",
          "value": "bar"
        },
        {
          "key": "nest",
          "type": "changed",
          "value1": {
            "key": "value"
          },
          "value2": "str"
        }
      ]
    },
    {
      "key": "group2",
      "type": "deleted",
      "value": {
        "abc": 12345,
        "deep": {
          "id": 45
        }
      }
    },
    {
      "key": "group3",
      "type": "added",
      "value": {
        "deep": {
          "id": {
            "number": 45
          }
        },
        "fee": 100500
      }
    }
  ]
}"""


def test_plain():
    """
    testing the plain formate
    """
    formatter = plain.reformate(TREE_SAMPLE)
    assert formatter == """Property 'common.follow' was added with value:  false
Property 'common.setting2' was deleted
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value:  'blah blah'
Property 'common.setting5' was added with value:  [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value:  'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was deleted
Property 'group3' was added with value:  [complex value]"""


def test_stylish():
    """
    testing the stylish formate
    """
    formatter = stylish.reformate(SIMPLE_TREE_SAMPLE)
    assert formatter == """{
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
