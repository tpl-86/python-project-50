import json
from gendiff.generate_diff import generate_diff
from gendiff.formatting_functions.json import json as format_json
from pathlib import Path


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_json():
    file1 = str(get_path('file1.json'))
    file2 = str(get_path('file2.json'))
    expected = get_path('expected_json.json')
    with open(expected, 'r') as json_file:
        result = json.load(json_file)
    generated_diff = generate_diff(file1, file2, format_json)
    diff_json = json.loads(generated_diff)
    assert diff_json == result
