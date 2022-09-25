from unittest import TestCase

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.conditional.when_any import WhenAny
from simpleruleengine.expression.expression import Expression
from simpleruleengine.operator.between import Between
from simpleruleengine.operator.greater_than import Gt
from simpleruleengine.operator.greater_than_equal import Gte
from simpleruleengine.operator.string_in import In
from simpleruleengine.operator.less_than_equal import Lte
from simpleruleengine.operator.string_not_in import NotIn
from simpleruleengine.rule.rule_decision import RuleDecision
from simpleruleengine.rulerow.rule_row_decision import RuleRowDecision
from simpleruleengine.ruleset.rule_set_decision import RuleSetDecision
from simpleruleengine.token.numeric_token import NumericToken
from simpleruleengine.token.string_token import StringToken

OWNED_BY_FAMILY = "Owned by Family"

OWNED_BY_SELF = "Owned by Self"

OWNED = "Not Owned"


class TestRuleDecision(TestCase):
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

        rule_decision = RuleDecision(rule_set_decision)
        assert rule_decision.execute(fact_for_no_go) == "NO_GO"
