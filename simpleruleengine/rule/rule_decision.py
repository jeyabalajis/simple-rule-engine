from simpleruleengine.ruleset.rule_set_decision import RuleSetDecision
from simpleruleengine.rule.rule import Rule
from typing import Any


class RuleDecision(Rule):
    def __init__(self, *rule_sets: RuleSetDecision):
        super().__init__(rule_sets)
        self.rule_sets = rule_sets

    def execute(self, token_dict: dict) -> Any:
        super(RuleDecision, self).execute(token_dict)
        result = None
        for rule_set in self.rule_sets:
            result = rule_set.evaluate(token_dict=token_dict)

        return result

    def get_token_dict_structure(self) -> dict:
        return super(RuleDecision, self).get_token_dict_structure()
