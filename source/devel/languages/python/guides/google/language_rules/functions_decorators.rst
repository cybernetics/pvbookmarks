

.. index::
   pair: python; function decorators


.. _function_decorators_g:

===============================================
Function and Method Decorators: use judiciously
===============================================

Use decorators judiciously when there is a clear advantage.


**Definition**
    Decorators for Functions and Methods (a.k.a "the @ notation").

The most common decorators are @classmethod and @staticmethod, for converting
ordinary methods to class or static methods.

However, the decorator syntax allows for user-defined decorators as well.

Specifically, for some function my_decorator, this::

    class C(object):
        @my_decorator
        def method(self):
            # method body ...

is equivalent to::

    class C(object):
        def method(self):
            # method body ...
        method = my_decorator(method)

**Pros**
    Elegantly specifies some transformation on a method; the transformation
    might eliminate some repetitive code, enforce invariants, etc.

**Cons**
    Decorators can perform arbitrary operations on a function's arguments or
    return values, resulting in surprising implicit behavior.
    Additionally, decorators execute at import time. Failures in decorator
    code are pretty much impossible to recover from.

Decision
========


Use decorators judiciously when there is a clear advantage.

Decorators should follow the same import and naming guidelines as functions.

Decorator pydoc should clearly state that the function is a decorator.

Write unit tests for decorators.

Avoid external dependencies in the decorator itself (e.g. don't rely on files,
sockets, database connections, etc.), since they might not be available when
the decorator runs (at import time, perhaps from pychecker or other tools).

A decorator that is called with valid parameters should (as much as possible)
be guaranteed to succeed in all cases.

Decorators are a special case of "top level code" - see :ref:`main <python_main>`
for more discussion.
