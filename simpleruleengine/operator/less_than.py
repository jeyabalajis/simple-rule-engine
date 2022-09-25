from operator import lt

from simpleruleengine.operator.numeric_operator import NumericOperator


class Lt(NumericOperator):
    def __init__(self, base_value):
        super().__init__(base_value)

    def evaluate(self, value_to_evaluate):
        return lt(value_to_evaluate, self._base_value)
