.. index::
   pair: python; pychecker


.. _python_pychecker:


=========
pychecker
=========

.. seealso:: http://pychecker.sourceforge.net/


Run pychecker over your code.

**Definition**
    PyChecker is a tool for finding bugs in Python source code.
    It finds problems that are typically caught by a compiler for less dynamic
    languages like C and C++. It is similar to lint.

Because of the dynamic nature of Python, some warnings may be incorrect;
however, spurious warnings should be fairly infrequent.

**Pros**
    Catches easy-to-miss errors like typos, use-vars-before-assignment, etc.

**Cons**
    pychecker isn't perfect. To take advantage of it, we'll need to sometimes:

    a) Write around it
    b) Suppress its warnings
    c) Improve it or
    d) Ignore it.

Decision
========

Make sure you run pychecker on your code.

For information on how to run pychecker, see the pychecker homepage

To suppress warnings, you can set a module-level variable named __pychecker__
to suppress appropriate warnings. For example::

    __pychecker__ = 'no-callinit no-classattr'

Suppressing in this way has the advantage that we can easily search for
suppressions and revisit them.

You can get a list of pychecker warnings by doing ``pychecker --help```.

Unused argument warnings can be suppressed by using "_" as the identifier for
the unused argument or prefixing the argument name with ``unused_``.

In situations where changing the argument names is infeasible, you can mention
them at the beginning of the function. For example::

    def foo(a, unused_b, unused_c, d=None, e=None):
        (d, e) = (d, e)  # Silence pychecker
        return a

Ideally, pychecker would be extended to ensure that such "unused declarations"
were true.

