import fastjsonschema
import os
import inspect
import json


class RuleRowDecision:
    cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    path = cwd + "/schema/" + "decision_rule_row_schema.json"
    with open(path) as f:
        __rule_row_decision_schema = json.load(f)

    def __init__(self, json_data: dict):
        self.json_data = json_data

    def validate_json_data(self):
        return fastjsonschema.compile(self.__rule_row_decision_schema)(self.json_data)
