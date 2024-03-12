import json


def get_value_diff(value, values1, values2):
    if value in values1 and value in values2:
        if values1[value] == values2[value]:
            return f'    {value}: {values1.get(value)}\n'
        else:
            return f'  - {value}: {values1.get(value)}\n'
        f'  + {value}: {values2.get(value)}\n'
    elif value not in values2:
        return f'  - {value}: {values1.get(value)}\n'
    else:
        return f'  + {value}: {values2.get(value)}\n'


def generate_diff(file1, file2):
    result = ''
    value1 = json.load(open(file1))
    value2 = json.load(open(file2))
    union_values = sorted(list(set(value1.keys()) | set(value2.keys())))
    for i in union_values:
        result += get_value_diff(i, value1, value2)
    return f'{{\n{result}}}\n'.lower()
