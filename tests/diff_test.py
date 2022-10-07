"""
Comparing 2 files json and yaml to see if the scrips works
"""
from gendiff import generate_diff

SAMPLE_RESULT: str = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_diff_json():
    """
    Testing the difference between 2 json files
    """
    result: str = generate_diff('tests/fixtures/file3.json',
                                'tests/fixtures/file4.json')
    assert result == SAMPLE_RESULT


def test_diff_yaml():
    """
    testing the difference between 2 yaml files
    """
    result: str = generate_diff('tests/fixtures/file3.yaml',
                                'tests/fixtures/file4.yaml')
    assert result == SAMPLE_RESULT


def test_diff_yaml_json():
    """
    testing the difference between yaml and json files
    """
    result: str = generate_diff('tests/fixtures/file3.json',
                                'tests/fixtures/file4.yaml')
    assert result == SAMPLE_RESULT


def test_diff_json_plain():
    """
    testing the difference in plain style
    """
    result: str = generate_diff('tests/fixtures/file1.yaml',
                                'tests/fixtures/file2.yaml',
                                'plain')
    assert result == """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""


def test_diff_json_formate():
    """
    testing the difference in json style
    """
    result: str = generate_diff('tests/fixtures/file1.json',
                                'tests/fixtures/file2.json', 'json')
    assert result == """{
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
