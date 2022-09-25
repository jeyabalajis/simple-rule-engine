from unittest import TestCase

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.conditional.when_any import WhenAny
from simpleruleengine.expression.expression import Expression
from simpleruleengine.operator.greater_than import Gt
from simpleruleengine.operator.string_in import In
from simpleruleengine.token.numeric_token import NumericToken
from simpleruleengine.token.string_token import StringToken


class TestWhenAny(TestCase):
    def test_evaluate_true(self):
        numeric_token_age = NumericToken(name="age")
        age_gt_35 = Expression(numeric_token_age, Gt(35))

        string_token_pet = StringToken(name="pet")
        pet_in_dog_cat = Expression(string_token_pet, In("dog", "cat"))

        when_any_age_or_pet = WhenAny(age_gt_35, pet_in_dog_cat)

        token_dict = {"age": 25, "pet": "dog"}
        assert when_any_age_or_pet.evaluate(token_dict) is True

    def test_evaluate_false(self):
        numeric_token_age = NumericToken(name="age")
        age_gt_35 = Expression(numeric_token_age, Gt(35))

        string_token_pet = StringToken(name="pet")
        pet_in_dog_cat = Expression(string_token_pet, In("dog", "cat"))

        when_any_age_or_pet = WhenAny(age_gt_35, pet_in_dog_cat)

        token_dict = {"age": 25, "pet": "parrot"}
        assert when_any_age_or_pet.evaluate(token_dict) is False

    def test_recursive(self):
        numeric_token_age = NumericToken(name="age")
        age_gt_35 = Expression(numeric_token_age, operator=Gt(35))

        string_token_pet = StringToken(name="pet")
        pet_in_dog_cat = Expression(string_token_pet, In("dog", "cat"))

        string_token_ownership = StringToken(name="ownership")
        ownership_in_owned_leased = Expression(string_token_ownership, In("owned", "leased"))

        age_or_pet_condition = WhenAny(age_gt_35, pet_in_dog_cat)

        age_or_pet_and_ownership = WhenAll(
            age_or_pet_condition,
            ownership_in_owned_leased
        )

        token_dict = {"age": 40, "pet": "parrot", "ownership": "owned"}
        assert age_or_pet_and_ownership.evaluate(token_dict) is True

        token_dict = {"age": 10, "pet": "dog", "ownership": "rented"}
        assert age_or_pet_and_ownership.evaluate(token_dict) is False

        token_dict = {"age": 25, "pet": "parrot", "ownership": "owned"}
        assert age_or_pet_and_ownership.evaluate(token_dict) is False
