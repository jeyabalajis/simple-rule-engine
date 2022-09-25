from unittest import TestCase

import pytest

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.conditional.when_any import WhenAny
from simpleruleengine.expression.expression import Expression
from simpleruleengine.operator.between import Between
from simpleruleengine.operator.greater_than import Gt
from simpleruleengine.operator.greater_than_equal import Gte
from simpleruleengine.operator.string_in import In
from simpleruleengine.operator.less_than_equal import Lte
from simpleruleengine.operator.string_not_in import NotIn
from simpleruleengine.rulerow.rule_row_decision import RuleRowDecision
from simpleruleengine.ruleset.rule_set_decision import RuleSetDecision
from simpleruleengine.token.numeric_token import NumericToken
from simpleruleengine.token.string_token import StringToken

OWNED_BY_FAMILY = "Owned by Family"

OWNED_BY_SELF = "Owned by Self"

OWNED = "Not Owned"


class TestRuleSetDecision(TestCase):
    def test_evaluate_exception(self):
        with pytest.raises(TypeError):
            RuleSetDecision("test_1", "test_2")

    def test_evaluate(self):
        age_gt_35 = Expression(NumericToken("age"), Gt(35))
        pet_in_dog_cat = Expression(StringToken("pet"), In("dog", "cat"))
        rule_row_decision_go = RuleRowDecision(
            WhenAll(age_gt_35, pet_in_dog_cat),
            "GO"
        )

        age_lte_35 = Expression(NumericToken("age"), Lte(35))
        pet_not_in_dog_cat = Expression(StringToken("pet"), NotIn("dog", "cat"))
        rule_row_decision_no_go = RuleRowDecision(
            WhenAll(age_lte_35, pet_not_in_dog_cat),
            "NO_GO"
        )

        rule_set_decision = RuleSetDecision(rule_row_decision_go, rule_row_decision_no_go)

        # evaluate a fact now against the rule for no go decision
        fact_for_no_go = {"age": 25, "pet": "parrot"}
        assert rule_set_decision.evaluate(fact_for_no_go) == "NO_GO"

    def test_evaluate_simple_decision(self):
        cibil_score_between_650_800 = Expression(NumericToken("cibil_score"), Between(floor=650, ceiling=800))
        marital_status_in_married_unspecified = Expression(StringToken("marital_status"), In("Married", "Unspecified"))
        business_owned_by_self_family = Expression(
            StringToken("business_ownership"),
            In(OWNED_BY_SELF, OWNED_BY_FAMILY)
        )

        rule_row_decision_go = RuleRowDecision(
            WhenAll(
                cibil_score_between_650_800,
                marital_status_in_married_unspecified,
                business_owned_by_self_family
            ),
            "GO"
        )
        rule_set_decision = RuleSetDecision(rule_row_decision_go)

        fact = dict(cibil_score=700, marital_status="Married", business_ownership=OWNED_BY_SELF)
        assert rule_set_decision.evaluate(fact) == "GO"

    def test_evaluate_complex_decision(self):
        applicant_age_gte_35 = Expression(NumericToken("applicant_age"), Gte(35))
        business_owned_by_self_family = Expression(
            StringToken("business_ownership"),
            In(OWNED_BY_SELF, OWNED_BY_FAMILY)
        )
        applicant_owned_by_self_family = Expression(
            StringToken("applicant_ownership"),
            In(OWNED_BY_SELF, OWNED_BY_FAMILY)
        )

        rule_row_decision_go = RuleRowDecision(
            WhenAll(
                applicant_age_gte_35,
                WhenAny(
                    business_owned_by_self_family,
                    applicant_owned_by_self_family
                )
            ),
            "GO"
        )
        rule_set_decision = RuleSetDecision(rule_row_decision_go)

        fact_go = dict(
            applicant_age=42,
            applicant_ownership=OWNED,
            business_ownership=OWNED_BY_SELF
        )
        assert rule_set_decision.evaluate(fact_go) == "GO"

        fact_no_go_1 = dict(
            applicant_age=42,
            applicant_ownership=OWNED,
            business_ownership=OWNED
        )
        assert rule_set_decision.evaluate(fact_no_go_1) != "GO"

        fact_no_go_2 = dict(
            applicant_age=25,
            applicant_ownership=OWNED_BY_SELF,
            business_ownership=OWNED_BY_SELF
        )
        assert rule_set_decision.evaluate(fact_no_go_2) != "GO"
