
.. index::
   pair: python ; global variables


.. _python_global_variables:


======================
Avoid global variables
======================


**Definition**
    Variables that are declared at the module level.

**Pros**
    Occasionally useful.

**Cons**
    Has the potential to change module behavior during the import, because
    assignments to module-level variables are done when the module is imported.

Decision
========

Avoid global variables in favor of class variables.

Some exceptions are:

- Default options for scripts.
- Module-level constants. For example: PI = 3.14159. Constants should be
  named using all caps with underscores; see :ref:`Naming <python_naming_guideline>`.
- It is sometimes useful for globals to cache values needed or returned by
  functions.
- If needed, globals should be made internal to the module and accessed through
  public module level functions; see :ref:`Naming <python_naming_guideline>`.


