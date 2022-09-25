from simpleruleengine.token.token import Token
from simpleruleengine.rule.rule import Rule


class RuleToken(Token):
    def __init__(self, name: str, rule: Rule):
        super().__init__(name)
        self.rule = rule

    def get_token_dict_structure(self) -> dict:
        return self.rule.get_token_dict_structure()

    def get_token_value(self, token_dict: dict):
        return self.rule.execute(token_dict)
