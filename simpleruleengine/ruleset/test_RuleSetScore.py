from unittest import TestCase

import pytest

from simpleruleengine.conditional.WhenAll import WhenAll
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.rulerow.RuleRowScore import RuleRowScore
from simpleruleengine.ruleset.RuleSetScore import RuleSetScore
from simpleruleengine.token.NumericToken import NumericToken


class TestRuleSetScore(TestCase):
    def test_evaluate_exception(self):
        with pytest.raises(TypeError):
            RuleSetScore(["test_1", "test_2"])

    def test_evaluate(self):
        _gt_operator = Gt(2)
        _token = NumericToken("no_of_bl_paid_off_successfully", _gt_operator)
        _and = WhenAll([_token])

        _score_row = RuleRowScore(antecedent=_and, consequent=70)

        _score_set = RuleSetScore([_score_row], 0.6)
        _token_dict = {"no_of_bl_paid_off_successfully": 3}

        if _score_set.evaluate(_token_dict) != 42:
            self.fail()

    def test_evaluate_2(self):
        _gt_operator = Gt(2)
        _token = NumericToken("no_of_bl_paid_off_successfully", _gt_operator)
        _and = WhenAll([_token])

        _score_row = RuleRowScore(antecedent=_and, consequent=70)

        _score_set = RuleSetScore([_score_row], 0.6)
        _token_dict = {"no_of_bl_paid_off_successfully": 1}

        if _score_set.evaluate(_token_dict) != 0.0:
            self.fail()
