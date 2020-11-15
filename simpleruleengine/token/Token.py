from abc import ABC, abstractmethod
from simpleruleengine.operator.Operator import Operator


class Token(ABC):
    def __init__(self, token_name: str, operator: Operator):
        self.token_name = token_name
        self.operator = operator

    @abstractmethod
    def evaluate(self, value_to_evaluate):
        pass
