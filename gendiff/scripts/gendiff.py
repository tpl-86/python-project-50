#!/usr/bin/env python3
from gendiff.scripts.parsing import args
from gendiff.generate_diff import generate_diff
from gendiff.stylish import stylish


def main():
    print(generate_diff(args.first_file, args.second_file, stylish))


if __name__ == '__main__':
    main()
