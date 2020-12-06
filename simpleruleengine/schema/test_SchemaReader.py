from unittest import TestCase
import pytest
import fastjsonschema
from simpleruleengine.schema.SchemaReader import SchemaReader
from simpleruleengine.rule.RuleRowDecision import RuleRowDecision


class TestSchemaReader(TestCase):
    def test_schema(self):
        _schema_reader = SchemaReader(schema_file_name="decision_schema")

        _schema = _schema_reader.schema()
        if not isinstance(_schema, dict):
            self.fail()

        if "$rule" not in _schema:
            self.fail()

    def test_validate_correct_schema(self):
        _test_rule_row = {
            "all_of": {
                "elements": [
                    {
                        "token": {
                            "token_name": "age",
                            "operator": {
                                "operation": ">=",
                                "operator_type": "numeric",
                                "base_value_numeric": 35
                            }
                        }
                    },
                    {
                        "token": {
                            "token_name": "ownership",
                            "operator": {
                                "operation": "in",
                                "operator_type": "string",
                                "base_value_array_string": ["owned", "leased"]
                            }
                        },
                    }
                ]
            }
        }
        _schema_reader = SchemaReader(schema_file_name="conditional_schema")

        if not _schema_reader.validate_json_data(_test_rule_row):
            self.fail()

