def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, tuple):
        return f"From {format_value(value[0])} to {format_value(value[1])}"
    elif value is None:
        return "null"
    return str(value).lower() if isinstance(value, bool) else f"'{value}'"


def plain(data):
    results = []

    def iter(obj, path=""):
        for item in obj:
            key = item['key']
            type = item['type']
            value = item['value']
            if path:
                new_path = f"{path}.{key}"
            else:
                new_path = key

            match type:
                case 'nested':
                    iter(value, new_path)
                case 'added':
                    results.append(f"Property '{new_path}' "
                                   f"was added with value: "
                                   f"{format_value(value)}")
                case 'deleted':
                    results.append(f"Property '{new_path}' was removed")
                case 'changed':
                    results.append(f"Property '{new_path}' "
                                   f"was updated. {format_value(value)}")

    iter(data)
    return '\n'.join(results)
