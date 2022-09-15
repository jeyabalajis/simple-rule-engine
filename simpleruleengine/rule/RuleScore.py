from simpleruleengine.ruleset.RuleSetScore import RuleSetScore
from typing import List


class RuleScore:
    def __init__(self, rule_set_scores: List[RuleSetScore]):
        self.rule_set_scores = rule_set_scores

    def evaluate(self, token_dict: dict):
        total_score = 0
        for rule_set_score in self.rule_set_scores:
            total_score += rule_set_score.evaluate(token_dict=token_dict)

        return total_score
