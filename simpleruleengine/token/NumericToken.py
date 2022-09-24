from simpleruleengine.token.Token import Token


class NumericToken(Token):
    def __init__(self, name: str):
        super().__init__(name)

    def get_token_dict_structure(self) -> dict:
        return super(NumericToken, self).get_token_dict_structure()

    def get_token_value(self, token_dict: dict):
        return super(NumericToken, self).get_token_value(token_dict)
