from abc import ABC, abstractmethod
from typing import List, Union
from simpleruleengine.token.Token import Token
from simpleruleengine.utils.type_util import is_dict


class Conditional(ABC):
    """ Conditional is an abstract base class for validating a set of Tokens or Conditionals """

    def __init__(self, tokens: List):
        self.__validate_tokens(tokens)
        self.tokens = tokens

    @abstractmethod
    def evaluate(self, token_dict: dict) -> bool:
        if not is_dict(token_dict):
            raise ValueError("Only dict is allowed for token_dict")

        for token in self.tokens:
            if isinstance(token, Conditional):
                token.evaluate(token_dict)

            if isinstance(token, Token) and token.token_name not in token_dict:
                raise ValueError("Value for Token Name {} not sent".format(token.token_name))
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
                isinstance(token, Conditional)
        ):
            raise TypeError("Only Token or Conditional allowed")
