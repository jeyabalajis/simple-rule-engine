from abc import ABC, abstractmethod
from simpleruleengine.utils.type_util import is_dict


class Rule(ABC):
    def __init__(self, *tokens):
        self.rule_sets = tokens

    @abstractmethod
    def execute(self, token_dict: dict) -> bool:
        if not is_dict(token_dict):
            raise ValueError("Only dict is allowed for token_dict")

        return True

    @abstractmethod
    def get_token_dict_structure(self) -> dict:
        return dict()

