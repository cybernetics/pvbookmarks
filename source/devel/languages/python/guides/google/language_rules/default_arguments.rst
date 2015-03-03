
.. index::
   pair: python ; Default Argument Values


.. _python_default_argument_values:


=============================================
Default Argument Values : okay in most cases
=============================================


**Definition**
    You can specify values for variables at the end of a function's
    parameter list, e.g., def foo(a, b=0):.

If foo is called with only one argument, b is set to 0.

If it is called with two arguments, b has the value of the second argument.

**Pros**
    Often you have a function that uses lots of default values, but—rarely—you
    want to override the defaults.
    Default argument values provide an easy way to do this, without having to
    define lots of functions for the rare exceptions.
    Also, Python does not support overloaded methods/functions and default
    arguments are an easy way of "faking" the overloading behavior.

**Cons**
    Default arguments are evaluated once at module load time. This may cause
    problems if the argument is a mutable object such as a list or a dictionary.
    If the function modifies the object (e.g., by appending an item to a list),
    the default value is modified.

Decision
========

Okay to use with the following caveats:

**Do not use mutable objects as default values** in the function or method
definition.

Yes::

    def foo(a, b=None):
         if b is None:
             b = []

No::

    def foo(a, b=[]):
         ...

Calling code must use named values for arguments with a default value.

This helps document the code somewhat and helps prevent and detect interface
breakage when more arguments are added.

::

    def foo(a, b=1):
    ...

Yes::

    foo(1)
    foo(1, b=2)

No::

    foo(1, 2)
