from unittest import TestCase

import pytest

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.conditional.when_any import WhenAny
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.In import In
from simpleruleengine.operator.Lt import Lt
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.token.StringToken import StringToken
from simpleruleengine.expression.expression import Expression


class TestWhenAll(TestCase):
    def test_evaluate_true(self):
        numeric_token_age = NumericToken(name="age")
        age_gt_35 = Expression(numeric_token_age, operator=Gt(35))

        string_token_pet = StringToken(name="pet")
        pet_in_dog_cat = Expression(string_token_pet, In(["dog", "cat"]))

        when_all_age_and_pet = WhenAll([age_gt_35, pet_in_dog_cat])

        token_dict = {"age": 40, "pet": "dog"}
        assert when_all_age_and_pet.evaluate(token_dict) is True

    def test_evaluate_false(self):
        numeric_token_age = NumericToken(name="age")
        age_gt_35 = Expression(numeric_token_age, operator=Gt(35))

        string_token_pet = StringToken(name="pet")
        pet_in_dog_cat = Expression(string_token_pet, In(["dog", "cat"]))

        when_all_age_and_pet = WhenAll([age_gt_35, pet_in_dog_cat])

        token_dict = {"age": 40, "pet": "parrot"}
        assert when_all_age_and_pet.evaluate(token_dict) is False

        token_dict = {"age": 25, "pet": "parrot"}
        assert when_all_age_and_pet.evaluate(token_dict) is False

    def test_insufficient_values(self):
        with pytest.raises(ValueError):
            numeric_token_age = NumericToken(name="age")
            age_gt_35 = Expression(numeric_token_age, operator=Gt(35))

            string_token_pet = StringToken(name="pet")
            pet_in_dog_cat = Expression(string_token_pet, In(["dog", "cat"]))

            when_all_age_and_pet = WhenAll([age_gt_35, pet_in_dog_cat])

            token_dict = {"age": 40}
            when_all_age_and_pet.evaluate(token_dict)
