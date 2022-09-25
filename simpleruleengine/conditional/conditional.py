from abc import ABC, abstractmethod
from typing import Union

from simpleruleengine.expression.expression import Expression
from simpleruleengine.utils.type_util import is_dict


class Conditional(ABC):
    """ Conditional is an abstract base class for validating a set of Tokens or Conditionals """

    def __init__(self, *expressions):
        self.expressions = expressions

    @abstractmethod
    def evaluate(self, token_dict: dict) -> bool:
        if not is_dict(token_dict):
            raise ValueError("Only dict is allowed for token_dict")

        return True

    def get_token_dict_structure(self) -> dict:
        """get_tokens_dict returns a dict of expressions with token_name as key.
        This can be used by consumer to fill values before calling evaluate
        """
        token_dict = {}
        for expression in self.expressions:
            token_dict_for_expression = expression.token.get_token_dict_structure()
            for key, value in token_dict_for_expression.items():
                token_dict[key] = value

        return token_dict
