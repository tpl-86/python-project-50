import itertools


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def stylish(value, replacer=' ', spaces_count=4):
    def iter_(current_value, depth):
        if (not isinstance(current_value, dict)
                and not isinstance(current_value, list)):
            return format_value(current_value)
        deep_indent_size = depth * spaces_count - 2
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * (depth * spaces_count - 4)
        lines = []
        if isinstance(current_value, list):
            for elem in current_value:
                key = elem['key']
                type = elem['type']
                value = elem['value']
                match type:
                    case 'nested':
                        lines.append(
                            (f'{deep_indent}  {key}: '
                             f'{iter_(value, depth + 1)}'))
                    case 'added':
                        lines.append(
                            (f'{deep_indent}+ {key}: '
                             f'{iter_(value, depth + 1)}'))
                    case 'changed':
                        lines.append(
                            (f'{deep_indent}- {key}: '
                             f'{iter_(value[0], depth + 1)}'))
                        lines.append(
                            (f'{deep_indent}+ {key}: '
                             f'{iter_(value[1], depth + 1)}'))
                    case 'deleted':
                        lines.append(
                            (f'{deep_indent}- {key}: '
                             f'{iter_(value, depth + 1)}'))
                    case _:
                        lines.append(
                            (f'{deep_indent}  {key}: '
                             f'{iter_(value, depth + 1)}'))
        else:
            deep_indent = depth * spaces_count * replacer
            for key, val in current_value.items():
                lines.append(
                    f'{deep_indent}{key}: {iter_(val, depth + 1)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 1)
