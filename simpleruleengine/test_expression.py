from unittest import TestCase
from simpleruleengine.token.string_token import StringToken
from simpleruleengine.token.numeric_token import NumericToken
from simpleruleengine.token.rule_token import RuleToken
from simpleruleengine.operator.string_in import In
from simpleruleengine.operator.greater_than_equal import Gte
from simpleruleengine.expression.expression import Expression


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

    def test_evaluate_rule_token(self):
        assert True
