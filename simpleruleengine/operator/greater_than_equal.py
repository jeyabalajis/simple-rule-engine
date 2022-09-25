from operator import ge

from simpleruleengine.operator.numeric_operator import NumericOperator


class Gte(NumericOperator):
    def __init__(self, base_value):
        super().__init__(base_value)

    def evaluate(self, value_to_evaluate):
        return ge(value_to_evaluate, self._base_value)
