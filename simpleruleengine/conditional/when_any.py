from simpleruleengine.conditional.conditional import Conditional
from simpleruleengine.expression.expression import Expression


class WhenAny(Conditional):
    def __init__(self, expressions: [Expression]):
        super().__init__(expressions)

    def evaluate(self, token_dict: dict) -> bool:
        super(WhenAny, self).evaluate(token_dict)
        result = False
        for expression in self.expressions:
            result = result or expression.evaluate(token_dict)
        return result
