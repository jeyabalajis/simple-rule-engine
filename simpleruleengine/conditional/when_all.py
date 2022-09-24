from simpleruleengine.conditional.conditional import Conditional
from simpleruleengine.expression.expression import Expression
from typing import List


class WhenAll(Conditional):
    def __init__(self, expressions: List[Expression]):
        super().__init__(expressions)

    def evaluate(self, token_dict: dict) -> bool:
        super(WhenAll, self).evaluate(token_dict)
        result = True
        for expression in self.expressions:
            result = result and expression.evaluate(token_dict)
        return result
