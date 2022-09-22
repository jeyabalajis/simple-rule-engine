from simpleruleengine.ruleset.RuleSetScore import RuleSetScore
from typing import List
from simpleruleengine.rule.rule import Rule


class RuleScore(Rule):
    def __init__(self, tokens: List[RuleSetScore]):
        super().__init__(tokens)
        self.tokens = tokens

    def evaluate(self, token_dict: dict):
        super(RuleScore, self).evaluate(token_dict)
        total_score = 0
        for token in self.tokens:
            total_score += token.evaluate(token_dict=token_dict)

        return total_score
