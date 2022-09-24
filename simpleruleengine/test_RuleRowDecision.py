from unittest import TestCase

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.expression.expression import Expression
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.In import In
from simpleruleengine.rulerow.RuleRowDecision import RuleRowDecision
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.token.StringToken import StringToken


class TestRuleRowDecision(TestCase):
    def test_evaluate(self):
        age_gt_35 = Expression(NumericToken("age"), Gt(35))
        pet_in_dog_cat = Expression(StringToken("pet"), In(["dog", "cat"]))
        rule_row_decision_go = RuleRowDecision(
            WhenAll([age_gt_35, pet_in_dog_cat]),
            "GO"
        )

        fact = {"age": 40, "pet": "dog"}
        assert rule_row_decision_go.evaluate(fact) == "GO"
