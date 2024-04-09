def diff(data1, data2):
    keys = sorted(set(data1) | set(data2))

    def compare(key):
        if key not in data1:
            return {'key': key, 'type': 'added', 'value': data2[key]}
        elif key not in data2:
            return {'key': key, 'type': 'deleted', 'value': data1[key]}

        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = diff(data1[key], data2[key])
            return {'key': key, 'type': 'nested', 'value': children}
        elif data1[key] == data2[key]:
            return {'key': key, 'type': 'unchanged', 'value': data1[key]}
        else:
            return {'key': key,
                    'type': 'changed',
                    'value': (data1[key], data2[key])}

    return [compare(key) for key in keys]
