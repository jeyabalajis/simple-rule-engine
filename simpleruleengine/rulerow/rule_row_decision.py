from simpleruleengine.conditional.conditional import Conditional
from simpleruleengine.exception.rule_row_exceptions import RuleRowNotEvaluatedException


class RuleRowDecision:
    def __init__(self, antecedent: Conditional, consequent: any):
        self.__validate_antecedent(antecedent)
        self.antecedent: Conditional = antecedent
        self.consequent: any = consequent

    def evaluate(self, token_dict: dict) -> any:
        if self.antecedent.evaluate(token_dict):
            return self.consequent
        raise RuleRowNotEvaluatedException

    @classmethod
    def __validate_antecedent(cls, antecedent):
        if not isinstance(antecedent, Conditional):
            raise TypeError("Only Conditional allowed for antecedent")
