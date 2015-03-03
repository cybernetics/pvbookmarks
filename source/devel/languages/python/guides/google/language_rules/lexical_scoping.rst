.. index::
   pair: python; Lexical Scoping


.. _python_lexical_scoping:


==============================
Lexical Scoping : okay to use
==============================



**Definition**
    A nested Python function can refer to variables defined in enclosing
    functions, but can not assign to them. Variable bindings are resolved
    using lexical scoping, that is, based on the static program text.
    Any assignment to a name in a block will cause Python to treat all
    references to that name as a local variable, even if the use precedes
    the assignment. If a global declaration occurs, the name is treated as a
    global variable.

An example of the use of this feature is::

    def get_adder(summand1):
        """Returns a function that adds numbers to a given number."""
        def adder(summand2):
            return summand1 + summand2

        return adder

**Pros**
    Often results in clearer, more elegant code. Especially comforting to
    experienced Lisp and Scheme (and Haskell and ML and …) programmers.

**Cons**
    Can lead to confusing bugs. Such as this example based on PEP-0227:

::

    i = 4
    def foo(x):
        def bar():
            print i,
        # ...
        # A bunch of code here
        # ...
        for i in x:  # Ah, i *is* local to Foo, so this is what Bar sees
            print i,
        bar()

So foo([1, 2, 3]) will print 1 2 3 3, not 1 2 3 4.

Decision
========


Okay to use.
