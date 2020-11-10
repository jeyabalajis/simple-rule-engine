from operator import ge
from simpleruleengine.token.SimpleToken import SimpleToken
from simpleruleengine.operator.NumericOperator import NumericOperator


class NumericToken(SimpleToken):
    def __init__(self, token_name: str, operator: NumericOperator):
        self.token_name = token_name
        self.operator = operator

    def evaluate(self, value_to_evaluate):
        return self.operator.evaluate(value_to_evaluate)
