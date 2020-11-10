import pytest
from unittest import TestCase
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.operator.Gte import Gte
from simpleruleengine.operator.Lte import Lte
from simpleruleengine.operator.Lt import Lt


class TestNumericToken(TestCase):
    def test_numeric_type_gte(self):
        with pytest.raises(ValueError):
            _gte = Gte("35")

    def test_numeric_type_lte(self):
        with pytest.raises(ValueError):
            _lte = Lte("35")

    def test_evaluate_gte(self):
        _gte = Gte(35)
        numeric_token = NumericToken("my_token", _gte)
        if not numeric_token.evaluate(40):
            self.fail()

    def test_evaluate_lte(self):
        _lte = Lte(35)
        numeric_token = NumericToken("my_token", _lte)
        if not numeric_token.evaluate(35):
            self.fail()

    def test_evaluate_lt(self):
        _lte = Lt(35)
        numeric_token = NumericToken("my_token", _lte)
        if not numeric_token.evaluate(34):
            self.fail()
