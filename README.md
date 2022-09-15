# simple-rule-engine

A __lightweight__ yet __powerful__ rule engine that allows declarative specification of business rules and **saves tons of repeated development work**.

## Key Features
1. Ability to __declaratively__ author both Scoring and Decision Rules.
2. Ability to __version control__ rule declarations thus enabling auditing of rule changes over a period of time.
3. Ability to author **_chained rules_**. Evaluation of one rule can refer to the result of another rule, thus enabling 
modular, hierarchical rules. 

# Table of Contents
- [Why Rule Engine](#Why-Rule-Engine)
- [Concepts](#Concepts)
- [Examples](#Examples)

# Why Rule Engine?
Decision making has always been at the heart of any business. In certain industries (such as Lending), some of the decisions made are so dynamic & at a flux that programming these decisions by hand is counter-productive.

Take the example of the decision of giving someone a loan. It primarily involves ascertaining two fundamental factors:
- Ability to repay the loan.
- Intent to repay the loan.

When you start assessing a borrower based on above, you typically get all facts required to make a decision (such as Bureau score, bank statements etc.) and you will pass these facts through a decision matrix to arrive at 
- A composite score on a scale that gives an indication of _whether the borrower will repay the loan_ (**intent**)
- A recommendation of _how much loan_ should be given to the borrower. (**ability**)

The aforementioned decisions involve evaluation of multiple parameters. You simply cannot write a program to solve such complex scoring or decision problems:
 - The evaluations and/or scores will _always_ change over a period of time to adjust to business needs 
- The _rules_ will also change based on the nature of the business product.

> The simple-rule-engine solves such dynamic decision making problems by abstracting the scoring or decision making into a _framework_ and providing a standard rule template to author the rules. 

> The rules can be authored through a separate UI and stored as rule template in a database. The rule engine then _can be treated as a service_ and just by passing all the facts (a.k.a inputs), we get the the corresponding decisions or scores (output). 

> The caller of the rule engine is agnostic of the business logic behiond rule evaluation.

### Benefits

- Declarative authoring of rules. This can be done by a business analyst, rather than a developer. The developer just focuses on extracting the facts that are required to be passed into the engine.
- Versioning of rules to enable the auditing of the rule changes over a period of time.

# Concepts

The simple-rule-engine is composed of two parts:

- A Rule template which enables one to declaratively specify a rule, which can either be a Decision (or) a Score. The rule template is uniquely identified by a name.
- A parser engine which when passed with a rule name & facts, parses the rule template against the facts given and provides an output. The output can either be a score (numeric) or a decision (anything).

The simple-rule-engine allows the rules to be _“chained”_. I.e. you can build a small portion of the score as an independent rule and _“use”_ this rule in another rule. 

## Rule Declaration Language 

- At the heart of simple-serverless-rule-engine is the rule declaration language. 
- The rule declaration language supports two types of rules: Decision rule or a Score rule.  

### Score rule:

- A Score rule is composed of one or many rule sets. 
- Each rule-set computes a sub-score and is applied a weight. 
- The total score then would be the sum of all the individual scores of all the rule sets belonging to a rule.
- A rule set is composed of one or many rule rows. 
- You can ‘roughly’ think of each Rule Row as a Conditional evaluation of the facts (a.k.a antecedent) & a score based on these conditions (a.k.a consequent).
 
![Score Rule Concept](/images/score_rule.png)

### Decision rule:

- A Decision rule is always composed of only one rule set.
- A rule set is composed of one or many rule rows. 
- You can ‘roughly’ think of each Rule Row as a Conditional evaluation of the facts (a.k.a antecedent) & a score based on these conditions (a.k.a consequent).
- A decision rule always arrives at a single decision at the end of parsing.
- The decision can be anything (a numeric, a string such as YES/NO or even a JSON)

![Decision Rule Concept](/images/decision_rule.png)

### Antecedent and Consequent

- An antecedent at the core is an evaluator. It evaluates one or many facts through an operator.
- For evaluating numeric facts, a numeric operator is used. It can be one of (<=, <, >, >=, ==, <>, between, is_none)
- For evaluating string facts, a string operator is used. It can be one of (in_list, contains, is_none, equals)
- You can mix evaluation of more than one fact & combine the result with an “and” or “or” condition.
- You can perform complex evaluations involving multiple facts combining AND and OR conditions recursively in the antecedent. See [Examples](#Examples).
- The system allows a total recursion depth of 5 to allow complex evaluations.

# Examples

## A simple decision tree involving facts

### Decision matrix

| Bureau Score | Marital Status | Business Ownership | Decision
| :----------: | :----------------: | :----------------: | --------:|
| between 650 and 800        | in [Married, Unspecified]                | in [Owned by Self, Owned by Family] | GO       |

### Rule specification
```python
cibil_score_between_650_800 = NumericToken("cibil_score", Between(floor=650, ceiling=800))
marital_status_in_married_unspecified = StringToken("marital_status", In(["Married", "Unspecified"]))
business_owned_by_self_family = StringToken("business_ownership", In(["Owned by Self", "Owned by Family"]))

rule_row_decision_go = RuleRowDecision(
    WhenAll([cibil_score_between_650_800, marital_status_in_married_unspecified, business_owned_by_self_family]),
    "GO"
)
rule_set_decision = RuleSetDecision([rule_row_decision_go])

fact = dict(cibil_score=700, marital_status="Married", business_ownership="Owned by Self")
assert rule_set_decision.evaluate(fact) == "GO"
```

## A complex decision tree involving multiple AND  and OR conditions

### Decision matrix

| Applicant Age | Applicant Ownership| Business Ownership | Decision
| :----------: | :----------------: | :----------------: | --------:|
| >=35        | in [Owned by Self, Owned by Family]                | in [Owned by Self, Owned by Family] | GO       |
| >=35        | in [Owned by Self, Owned by Family]                | in [Rented] | GO       |
| >=35        | in [Rented]                | in [Owned by Self, Owned by Family] | GO       |
| >=35        | in [Rented]                | in [Rented] | NO GO       |
| <35        | in [Rented]                | in [Rented] | NO GO       |
| <35        | in [Owned by Self, Owned by Family]                | in [Rented] | NO GO       |
| <35        | in [Rented]                | in  [Owned by Self, Owned by Family] | NO GO       |
| <35        | in [Owned by Self, Owned by Family]                | in [Owned by Self, Owned by Family] | GO       |


- when the applicant age is >=35, either of applicant ownership or business ownership must be Owned.
- When the applicant age is <35, both the applicant ownership and business ownership must be Owned.


### Rule specification
```python
applicant_age_gte_35 = NumericToken("applicant_age", Gte(35))
business_owned_by_self_family = StringToken("business_ownership", In(["Owned by Self", "Owned by Family"]))
applicant_owned_by_self_family = StringToken("applicant_ownership", In(["Owned by Self", "Owned by Family"]))

rule_row_decision_go = RuleRowDecision(
    WhenAll(
        [applicant_age_gte_35, WhenAny([business_owned_by_self_family, applicant_owned_by_self_family])]
    ),
    "GO"
)
rule_set_decision = RuleSetDecision([rule_row_decision_go])

fact_go = dict(applicant_age=42, applicant_ownership="Not Owned", business_ownership="Owned by Self")
assert rule_set_decision.evaluate(fact_go) == "GO"

fact_no_go_1 = dict(applicant_age=42, applicant_ownership="Not Owned", business_ownership="Not Owned")
assert rule_set_decision.evaluate(fact_no_go_1) != "GO"

fact_no_go_2 = dict(applicant_age=25, applicant_ownership="Owned by Self", business_ownership="Owned by Self")
assert rule_set_decision.evaluate(fact_no_go_2) != "GO"
```

## A scoring rule involving multiple parameters
|Rule set Name|Weightage|
|:-----------:|:-------:|
|no_of_running_bl_pl|0.3|
|last_loan_drawn_in_months|0.3|
|no_of_bl_paid_off_successfully|0.2|
|value_of_bl_paid_successfully|0.2|

### no_of_running_bl_pl
|Condition|Score|
|:-----------:|:-------:|
|no_of_running_bl_pl >= 7 |-100|
|no_of_running_bl_pl >= 4 |-40|
|no_of_running_bl_pl >= 2 |30|
|no_of_running_bl_pl >= 0 |100|
|no_of_running_bl_pl is none |100|

### last_loan_drawn_in_months
|Condition|Score|
|:-----------:|:-------:|
|last_loan_drawn_in_months == 0 |30|
|last_loan_drawn_in_months <3 |-30|
|last_loan_drawn_in_months <= 12 |40|
|last_loan_drawn_in_months >12 |100|
|last_loan_drawn_in_months is none |100|


### no_of_bl_paid_off_successfully
|Condition|Score|
|:-----------:|:-------:|
|no_of_bl_paid_off_successfully == 0 |30|
|no_of_bl_paid_off_successfully <=2 |70|
|no_of_bl_paid_off_successfully <= 4 |85|
|no_of_bl_paid_off_successfully >4 |100|
|no_of_bl_paid_off_successfully is none |100|

### value_of_bl_paid_successfully
|Condition|Score|
|:-----------:|:-------:|
|value_of_bl_paid_successfully == 0 |30|
|value_of_bl_paid_successfully <=100000 |35|
|value_of_bl_paid_successfully <= 400000 |50|
|value_of_bl_paid_successfully > 400000 |100|
|value_of_bl_paid_successfully is none |100|

### Test Cases
|no_of_running_bl_pl|last_loan_drawn_in_months|no_of_bl_paid_off_successfully|value_of_bl_paid_successfully|Final Score|
|:-----------:|:-------:|:-----------:|:-------:|:---------:|
|8|2|0|0| -27|  
|0|13|5|none| 100|

### Rule Specification
```json
{ 
    "rule_name" : "bureau_score_loans", 
    "rule_description" : "bureau_score_loans", 
    "rule_type" : "score", 
    "rule_set" : [
        {
            "set_name" : "no_of_running_bl_pl", 
            "weight" : 0.3, 
            "rule_set_type" : "evaluate", 
            "rule_rows" : [
                {
                    "antecedent" : {
                        "token_name" : "no_of_running_bl_pl", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : ">=", 
                        "eval_value" : 7.0
                    }, 
                    "consequent" : {
                        "score" : -100.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "no_of_running_bl_pl", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : ">=", 
                        "eval_value" : 4.0
                    }, 
                    "consequent" : {
                        "score" : -40.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "no_of_running_bl_pl", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : ">=", 
                        "eval_value" : 2.0
                    }, 
                    "consequent" : {
                        "score" : 30.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "no_of_running_bl_pl", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : ">=", 
                        "eval_value" : 0.0
                    }, 
                    "consequent" : {
                        "score" : 100.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "no_of_running_bl_pl", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "is_none"
                    }, 
                    "consequent" : {
                        "score" : 100.0
                    }
                }
            ]
        }, 
        {
            "set_name" : "last_loan_drawn_in_months", 
            "weight" : 0.3, 
            "rule_set_type" : "evaluate", 
            "rule_rows" : [
                {
                    "antecedent" : {
                        "token_name" : "last_loan_drawn_in_months", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "==", 
                        "eval_value" : 0.0
                    }, 
                    "consequent" : {
                        "score" : 30.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "last_loan_drawn_in_months", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "<", 
                        "eval_value" : 3.0
                    }, 
                    "consequent" : {
                        "score" : -30.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "last_loan_drawn_in_months", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "<=", 
                        "eval_value" : 12.0
                    }, 
                    "consequent" : {
                        "score" : 40.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "last_loan_drawn_in_months", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : ">", 
                        "eval_value" : 12.0
                    }, 
                    "consequent" : {
                        "score" : 100.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "last_loan_drawn_in_months", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "is_none"
                    }, 
                    "consequent" : {
                        "score" : 100.0
                    }
                }
            ]
        }, 
        {
            "set_name" : "no_of_bl_paid_off_successfully", 
            "weight" : 0.2, 
            "rule_set_type" : "evaluate", 
            "rule_rows" : [
                {
                    "antecedent" : {
                        "token_name" : "no_of_bl_paid_off_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "==", 
                        "eval_value" : 0.0
                    }, 
                    "consequent" : {
                        "score" : 30.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "no_of_bl_paid_off_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "<=", 
                        "eval_value" : 2.0
                    }, 
                    "consequent" : {
                        "score" : 70.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "no_of_bl_paid_off_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "<=", 
                        "eval_value" : 4.0
                    }, 
                    "consequent" : {
                        "score" : 85.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "no_of_bl_paid_off_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : ">", 
                        "eval_value" : 4.0
                    }, 
                    "consequent" : {
                        "score" : 100.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "no_of_bl_paid_off_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "is_none"
                    }, 
                    "consequent" : {
                        "score" : 100.0
                    }
                }
            ]
        }, 
        {
            "set_name" : "value_of_bl_paid_successfully", 
            "weight" : 0.2, 
            "rule_set_type" : "evaluate", 
            "rule_rows" : [
                {
                    "antecedent" : {
                        "token_name" : "value_of_bl_paid_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "==", 
                        "eval_value" : 0.0
                    }, 
                    "consequent" : {
                        "score" : 30.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "value_of_bl_paid_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "<=", 
                        "eval_value" : 100000.0
                    }, 
                    "consequent" : {
                        "score" : 35.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "value_of_bl_paid_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "<=", 
                        "eval_value" : 400000.0
                    }, 
                    "consequent" : {
                        "score" : 50.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "value_of_bl_paid_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : ">", 
                        "eval_value" : 400000.0
                    }, 
                    "consequent" : {
                        "score" : 100.0
                    }
                }, 
                {
                    "antecedent" : {
                        "token_name" : "value_of_bl_paid_successfully", 
                        "token_type" : "numeric", 
                        "token_category" : "organic", 
                        "operator" : "is_none"
                    }, 
                    "consequent" : {
                        "score" : 100.0
                    }
                }
            ]
        }
    ]
}
```
