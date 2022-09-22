from unittest import TestCase

from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.conditional.when_any import WhenAny
from simpleruleengine.operator.Gt import Gt
from simpleruleengine.operator.In import In
from simpleruleengine.token.NumericToken import NumericToken
from simpleruleengine.token.StringToken import StringToken


class TestWhenAny(TestCase):
    def test_evaluate_true(self):
        age_gt_35 = NumericToken(token_name="age", operator=Gt(35))
        pet_in_dog_cat = StringToken("pet", In(["dog", "cat"]))

        age_or_pet_conditional = WhenAny([age_gt_35, pet_in_dog_cat])

        _token_dict = {"age": 25, "pet": "dog"}
        assert age_or_pet_conditional.evaluate(_token_dict) is True

    def test_evaluate_false(self):
        age_gt_35 = NumericToken(token_name="age", operator=Gt(35))
        pet_in_dog_cat = StringToken("pet", In(["dog", "cat"]))

        age_or_pet_conditional = WhenAny([age_gt_35, pet_in_dog_cat])

        _token_dict = {"age": 25, "pet": "parrot"}
        assert age_or_pet_conditional.evaluate(_token_dict) is False

    def test_recursive(self):
        age_gt_35 = NumericToken(token_name="age", operator=Gt(35))
        pet_in_dog_cat = StringToken("pet", In(["dog", "cat"]))
        ownership_in_owned_leased = StringToken("ownership", In(["owned", "leased"]))

        age_or_pet_condition = WhenAny([age_gt_35, pet_in_dog_cat])

        age_or_pet_and_ownership = WhenAll([age_or_pet_condition, ownership_in_owned_leased])

        token_dict = {"age": 40, "pet": "parrot", "ownership": "owned"}
        assert age_or_pet_and_ownership.evaluate(token_dict) is True

        token_dict = {"age": 10, "pet": "dog", "ownership": "rented"}
        assert age_or_pet_and_ownership.evaluate(token_dict) is False

        token_dict = {"age": 25, "pet": "parrot", "ownership": "owned"}
        assert age_or_pet_and_ownership.evaluate(token_dict) is False
