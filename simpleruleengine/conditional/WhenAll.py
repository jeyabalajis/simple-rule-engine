from simpleruleengine.conditional.Conditional import Conditional
from simpleruleengine.token.Token import Token
from typing import List


class WhenAll(Conditional):
    def __init__(self, tokens: List[Token]):
        super().__init__(tokens)

    def evaluate(self, token_dict: dict) -> bool:
        super(WhenAll, self).evaluate(token_dict)
        _result = True
        for token in self.tokens:
            _token_result = True
            if isinstance(token, Token):
                _token_result = token.evaluate(token_dict[token.token_name])

            if isinstance(token, Conditional):
                _token_result = token.evaluate(token_dict)

            _result = _result and _token_result
        return _result
