from abc import ABC, abstractmethod
from typing import List, Union
from simpleruleengine.token.Token import Token
from simpleruleengine.utils.type_util import is_dict
from simpleruleengine.rule.rule import Rule


class Conditional(ABC):
    """ Conditional is an abstract base class for validating a set of Tokens or Conditionals """

    def __init__(self, tokens: List):
        self.__validate_tokens(tokens)
        self.tokens = tokens

    @abstractmethod
    def evaluate(self, token_dict: dict) -> bool:
        if not is_dict(token_dict):
            raise ValueError("Only dict is allowed for token_dict")

        return True

    def get_tokens_dict(self) -> dict:
        """get_tokens_dict returns a dict of tokens with token_name as key.
        This can be used by consumer to fill values before calling evaluate
        """
        token_dict = {}
        for token in self.tokens:
            token_dict[token.token_name] = None

        return token_dict

    @classmethod
    def __validate_tokens(cls, tokens):
        if type(tokens).__name__ not in 'list':
            raise TypeError("Only List allowed")

        [cls.__validate_token_instance(_token) for _token in tokens]

    @classmethod
    def __validate_token_instance(cls, token):
        if not (
                isinstance(token, Token) or
                isinstance(token, Conditional) or
                isinstance(token, Rule)
        ):
            raise TypeError("Only Token or Conditional or Rule allowed")
