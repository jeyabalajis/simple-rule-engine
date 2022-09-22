from unittest import TestCase

import pytest

from simpleruleengine.operator.Eq import Eq
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.Gte import Gte
from simpleruleengine.operator.Lt import Lt
from simpleruleengine.operator.Lte import Lte
from simpleruleengine.token.NumericToken import NumericToken


class TestNumericToken(TestCase):
    def test_numeric_type_gte(self):
        with pytest.raises(ValueError):
            Gte("35")

    def test_numeric_type_lte(self):
        with pytest.raises(ValueError):
            Lte("35")

    def test_evaluate_gte(self):
        _gte = Gte(35)
        numeric_token = NumericToken("my_token", _gte)
        if not numeric_token.evaluate({"my_token": 40}):
            self.fail()

    def test_evaluate_gt(self):
        _gt = Gt(35)
        numeric_token = NumericToken("my_token", _gt)
        if not numeric_token.evaluate({"my_token": 40}):
            self.fail()

    def test_evaluate_lte(self):
        _lte = Lte(35)
        numeric_token = NumericToken("my_token", _lte)
        if not numeric_token.evaluate({"my_token": 35}):
            self.fail()

    def test_evaluate_lt(self):
        _lte = Lt(35)
        numeric_token = NumericToken("my_token", _lte)
        if not numeric_token.evaluate({"my_token": 34}):
            self.fail()

    def test_evaluate_eq(self):
        _eq = Eq(35.567)
        numeric_token = NumericToken("my_token", _eq)
        if numeric_token.evaluate({"my_token": 35.56}):
            self.fail()

        if not numeric_token.evaluate({"my_token": 35.567}):
            self.fail()
