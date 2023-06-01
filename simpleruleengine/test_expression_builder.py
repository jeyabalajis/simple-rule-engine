from unittest import TestCase

from simpleruleengine.expression.expression_builder import ExpressionBuilder


class TestExpressionBuilder(TestCase):
    def test_build(self):
        numeric_expression = ExpressionBuilder().numeric_token("age").greater_than(40).build()
        assert numeric_expression.evaluate(dict(age=45)) is True

        cibil_score_between = ExpressionBuilder().numeric_token("cibil_score").between(650, 800).build()
        assert cibil_score_between.evaluate(dict(cibil_score=700)) is True

        marital_status_in = ExpressionBuilder().string_token("marital_status").in_list("Married", "Unspecified").build()
        assert marital_status_in.evaluate(dict(marital_status="Bachelor")) is False
