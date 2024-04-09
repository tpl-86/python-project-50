from gendiff.generate_diff import get_file_data
from pathlib import Path


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_get_file_data():
    filename = str(get_path('test_get_file_data.yml'))
    assert get_file_data(filename) == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
