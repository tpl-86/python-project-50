import json
import yaml


def get_key_value(value, values):
    if value in values:
        return f'{value}: {values[value]}\n'


def get_file_data(filename):
    if filename.endswith('.yaml') or filename.endswith('.yml'):
        data = yaml.safe_load(open(filename))
    if filename.endswith('.json'):
        data = json.load(open(filename))
    return data


def generate_diff(file1, file2):
    result = ''
    value1 = get_file_data(file1)
    value2 = get_file_data(file2)
    union_values = sorted(list(set(value1.keys()) | set(value2.keys())))
    inter_values = set(value1.keys()) & set(value2.keys())
    diff_values1 = set(value1.keys()) - set(value2.keys())
    for i in union_values:
        if i in inter_values:
            if value1[i] == value2[i]:
                result += f'    {get_key_value(i, value1)}'
            else:
                result += f'  - {get_key_value(i, value1)}'
                result += f'  + {get_key_value(i, value2)}'
        elif i in diff_values1:
            result += f'  - {get_key_value(i, value1)}'
        else:
            result += f'  + {get_key_value(i, value2)}'
    return f'{{\n{result}}}\n'.lower()
