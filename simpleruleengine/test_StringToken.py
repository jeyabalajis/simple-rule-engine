from unittest import TestCase

import pytest

from simpleruleengine.operator.In import In
from simpleruleengine.operator.NotIn import NotIn
from simpleruleengine.token.StringToken import StringToken


class TestStringToken(TestCase):
    def test_string_type(self):
        with pytest.raises(ValueError):
            _in = In(35)

    def test_string_type_list(self):
        with pytest.raises(ValueError):
            _in = In([35, 45, 67])

    def test_evaluate_in(self):
        _in = In(["dog", "cat"])
        str_token = StringToken("my_token", _in)
        if not str_token.evaluate("dog"):
            self.fail()

    def test_evaluate_not_in(self):
        _not_in = NotIn(["dog", "cat"])
        str_token = StringToken("my_token", _not_in)
        if not str_token.evaluate("DOG"):
            self.fail()
