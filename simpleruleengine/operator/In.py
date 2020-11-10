from simpleruleengine.operator.StringOperator import StringOperator


class In(StringOperator):
    def __init__(self, base_value):
        super().__init__(base_value)

    def evaluate(self, value_to_evaluate):
        return value_to_evaluate in self.base_value
