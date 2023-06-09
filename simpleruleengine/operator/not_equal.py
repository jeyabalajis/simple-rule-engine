from operator import eq

from simpleruleengine.operator.numeric_operator import NumericOperator


class NotEq(NumericOperator):
    def __init__(self, base_value):
        super().__init__(base_value)

    def evaluate(self, value_to_evaluate):
        return False if eq(value_to_evaluate, self._base_value) else True
