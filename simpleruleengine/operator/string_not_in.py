from simpleruleengine.operator.string_operator import StringOperator


class NotIn(StringOperator):
    def __init__(self, *base_value):
        super().__init__(base_value)

    def evaluate(self, value_to_evaluate):
        return value_to_evaluate not in self.base_value
