from unittest import TestCase

import pytest

from simpleruleengine.conditional.And import And
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.In import In
from simpleruleengine.operator.Lte import Lte
from simpleruleengine.operator.NotIn import NotIn
from simpleruleengine.rulerow.RuleRowDecision import RuleRowDecision
from simpleruleengine.ruleset.RuleSetDecision import RuleSetDecision
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.token.StringToken import StringToken


class TestRuleSetDecision(TestCase):
    def test_evaluate_exception(self):
        with pytest.raises(TypeError):
            _rule_set_decision = RuleSetDecision(["test_1", "test_2"])

    def test_evaluate(self):
        _token_age = NumericToken(token_name="age", operator=Gt(35))
        _in = In(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _tokens = [_token_age, _token_pet]
        _and = And(_tokens)

        _rule_row_decision_1 = RuleRowDecision(_and, "GO")

        _token_age = NumericToken(token_name="age", operator=Lte(35))
        _in = NotIn(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _tokens = [_token_age, _token_pet]
        _and = And(_tokens)

        _rule_row_decision_2 = RuleRowDecision(_and, "NO_GO")
        _token_dict = {"age": 25, "pet": "parrot"}

        _rule_set_decision = RuleSetDecision([_rule_row_decision_1, _rule_row_decision_2])
        if _rule_set_decision.evaluate(_token_dict) != "NO_GO":
            self.fail()

    def test_evaluate_no_decision(self):
        _token_age = NumericToken(token_name="age", operator=Gt(35))
        _in = In(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _tokens = [_token_age, _token_pet]
        _and = And(_tokens)

        _rule_row_decision_1 = RuleRowDecision(_and, "GO")
        _rule_set_decision = RuleSetDecision([_rule_row_decision_1])

        _token_dict = {"age": 25, "pet": "parrot"}
        if _rule_set_decision.evaluate(_token_dict) != RuleSetDecision.NO_DECISION_ROW_EVALUATED:
            self.fail()
