from simpleruleengine.operator.StringOperator import StringOperator
from simpleruleengine.token.Token import Token


class StringToken(Token):
    def __init__(self, token_name: str, operator: StringOperator):
        super().__init__(token_name, operator)

    def evaluate(self, token_dict: dict):
        if self.token_name not in token_dict:
            raise ValueError("{} not in token_dict".format(self.token_name))
        return self.operator.evaluate(token_dict.get(self.token_name))
