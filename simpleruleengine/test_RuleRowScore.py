from unittest import TestCase

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.expression.expression import Expression
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.rulerow.RuleRowScore import RuleRowScore
from simpleruleengine.token.NumericToken import NumericToken
import pytest
from simpleruleengine.exception.rule_row_exceptions import RuleRowNotEvaluatedException


class TestRuleRowScore(TestCase):
    def test_evaluate_negative(self):
        no_of_bl_pl_paid_off_gt_2 = Expression(NumericToken("no_of_bl_paid_off_successfully"), Gt(2))
        _and = WhenAll([no_of_bl_pl_paid_off_gt_2])

        _score_row = RuleRowScore(antecedent=_and, consequent=70)

        _token_dict = {"no_of_bl_paid_off_successfully": 1}
        with pytest.raises(RuleRowNotEvaluatedException):
            _score_row.evaluate(_token_dict)

    def test_evaluate_positive(self):
        no_of_bl_pl_paid_off_gt_2 = Expression(NumericToken("no_of_bl_paid_off_successfully"), Gt(2))
        _and = WhenAll([no_of_bl_pl_paid_off_gt_2])

        _score_row = RuleRowScore(antecedent=_and, consequent=70)

        _token_dict = {"no_of_bl_paid_off_successfully": 3}
        if _score_row.evaluate(_token_dict) != 70.0:
            self.fail()
