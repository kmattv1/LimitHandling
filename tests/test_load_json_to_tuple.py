from unittest import TestCase

from src.usecase import load_json_to_tuple


class TestJsonToTuple(TestCase):
    def test_given_json_string_when_parsed_then_tuple_matches(self):
        # Given
        json_string = '{"testKey": "test Value", "t_2": "v_2"}'

        # When
        parsed = load_json_to_tuple.parse_json_to_tuple(json_string)

        # Then
        assert parsed.testKey == "test Value"
        assert parsed.t_2 == "v_2"