from abc import abstractmethod

from simpleruleengine.operator.Operator import Operator
from simpleruleengine.utils.type_util import string, string_list


class StringOperator(Operator):
    def __init__(self, base_value):
        self.__assert_string(base_value)
        self._base_value = base_value

    @property
    def base_value(self):
        return self._base_value

    @base_value.setter
    def base_value(self, base_value):
        self.__assert_string(base_value)
        self._base_value = base_value

    @classmethod
    def __assert_string(cls, base_value):
        if not (string(base_value) or string_list(base_value)):
            raise ValueError("Only String allowed")

    @abstractmethod
    def evaluate(self, value_to_evaluate):
        pass
