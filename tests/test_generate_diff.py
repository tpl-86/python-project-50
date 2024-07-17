from gendiff.generate_diff import generate_diff
from gendiff.formatting_functions.stylish import stylish
from pathlib import Path


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name

def test_generate_diff():
    file1 = str(get_path('file1.json'))
    file2 = str(get_path('file2.json'))
    expected = get_path('expected.txt')
    assert generate_diff(file1, file2, stylish) + '\n' == open(expected).read()


def test_generate_diff():
    file1 = str(get_path('file1.yml'))
    file2 = str(get_path('file2.yml'))
    expected = get_path('expected.txt')
    assert generate_diff(file1, file2, stylish) + '\n' == open(expected).read()
