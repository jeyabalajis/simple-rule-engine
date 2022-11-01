from abc import abstractmethod

from simpleruleengine.operator.operator import Operator


class BooleanOperator(Operator):
    def __init__(self, base_value: bool):
        self.__assert_boolean(base_value)
        self._base_value = base_value

    @property
    def base_value(self):
        return self._base_value

    @base_value.setter
    def base_value(self, base_value):
        self.__assert_boolean(base_value)
        self._base_value = base_value

    def evaluate(self, value_to_evaluate):
        return value_to_evaluate is self._base_value

    @classmethod
    def __assert_boolean(cls, base_value):
        if not type(base_value).__name__ == "bool":
            raise ValueError("Only bool type allowed")
