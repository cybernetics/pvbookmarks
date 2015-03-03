
.. index::
   pair: python; Generators


.. _python_generators_g:

=========================
Use generators as needed
=========================


**Definition**
    A generator function returns an iterator that yields a value each time it
    executes a yield statement. After it yields a value, the runtime state of
    the generator function is suspended until the next value is needed.

**Pros**
    Simpler code, because the state of local variables and control flow are
    preserved for each call. A generator uses less memory than a function that
    creates an entire list of values at once.

**Cons**
    None.

Decision
========

Fine. Use "Yields:" rather than "Returns:" in the doc string for generator
functions.


