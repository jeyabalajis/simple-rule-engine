from simpleruleengine.rulerow.RuleRowDecision import RuleRowDecision


class RuleSetDecision:
    NO_DECISION_ROW_EVALUATED = "NO_DECISION_ROW_EVALUATED"

    def __init__(self, rule_rows: [RuleRowDecision]):
        self.validate_rule_rows_type(rule_rows)
        self.rule_rows: [RuleRowDecision] = rule_rows

    def evaluate(self, token_dict: dict):
        for rule_row in self.rule_rows:
            _result = rule_row.evaluate(token_dict)
            if _result == {}:
                continue

            return _result

        return self.NO_DECISION_ROW_EVALUATED

    @classmethod
    def validate_rule_rows_type(cls, rule_rows):
        for rule_row in rule_rows:
            if not isinstance(rule_row, RuleRowDecision):
                raise TypeError("Only RuleRowDecision type allowed for rule rows")
