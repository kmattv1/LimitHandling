import json
from collections import namedtuple


def custom_json_decoder(dictionary):
    return namedtuple('X', dictionary.keys())(*dictionary.values())


def parse_json_to_tuple(json_string):
    return json.loads(json_string, object_hook=custom_json_decoder)
