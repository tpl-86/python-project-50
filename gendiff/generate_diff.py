import json
import yaml
from gendiff.stylish import stylish
from gendiff.diff import diff


def get_file_data(filename):
    if filename.endswith('.yaml') or filename.endswith('.yml'):
        data = yaml.safe_load(open(filename))
    if filename.endswith('.json'):
        data = json.load(open(filename))
    return data


def generate_diff(file1, file2, formatter=stylish):
    data1 = get_file_data(file1)
    data2 = get_file_data(file2)
    result = diff(data1, data2)
    return formatter(result)
