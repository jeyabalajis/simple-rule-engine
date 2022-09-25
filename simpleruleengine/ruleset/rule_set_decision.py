from simpleruleengine.rulerow.rule_row_decision import RuleRowDecision
from simpleruleengine.exception.rule_row_exceptions import RuleRowNotEvaluatedException


class RuleSetDecision:
    NO_DECISION_ROW_EVALUATED = "NO_DECISION_ROW_EVALUATED"

    def __init__(self, *rule_rows: RuleRowDecision):
        self.validate_rule_rows_type(rule_rows)
        self.rule_rows = rule_rows

    def evaluate(self, token_dict: dict):
        for rule_row in self.rule_rows:
            try:
                _result = rule_row.evaluate(token_dict)
            except RuleRowNotEvaluatedException:
                continue

            return _result

        return self.NO_DECISION_ROW_EVALUATED

    @classmethod
    def validate_rule_rows_type(cls, rule_rows):
        for rule_row in rule_rows:
            if not isinstance(rule_row, RuleRowDecision):
                raise TypeError("Only RuleRowDecision type allowed for rule rows")
