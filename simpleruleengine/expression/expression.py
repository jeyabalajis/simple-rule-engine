from simpleruleengine.operator.operator import Operator
from simpleruleengine.token.token import Token


class Expression:
    def __init__(self, token: Token, operator: Operator):
        self.token = token
        self.operator = operator

    def evaluate(self, token_dict: dict) -> bool:
        return self.operator.evaluate(self.token.get_token_value(token_dict))
