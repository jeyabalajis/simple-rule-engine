import pytest
from unittest import TestCase
from simpleruleengine.token.StringToken import StringToken
from simpleruleengine.operator.In import In


class TestStringToken(TestCase):
    def test_evaluate_in(self):
        _in = In(["dog", "cat"])
        str_token = StringToken("my_token", _in)
        if not str_token.evaluate("dog"):
            self.fail()
