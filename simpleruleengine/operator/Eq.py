from simpleruleengine.operator.NumericOperator import NumericOperator
from operator import eq


class Eq(NumericOperator):
    def __init__(self, base_value):
        super().__init__(base_value)

    def evaluate(self, value_to_evaluate):
        return eq(value_to_evaluate, self._base_value)
