from unittest import TestCase
from simpleruleengine.rule.RuleRowDecision import RuleRowDecision
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.token.StringToken import StringToken
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.In import In
from simpleruleengine.conditional.And import And


class TestRuleRowDecision(TestCase):
    def test_evaluate(self):
        _token_age = NumericToken(token_name="age", operator=Gt(35))
        _in = In(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _tokens = [_token_age, _token_pet]
        _and = And(_tokens)

        _rule_row_decision = RuleRowDecision(_and, "GO")
        _token_dict = {"age": 40, "pet": "dog"}
        if _rule_row_decision.evaluate(_token_dict) != "GO":
            self.fail()
