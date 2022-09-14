from unittest import TestCase

import pytest

from simpleruleengine.conditional.WhenAll import WhenAll
from simpleruleengine.conditional.WhenAny import WhenAny
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.In import In
from simpleruleengine.operator.Lt import Lt
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.token.StringToken import StringToken


class TestAnd(TestCase):
    def test_evaluate_true(self):
        _token_age = NumericToken(token_name="age", operator=Gt(35))
        _in = In(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _tokens = [_token_age, _token_pet]
        _and = WhenAll(_tokens)

        _token_dict = {"age": 40, "pet": "dog"}
        if not _and.evaluate(_token_dict):
            self.fail()

    def test_evaluate_false(self):
        _token_age = NumericToken(token_name="age", operator=Gt(35))
        _in = In(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _tokens = [_token_age, _token_pet]
        _and = WhenAll(_tokens)

        _token_dict = {"age": 40, "pet": "parrot"}
        if _and.evaluate(_token_dict):
            self.fail()

        _token_dict = {"age": 25, "pet": "dog"}
        if _and.evaluate(_token_dict):
            self.fail()

    def test_insufficient_values(self):
        with pytest.raises(ValueError):
            _token_age = NumericToken(token_name="age", operator=Gt(35))
            _in = In(["dog", "cat"])
            _token_pet = StringToken("pet", _in)

            _tokens = [_token_age, _token_pet]
            _and = WhenAll(_tokens)

            _token_dict = {"age": 40}
            _and.evaluate(_token_dict)

    def test_recursive(self):
        _token_age_gt = NumericToken(token_name="age", operator=Gt(35))
        _token_age_lt = NumericToken(token_name="age", operator=Lt(18))

        _in = In(["dog", "cat"])
        _token_pet = StringToken("pet", _in)

        _tokens = [_token_age_gt, _token_age_lt]
        _or = WhenAny(_tokens)

        _and = WhenAll([_or, _token_pet])

        _token_dict = {"age": 40, "pet": "parrot"}

        print("Result of WhenAny is {}".format(_or.evaluate(_token_dict)))
        print("Result of WhenAll for {} is {}".format(_token_dict, _and.evaluate(_token_dict)))

        if _and.evaluate(_token_dict):
            self.fail()

        _token_dict = {"age": 10, "pet": "dog"}
        print("Result of WhenAll for {} is {}".format(_token_dict, _and.evaluate(_token_dict)))
        if not _and.evaluate(_token_dict):
            self.fail()

        _token_dict = {"age": 25, "pet": "dog"}
        print("Result of WhenAll for {} is {}".format(_token_dict, _and.evaluate(_token_dict)))
        if _and.evaluate(_token_dict):
            self.fail()
