from abc import abstractmethod

from simpleruleengine.operator.operator import Operator


class BooleanOperator(Operator):
    def __init__(self):
        """Boolean Operator is unary, so does not have a base value"""

    @abstractmethod
    def evaluate(self, value_to_evaluate):
        pass
