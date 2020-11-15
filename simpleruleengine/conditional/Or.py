from simpleruleengine.conditional.Conditional import Conditional
from simpleruleengine.token.Token import Token


class Or(Conditional):
    def __init__(self, tokens: [Token]):
        super().__init__(tokens)

    def evaluate(self, token_dict: dict) -> bool:
        super(Or, self).evaluate(token_dict)
        _result = False
        for token in self.tokens:
            _token_result = False
            if isinstance(token, Token):
                _token_result = token.evaluate(token_dict[token.token_name])

            if isinstance(token, Conditional):
                _token_result = token.evaluate(token_dict)

            _result = _result or _token_result
        return _result

