from simpleruleengine.token.Token import Token
from simpleruleengine.operator.StringOperator import StringOperator


class StringToken(Token):
    def __init__(self, token_name: str, operator: StringOperator):
        super().__init__(token_name, operator)

    def evaluate(self, value_to_evaluate):
        return self.operator.evaluate(value_to_evaluate)
