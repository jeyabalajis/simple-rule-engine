from unittest import TestCase

import pytest

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.conditional.when_any import WhenAny
from simpleruleengine.operator.Eq import Eq
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.Gte import Gte
from simpleruleengine.operator.In import In
from simpleruleengine.operator.Lt import Lt
from simpleruleengine.operator.Lte import Lte
from simpleruleengine.rule.rule_score import RuleScore
from simpleruleengine.rulerow.RuleRowDecision import RuleRowDecision
from simpleruleengine.rulerow.RuleRowScore import RuleRowScore
from simpleruleengine.ruleset.RuleSetDecision import RuleSetDecision
from simpleruleengine.ruleset.RuleSetScore import RuleSetScore
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.token.RuleToken import RuleToken
from simpleruleengine.token.StringToken import StringToken


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

    def test_nested_rule(self):
        _gt_operator = Gt(2)
        _token = NumericToken("no_of_bl_paid_off_successfully", _gt_operator)
        _and = WhenAll([_token])

        _score_row = RuleRowScore(antecedent=_and, consequent=70)

        _score_set = RuleSetScore([_score_row], 0.6)
        _token_dict = {"no_of_bl_paid_off_successfully": 3}

        if _score_set.evaluate(_token_dict) != 42:
            self.fail()

        rule_no_bl_paid_off = RuleScore([_score_set])

        token_bl_pl_paid_off_gt_40 = RuleToken("rule_no_bl_paid_off", Gt(40), rule_no_bl_paid_off)
        applicant_age_gte_35 = NumericToken("applicant_age", Gte(35))
        business_owned_by_self_family = StringToken("business_ownership", In(["Owned by Self", "Owned by Family"]))
        rule_row_decision_go = RuleRowDecision(
            WhenAll(
                [applicant_age_gte_35, business_owned_by_self_family, token_bl_pl_paid_off_gt_40]
            ),
            "GO"
        )
        rule_set_decision = RuleSetDecision([rule_row_decision_go])
        fact_go = dict(
            no_of_bl_paid_off_successfully=3,
            applicant_age=42,
            business_ownership="Owned by Self"
        )
        assert rule_set_decision.evaluate(fact_go) == "GO"

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
