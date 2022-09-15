from simpleruleengine.conditional.Conditional import Conditional
from simpleruleengine.exception.rule_row_exceptions import RuleRowNotEvaluatedException


class RuleRowScore:

    def __init__(self, antecedent: Conditional, consequent: float):
        self.__validate_antecedent(antecedent)
        self.__validate_consequent(consequent)

        self.antecedent: Conditional = antecedent
        self.consequent: float = float(consequent)

    def evaluate(self, token_dict: dict) -> float:
        if self.antecedent.evaluate(token_dict):
            return self.consequent
        raise RuleRowNotEvaluatedException

    @classmethod
    def __validate_antecedent(cls, antecedent):
        if not isinstance(antecedent, Conditional):
            raise TypeError("Only Conditional allowed for antecedent")

    @classmethod
    def __validate_consequent(cls, consequent):
        if not (isinstance(consequent, float) or isinstance(consequent, int)):
            raise TypeError("Only int or float allowed for consequent")
