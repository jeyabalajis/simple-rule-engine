from simpleruleengine.ruleset.rule_set_score import RuleSetScore
from typing import List
from simpleruleengine.rule.rule import Rule


class RuleScore(Rule):
    def __init__(self, *rule_sets: RuleSetScore):
        super().__init__(rule_sets)
        self.rule_sets = rule_sets

    def execute(self, token_dict: dict) -> float:
        super(RuleScore, self).execute(token_dict)
        total_score = 0
        for rule_set in self.rule_sets:
            total_score += rule_set.evaluate(token_dict=token_dict)

        return total_score

    def get_token_dict_structure(self) -> dict:
        return super(RuleScore, self).get_token_dict_structure()
