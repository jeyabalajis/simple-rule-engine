from unittest import TestCase

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.expression.expression import Expression
from simpleruleengine.operator.greater_than import Gt
from simpleruleengine.operator.string_in import In
from simpleruleengine.rulerow.rule_row_decision import RuleRowDecision
from simpleruleengine.token.numeric_token import NumericToken
from simpleruleengine.token.string_token import StringToken


class TestRuleRowDecision(TestCase):
    def test_evaluate(self):
        age_gt_35 = Expression(NumericToken("age"), Gt(35))
        pet_in_dog_cat = Expression(StringToken("pet"), In("dog", "cat"))
        rule_row_decision_go = RuleRowDecision(
            WhenAll(age_gt_35, pet_in_dog_cat),
            "GO"
        )

        fact = {"age": 40, "pet": "dog"}
        assert rule_row_decision_go.evaluate(fact) == "GO"
