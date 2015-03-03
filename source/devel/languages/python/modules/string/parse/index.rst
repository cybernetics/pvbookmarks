
.. index::
   python modules (string parse)


.. _python_parse_module:

====================
Python parse module
====================


.. seealso::

   - http://pypi.python.org/pypi/parse/
   - http://docs.python.org/py3k/library/stdtypes.html#string-methods


Parse strings using a specification based on the Python format() syntax.

parse() is the opposite of format()

Basic usage::

    >>> from parse import *            # only exports parse() and compile()
    >>> parse("It's {}, I love it!", "It's spam, I love it!")
    <Result ('spam',) {}>
    >>> p = compile("It's {}, I love it!")
    >>> print p
    <Parser "It's {}, I love it!">
    >>> p.parse("It's spam, I love it!")
    <Result ('spam',) {}>






