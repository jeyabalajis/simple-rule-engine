from unittest import TestCase

from simpleruleengine.conditional.And import And
from simpleruleengine.conditional.Or import Or
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.In import In
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.token.StringToken import StringToken


class TestOr(TestCase):
    def test_evaluate_true(self):
        _token_age = NumericToken(token_name="age", operator=Gt(35))
        _in = In(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _tokens = [_token_age, _token_pet]
        _or = Or(_tokens)

        _token_dict = {"age": 25, "pet": "dog"}
        if not _or.evaluate(_token_dict):
            self.fail()

    def test_evaluate_false(self):
        _token_age = NumericToken(token_name="age", operator=Gt(35))
        _in = In(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _tokens = [_token_age, _token_pet]
        _or = Or(_tokens)

        _token_dict = {"age": 25, "pet": "parrot"}
        if _or.evaluate(_token_dict):
            self.fail()

    def test_recursive(self):
        _token_age_gt = NumericToken(token_name="age", operator=Gt(35))

        _in = In(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _in = In(["owned", "leased"])
        _token_ownership = StringToken("ownership", _in)

        _tokens = [_token_age_gt, _token_pet]
        _or = Or(_tokens)

        _and = And([_or, _token_ownership])

        _token_dict = {"age": 40, "pet": "parrot", "ownership": "owned"}

        if not _and.evaluate(_token_dict):
            self.fail()

        _token_dict = {"age": 10, "pet": "dog", "ownership": "rented"}
        if _and.evaluate(_token_dict):
            self.fail()

        _token_dict = {"age": 25, "pet": "parrot", "ownership": "owned"}
        if _and.evaluate(_token_dict):
            self.fail()
