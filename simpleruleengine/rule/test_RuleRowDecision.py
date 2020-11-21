from unittest import TestCase
from simpleruleengine.rule.RuleRowDecision import RuleRowDecision
import pytest
import fastjsonschema


class TestRuleRowDecision(TestCase):
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
        rule_row_decision = RuleRowDecision(_test_rule_row)

        if not rule_row_decision.validate_json_data():
            self.fail()

    def test_validate_incorrect_schema(self):
        with pytest.raises(fastjsonschema.JsonSchemaException):
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
                                    "base_value_numeric": 45
                                }
                            },
                        }
                    ]
                }
            }
            rule_row_decision = RuleRowDecision(_test_rule_row)

            rule_row_decision.validate_json_data()
