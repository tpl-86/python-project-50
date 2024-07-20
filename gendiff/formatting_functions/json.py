import json as new_json


def json(data):
    value_json = new_json.dumps(data, indent=2)
    return value_json
