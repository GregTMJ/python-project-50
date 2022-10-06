"""
Comparing 2 files json and yaml to see if the scrips works
"""
from gendiff.diff import generate_diff

SAMPLE_RESULT: str = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


def test_diff_json():
    """
    Testing the difference between 2 json files
    """
    result: str = generate_diff('../fixtures/file1.json', '../fixtures/file2.json')
    assert result == SAMPLE_RESULT


def test_diff_yaml():
    """
    testing the difference between 2 yaml files
    """
    result: str = generate_diff('fixtures/file1.yaml', 'fixtures/file2.yaml')
    assert result == SAMPLE_RESULT


def test_diff_yaml_json():
    """
    testing the difference between yaml and json files
    """
    result: str = generate_diff('fixtures/file1.json', 'fixtures/file2.yaml')
    assert result == SAMPLE_RESULT
