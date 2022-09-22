from abc import ABC, abstractmethod
from typing import List
from simpleruleengine.utils.type_util import is_dict


class Rule(ABC):
    def __init__(self, tokens: List):
        self.tokens = tokens

    @abstractmethod
    def evaluate(self, token_dict: dict) -> bool:
        if not is_dict(token_dict):
            raise ValueError("Only dict is allowed for token_dict")

        return True

