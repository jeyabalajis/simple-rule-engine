from simpleruleengine.utils.type_util import numeric
from simpleruleengine.operator.NumericOperator import NumericOperator
from operator import ge


class Gte(NumericOperator):
    def __init__(self, base_value):
        super().__init__(base_value)

    def evaluate(self, value_to_evaluate):
        return ge(value_to_evaluate, self._base_value)
