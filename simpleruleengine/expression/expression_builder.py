from simpleruleengine.expression.expression import Expression
from simpleruleengine.operator.between import Between
from simpleruleengine.operator.greater_than import Gt
from simpleruleengine.operator.operator import Operator
from simpleruleengine.operator.string_in import In
from simpleruleengine.token.numeric_token import NumericToken
from simpleruleengine.token.string_token import StringToken
from simpleruleengine.token.token import Token

from functools import wraps


def new_object(method):
    @wraps(method)
    def inner(self, *args, **kwargs):
        obj = self.__class__.__new__(self.__class__)
        obj.__dict__ = self.__dict__.copy()
        method(obj, *args, **kwargs)
        return obj

    return inner


class ExpressionBuilder:
    def __init__(self):
        self.token = None
        self.operator = None

    @new_object
    def numeric_token(self, token_name: str):
        self.token = NumericToken(name=token_name)

    @new_object
    def string_token(self, token_name: str):
        self.token = StringToken(name=token_name)

    @new_object
    def greater_than(self, value_to_evaluate):
        self.operator = Gt(base_value=value_to_evaluate)

    @new_object
    def between(self, floor, ceiling):
        self.operator = Between(floor=floor, ceiling=ceiling)

    @new_object
    def in_list(self, *base_value):
        self.operator = In(*base_value)

    def build(self):
        assert isinstance(self.token, Token)
        assert isinstance(self.operator, Operator)

        return Expression(token=self.token, operator=self.operator)
