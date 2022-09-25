from operator import ge
from operator import le

from simpleruleengine.operator.numeric_operator import NumericOperator


class Between(NumericOperator):
    def __init__(self, *, floor: float, ceiling: float):
        super().__init__(floor)
        self.floor = floor
        self.ceiling = ceiling

    def evaluate(self, value_to_evaluate):
        return ge(value_to_evaluate, self.floor) and le(value_to_evaluate, self.ceiling)
