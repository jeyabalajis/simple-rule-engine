from simpleruleengine.conditional.Conditional import Conditional


class RuleRowDecision:
    def __init__(self, antecedent: Conditional, consequent: any):
        self.antecedent: Conditional = antecedent
        self.consequent: any = consequent

    def evaluate(self, token_dict: dict) -> any:
        if self.antecedent.evaluate(token_dict):
            return self.consequent
        else:
            return {}

    @classmethod
    def __validate_antecedent(cls, antecedent):
        if not isinstance(antecedent, Conditional):
            raise TypeError("Only Conditional allowed for antecedent")
