from gendiff.generate_diff import generate_diff
from gendiff.formatting_functions.plain import plain
from pathlib import Path


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_plain():
    file1 = str(get_path('file1.yml'))
    file2 = str(get_path('file2.yml'))
    expected = get_path('expected_plain.txt')
    assert generate_diff(file1, file2, plain) + '\n' == open(expected).read()
