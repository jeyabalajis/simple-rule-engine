from simpleruleengine.conditional.conditional import Conditional
from simpleruleengine.token.Token import Token


class WhenAny(Conditional):
    def __init__(self, tokens: [Token]):
        super().__init__(tokens)

    def evaluate(self, token_dict: dict) -> bool:
        super(WhenAny, self).evaluate(token_dict)
        _result = False
        for token in self.tokens:
            _result = _result or token.evaluate(token_dict)
        return _result
