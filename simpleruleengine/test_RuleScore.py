from unittest import TestCase

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.operator.Eq import Eq
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.Gte import Gte
from simpleruleengine.operator.Lt import Lt
from simpleruleengine.operator.Lte import Lte
from simpleruleengine.rule.rule_score import RuleScore
from simpleruleengine.rulerow.RuleRowScore import RuleRowScore
from simpleruleengine.ruleset.RuleSetScore import RuleSetScore
from simpleruleengine.token.NumericToken import NumericToken


class TestRuleScore(TestCase):
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

        fact_rule_score = dict(last_loan_drawn_in_months=6, no_of_running_bl_pl=2)
        rule_score = RuleScore([no_of_run_bl_pl_rule_set, last_loan_drawn_in_months_rule_set])
        assert rule_score.evaluate(fact_rule_score) == 35.0
