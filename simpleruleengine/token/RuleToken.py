from simpleruleengine.operator.NumericOperator import NumericOperator
from simpleruleengine.token.Token import Token
from simpleruleengine.rule.rule import Rule


class RuleToken(Token):
    def __init__(self, token_name: str, operator: NumericOperator, rule: Rule):
        super().__init__(token_name, operator)
        self.rule = rule

    def evaluate(self, token_dict: dict):
        return self.rule.evaluate(token_dict)
