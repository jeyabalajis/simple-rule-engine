from simpleruleengine.operator.NumericOperator import NumericOperator
from operator import le


class Lte(NumericOperator):
    def __init__(self, base_value):
        super().__init__(base_value)

    def evaluate(self, value_to_evaluate):
        return le(value_to_evaluate, self._base_value)
