from unittest import TestCase
from simpleruleengine.operator.Between import Between


class TestBetween(TestCase):
    def test_evaluate_true(self):
        assert Between(floor=650, ceiling=800).evaluate(675)

    def test_evaluate_false(self):
        assert Between(floor=650, ceiling=800).evaluate(625) is not True
