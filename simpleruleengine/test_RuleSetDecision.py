from unittest import TestCase

import pytest

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.conditional.when_any import WhenAny
from simpleruleengine.operator.Between import Between
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.Gte import Gte
from simpleruleengine.operator.In import In
from simpleruleengine.operator.Lte import Lte
from simpleruleengine.operator.NotIn import NotIn
from simpleruleengine.rulerow.RuleRowDecision import RuleRowDecision
from simpleruleengine.ruleset.RuleSetDecision import RuleSetDecision
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.token.StringToken import StringToken

OWNED = "Not Owned"


class TestRuleSetDecision(TestCase):
    def test_evaluate_exception(self):
        with pytest.raises(TypeError):
            RuleSetDecision(["test_1", "test_2"])

    def test_evaluate(self):
        age_gt_35 = NumericToken("age", Gt(35))
        pet_in_dog_cat = StringToken("pet", In(["dog", "cat"]))
        rule_row_decision_go = RuleRowDecision(
            WhenAll([age_gt_35, pet_in_dog_cat]),
            "GO"
        )

        age_lte_35 = NumericToken("age", Lte(35))
        pet_not_in_dog_cat = StringToken("pet", NotIn(["dog", "cat"]))
        rule_row_decision_no_go = RuleRowDecision(
            WhenAll([age_lte_35, pet_not_in_dog_cat]),
            "NO_GO"
        )

        rule_set_decision = RuleSetDecision([rule_row_decision_go, rule_row_decision_no_go])

        # evaluate a fact now against the rule for no go decision
        fact_for_no_go = {"age": 25, "pet": "parrot"}
        assert rule_set_decision.evaluate(fact_for_no_go) == "NO_GO"

    def test_evaluate_simple_decision(self):
        cibil_score_between_650_800 = NumericToken("cibil_score", Between(floor=650, ceiling=800))
        marital_status_in_married_unspecified = StringToken("marital_status", In(["Married", "Unspecified"]))
        business_owned_by_self_family = StringToken("business_ownership", In(["Owned by Self", "Owned by Family"]))

        rule_row_decision_go = RuleRowDecision(
            WhenAll([cibil_score_between_650_800, marital_status_in_married_unspecified, business_owned_by_self_family]),
            "GO"
        )
        rule_set_decision = RuleSetDecision([rule_row_decision_go])

        fact = dict(cibil_score=700, marital_status="Married", business_ownership="Owned by Self")
        assert rule_set_decision.evaluate(fact) == "GO"

    def test_evaluate_complex_decision(self):
        applicant_age_gte_35 = NumericToken("applicant_age", Gte(35))
        business_owned_by_self_family = StringToken("business_ownership", In(["Owned by Self", "Owned by Family"]))
        applicant_owned_by_self_family = StringToken("applicant_ownership", In(["Owned by Self", "Owned by Family"]))

        rule_row_decision_go = RuleRowDecision(
            WhenAll(
                [applicant_age_gte_35, WhenAny([business_owned_by_self_family, applicant_owned_by_self_family])]
            ),
            "GO"
        )
        rule_set_decision = RuleSetDecision([rule_row_decision_go])

        fact_go = dict(applicant_age=42, applicant_ownership=OWNED, business_ownership="Owned by Self")
        assert rule_set_decision.evaluate(fact_go) == "GO"

        fact_no_go_1 = dict(applicant_age=42, applicant_ownership=OWNED, business_ownership=OWNED)
        assert rule_set_decision.evaluate(fact_no_go_1) != "GO"

        fact_no_go_2 = dict(applicant_age=25, applicant_ownership="Owned by Self", business_ownership="Owned by Self")
        assert rule_set_decision.evaluate(fact_no_go_2) != "GO"
