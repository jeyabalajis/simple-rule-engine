from abc import abstractmethod

from simpleruleengine.operator.operator import Operator
from simpleruleengine.utils.type_util import numeric


class NumericOperator(Operator):
    def __init__(self, base_value):
        self.__assert_numeric(base_value)
        self._base_value = base_value

    @property
    def base_value(self):
        return self._base_value

    @base_value.setter
    def base_value(self, base_value):
        self.__assert_numeric(base_value)
        self._base_value = base_value

    @classmethod
    def __assert_numeric(cls, base_value):
        if not numeric(base_value):
            raise ValueError("Only Integer and Float allowed")

    @abstractmethod
    def evaluate(self, value_to_evaluate):
        pass
