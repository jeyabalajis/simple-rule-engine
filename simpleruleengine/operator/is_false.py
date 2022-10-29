from simpleruleengine.operator.boolean_operator import BooleanOperator


class IsFalse(BooleanOperator):
    def __init__(self):
        super().__init__()

    def evaluate(self, value_to_evaluate):
        return value_to_evaluate is False
