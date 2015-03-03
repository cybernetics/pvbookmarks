.. index::
   pair: python; Nested/Local/Inner Classes and Functions


.. _python_nested_functions_g:


=================================================
Nested/Local/Inner Classes and Functions are fine
=================================================

Nested/local/inner classes and functions are fine.

**Definition**
    A class can be defined inside of a method, function, or class.


A function can be defined inside a method or function. Nested functions have
read-only access to variables defined in enclosing scopes.

**Pros**
    Allows definition of utility classes and functions that are only used
    inside of a very limited scope. Very ADT-y.

**Cons**
    Instances of nested or local classes cannot be pickled.

Decision
========


They are fine.
