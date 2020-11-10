from simpleruleengine.token.SimpleToken import SimpleToken
from simpleruleengine.operator.StringOperator import StringOperator


class StringToken(SimpleToken):
    def __init__(self, token_name: str, operator: StringOperator):
        super().__init__(token_name, operator)

    def evaluate(self, value_to_evaluate):
        return self.operator.evaluate(value_to_evaluate)
