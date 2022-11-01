from unittest import TestCase

from simpleruleengine.expression.expression import Expression
from simpleruleengine.operator.greater_than_equal import Gte
from simpleruleengine.operator.boolean_operator import BooleanOperator
from simpleruleengine.operator.string_in import In
from simpleruleengine.token.boolean_token import BooleanToken
from simpleruleengine.token.numeric_token import NumericToken
from simpleruleengine.token.string_token import StringToken


class TestExpression(TestCase):
    def test_evaluate_numeric_token(self):
        numeric_token_age = NumericToken(name="age")
        age_gte_35 = Expression(numeric_token_age, Gte(35))

        fact = dict(age=40)

        assert age_gte_35.evaluate(token_dict=fact) is True

    def test_evaluate_string_token(self):
        string_token_pet = StringToken(name="pet")
        pet_in_dog_cat = Expression(string_token_pet, In("dog", "cat"))

        fact = dict(pet="cat")
        assert pet_in_dog_cat.evaluate(token_dict=fact) is True

        fact = dict(pet="parrot")
        assert pet_in_dog_cat.evaluate(token_dict=fact) is False

    def test_evaluate_boolean_token_true(self):
        boolean_token_big_shot = BooleanToken("big_shot")
        big_shot_true = Expression(boolean_token_big_shot, BooleanOperator(True))

        fact = dict(big_shot=True)
        assert big_shot_true.evaluate(token_dict=fact) is True

        fact = dict(big_shot=False)
        assert big_shot_true.evaluate(token_dict=fact) is False

    def test_evaluate_boolean_token_false(self):
        boolean_token_big_shot = BooleanToken("big_shot")
        big_shot_true = Expression(boolean_token_big_shot, BooleanOperator(False))

        fact = dict(big_shot=True)
        assert big_shot_true.evaluate(token_dict=fact) is False

        fact = dict(big_shot=False)
        assert big_shot_true.evaluate(token_dict=fact) is True
