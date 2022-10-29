from simpleruleengine.operator.boolean_operator import BooleanOperator


class IsTrue(BooleanOperator):
    def __init__(self):
        super().__init__()

    def evaluate(self, value_to_evaluate):
        return value_to_evaluate is True
