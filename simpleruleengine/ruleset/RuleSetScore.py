from simpleruleengine.rulerow.RuleRowScore import RuleRowScore
from simpleruleengine.exception.rule_row_exceptions import RuleRowNotEvaluatedException


class RuleSetScore:
    def __init__(self, rule_rows: [RuleRowScore], weight: float):
        self.validate_rule_rows_type(rule_rows)
        self.validate_weight(weight)
        self.rule_rows: [RuleRowScore] = rule_rows
        self.weight = weight

    def evaluate(self, token_dict: dict):
        score = 0
        for rule_row in self.rule_rows:
            try:
                score = rule_row.evaluate(token_dict)
                return score * self.weight
            except RuleRowNotEvaluatedException:
                continue
        return score

    @classmethod
    def validate_rule_rows_type(cls, rule_rows):
        for rule_row in rule_rows:
            if not isinstance(rule_row, RuleRowScore):
                raise TypeError("Only RuleRowScore type allowed for rule rows")

    @classmethod
    def validate_weight(cls, weight):
        if not (isinstance(weight, int) or isinstance(weight, float)):
            raise TypeError("Only int or float type allowed for weight")

        if float(weight) > 1 or float(weight) < 0:
            raise ValueError("weight must be greater than zero and less than 1")
