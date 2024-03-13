import json


def is_value_diff(value, values):
    if value in values:
        return True


def generate_diff(file1, file2):
    result = ''
    value1 = json.load(open(file1))
    value2 = json.load(open(file2))
    union_values = sorted(list(set(value1.keys()) | set(value2.keys())))
    inter_values = set(value1.keys()) & set(value2.keys())
    diff_values1 = set(value1.keys()) - set(value2.keys())
    for i in union_values:
        if is_value_diff(i, inter_values):
            if value1[i] == value2[i]:
                result += f'    {i}: {value1.get(i)}\n'
            else:
                result += f'  - {i}: {value1.get(i)}\n'
                result += f'  + {i}: {value2.get(i)}\n'
        elif is_value_diff(i, diff_values1):
            result += f'  - {i}: {value1.get(i)}\n'
        else:
            result += f'  + {i}: {value2.get(i)}\n'
    return f'{{\n{result}}}\n'.lower()
