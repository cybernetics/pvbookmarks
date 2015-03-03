.. index::
   pair: python; Lambda Functions


.. _python_lambda_functions:

======================================
Lambda Functions : okay for one-liners
======================================
.

**Definition**
    Lambdas define anonymous functions in an expression, as opposed to a
    statement. They are often used to define callbacks or operators for
    higher-order functions like map() and filter().

**Pros**
    Convenient.

**Cons**
    Harder to read and debug than local functions. The lack of names means
    stack traces are more difficult to understand.
    Expressiveness is limited because the function may only contain an expression.

Decision
========

Okay to use them for one-liners. If the code inside the lambda function is
any longer than 60–80 chars, it's probably better to define it as a regular
(nested) function.

For common operations like multiplication, use the functions from the operator
module instead of lambda functions.

For example, prefer operator.mul to lambda x, y: x * y.
