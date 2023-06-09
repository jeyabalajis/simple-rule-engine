from unittest import TestCase
from simpleruleengine.operator.between import Between
from simpleruleengine.operator.greater_than_equal import Gte
from simpleruleengine.operator.string_in import In
from simpleruleengine.operator.boolean_operator import BooleanOperator
from simpleruleengine.operator.equal import Eq
from simpleruleengine.operator.not_equal import NotEq


class TestOperator(TestCase):
    def test_evaluate_between_true(self):
        assert Between(floor=650, ceiling=800).evaluate(675)

    def test_evaluate_between_false(self):
        assert Between(floor=650, ceiling=800).evaluate(625) is not True

    def test_evaluate_gte_true(self):
        assert Gte(650).evaluate(675) is True

    def test_evaluate_gte_false(self):
        assert Gte(650).evaluate(649) is False

    def test_evaluate_in_true(self):
        assert In("dog", "cat").evaluate("dog") is True

    def test_evaluate_boolean_true(self):
        assert BooleanOperator(True).evaluate(True) is True

    def test_evaluate_boolean_false(self):
        assert BooleanOperator(False).evaluate(False) is True

    def test_evaluate_equal_true(self):
        assert Eq(2).evaluate(3) is False

    def test_evaluate_not_equal_true(self):
        assert NotEq(2).evaluate(3) is True
        assert NotEq(2.25).evaluate(2.26) is True
