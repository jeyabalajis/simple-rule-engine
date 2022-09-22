from simpleruleengine.conditional.conditional import Conditional
from simpleruleengine.token.Token import Token
from typing import List


class WhenAll(Conditional):
    def __init__(self, tokens: List[Token]):
        super().__init__(tokens)

    def evaluate(self, token_dict: dict) -> bool:
        super(WhenAll, self).evaluate(token_dict)
        _result = True
        for token in self.tokens:
            _result = _result and token.evaluate(token_dict)
        return _result
