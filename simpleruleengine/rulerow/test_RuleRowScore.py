from unittest import TestCase

from simpleruleengine.conditional.And import And
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.rulerow.RuleRowScore import RuleRowScore
from simpleruleengine.token.NumericToken import NumericToken


class TestRuleRowScore(TestCase):
    def test_evaluate_negative(self):
        _gt_operator = Gt(2)
        _token = NumericToken("no_of_bl_paid_off_successfully", _gt_operator)
        _and = And([_token])

        _score_row = RuleRowScore(antecedent=_and, consequent=70)

        _token_dict = {"no_of_bl_paid_off_successfully": 1}
        if _score_row.evaluate(_token_dict) != 0.0:
            self.fail()

    def test_evaluate_positive(self):
        _gt_operator = Gt(2)
        _token = NumericToken("no_of_bl_paid_off_successfully", _gt_operator)
        _and = And([_token])

        _score_row = RuleRowScore(antecedent=_and, consequent=70)

        _token_dict = {"no_of_bl_paid_off_successfully": 3}
        if _score_row.evaluate(_token_dict) != 70.0:
            self.fail()
