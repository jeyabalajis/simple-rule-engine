from simpleruleengine.operator.NumericOperator import NumericOperator
from simpleruleengine.token.Token import Token


class NumericToken(Token):
    def __init__(self, token_name: str, operator: NumericOperator):
        super().__init__(token_name, operator)

    def evaluate(self, token_dict: dict):
        assert self.token_name in token_dict
        return self.operator.evaluate(token_dict.get(self.token_name))
