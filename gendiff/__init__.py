from gendiff.generate_diff import generate_diff
from gendiff.formatting_functions.plain import plain
from gendiff.formatting_functions.stylish import stylish
from gendiff.formatting_functions.json import json

__all__ = (
    'generate_diff',
    'stylish',
    'plain',
    'json'
)
