from unittest import TestCase

import pytest

from simpleruleengine.conditional.WhenAll import WhenAll
from simpleruleengine.operator.Eq import Eq
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.Gte import Gte
from simpleruleengine.operator.Lt import Lt
from simpleruleengine.operator.Lte import Lte
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

    def test_evaluate_complex_score(self):
        no_run_bl_pl_gte_7_score_minus_100 = RuleRowScore(WhenAll([NumericToken("no_of_running_bl_pl", Gte(7))]), -100)
        no_run_bl_pl_gte_4_score_minus_40 = RuleRowScore(WhenAll([NumericToken("no_of_running_bl_pl", Gte(4))]), -40)
        no_run_bl_pl_gte_2_score_30 = RuleRowScore(WhenAll([NumericToken("no_of_running_bl_pl", Gte(2))]), 30)
        no_run_bl_pl_gte_0_score_100 = RuleRowScore(WhenAll([NumericToken("no_of_running_bl_pl", Gte(0))]), 100)

        no_of_run_bl_pl_rule_set = RuleSetScore(
            [no_run_bl_pl_gte_7_score_minus_100, no_run_bl_pl_gte_4_score_minus_40,
             no_run_bl_pl_gte_2_score_30, no_run_bl_pl_gte_0_score_100],
            0.5
        )

        fact_no_run_bl_pl_2 = dict(no_of_running_bl_pl=2)
        assert no_of_run_bl_pl_rule_set.evaluate(fact_no_run_bl_pl_2) == 15.0

        last_loan_drawn_in_months_eq_0_score_30 = RuleRowScore(
            WhenAll([NumericToken("last_loan_drawn_in_months", Eq(0))]),
            30
        )
        last_loan_drawn_in_months_lt_3_score_minus_30 = RuleRowScore(
            WhenAll([NumericToken("last_loan_drawn_in_months", Lt(3))]),
            -30
        )
        last_loan_drawn_in_months_lte_12_score_40 = RuleRowScore(
            WhenAll([NumericToken("last_loan_drawn_in_months", Lte(12))]),
            40
        )
        last_loan_drawn_in_months_gt_12_score_100 = RuleRowScore(
            WhenAll([NumericToken("last_loan_drawn_in_months", Gt(12))]),
            100
        )

        last_loan_drawn_in_months_rule_set = RuleSetScore(
            [
                last_loan_drawn_in_months_eq_0_score_30,
                last_loan_drawn_in_months_lt_3_score_minus_30,
                last_loan_drawn_in_months_lte_12_score_40,
                last_loan_drawn_in_months_gt_12_score_100
            ],
            0.5
        )

        fact_last_loan_drawn_in_months_lte_12 = dict(last_loan_drawn_in_months=6)
        assert last_loan_drawn_in_months_rule_set.evaluate(fact_last_loan_drawn_in_months_lte_12) == 20.0
