# simple-rule-engine

A __lightweight__ yet __powerful__ rule engine that allows declarative specification of business rules and **saves tons of repeated development work**.

- This library has been utilized in authoring & evaluation of a number of complex credit decisioning, upgrade/downgrade, and lender evaulation criteria rules at [FundsCorner](https://medium.com/fundscornertech)
- This library can also be considered as a _Policy Framework_ for validating IaC (Infrastructure as Code).

[![CodeFactor](https://www.codefactor.io/repository/github/jeyabalajis/simple-rule-engine/badge)](https://www.codefactor.io/repository/github/jeyabalajis/simple-rule-engine)
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/jeyabalajis/simple-rule-engine/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/jeyabalajis/simple-rule-engine/tree/main)

## At a glance

simple-rule-engine is a Python library that enables declarative specification of decision or scoring rules.

### Example Decision matrix

| Bureau Score | Marital Status | Decision
| :----------: | :----------------: | --------:|
| between 650 and 800        | in [Married, Unspecified]                | GO |

### Rule specification

```python
from simpleruleengine.conditional.when_all import WhenAll
from simpleruleengine.expression.expression import Expression
from simpleruleengine.operator.between import Between
from simpleruleengine.operator.string_in import In
from simpleruleengine.rulerow.rule_row_decision import RuleRowDecision
from simpleruleengine.ruleset.rule_set_decision import RuleSetDecision
from simpleruleengine.token.numeric_token import NumericToken
from simpleruleengine.token.string_token import StringToken

if __name__ == "__main__":
    cibil_score_between_650_800 = Expression(
        NumericToken("cibil_score"),
        Between(floor=650, ceiling=800)
    )
    marital_status_in_married_unspecified = Expression(
        StringToken("marital_status"),
        In("Married", "Unspecified")
    )

    rule_row_decision_go = RuleRowDecision(
        WhenAll(
            cibil_score_between_650_800,
            marital_status_in_married_unspecified
        ),
        "GO"
    )
    rule_set_decision = RuleSetDecision(rule_row_decision_go)

    fact = dict(
        cibil_score=700,
        marital_status="Married"
    )
    assert rule_set_decision.evaluate(fact) == "GO"
```

## Key Features
1. Ability to __declaratively__ author both Scoring and Decision Rules. 
2. The library offers composable functional syntax that can be extended with various format adapters. See [here](https://github.com/jeyabalajis/simple-serverless-rule-engine) for an example of such an extension. 
2. Ability to __version control__ rule declarations thus enabling auditing of rule changes over a period of time.
3. Ability to author **_chained rules_**. Evaluation of one rule can refer to the result of another rule, thus enabling 
modular, hierarchical rules.

## Installation

[pypi repository](https://pypi.org/project/simpleruleengine/)

```commandline
pip install simpleruleengine==2.0.2
```

## Source Code

[simple-rule-engine GitHub Repository](https://github.com/jeyabalajis/simple-rule-engine)

# Simple Rule Engine - Motivation and Under-the-Hood

https://jeyabalajis.gitbook.io/simple-rule-engine/
