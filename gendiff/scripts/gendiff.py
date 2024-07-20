#!/usr/bin/env python3
from gendiff.scripts.cli import parse_args
from gendiff.generate_diff import generate_diff
from gendiff.formatting_functions.plain import plain
from gendiff.formatting_functions.stylish import stylish
from gendiff.formatting_functions.json import json


def main():
    args = parse_args()
    formatters = {
        'stylish': stylish,
        'plain': plain,
        'json': json
    }
    format_func = formatters.get(args.format, stylish)
    diff = generate_diff(args.first_file, args.second_file, format_func)
    print(diff)


if __name__ == '__main__':
    main()
