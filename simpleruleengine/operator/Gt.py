from operator import gt

from simpleruleengine.operator.NumericOperator import NumericOperator


class Gt(NumericOperator):
    def __init__(self, base_value):
        super().__init__(base_value)

    def evaluate(self, value_to_evaluate):
        return gt(value_to_evaluate, self._base_value)
