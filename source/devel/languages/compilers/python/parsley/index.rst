
.. index::
   pair: Parser ; parley


.. _python_parsley:

===================
Python Parsley
===================

.. seealso::

   - http://parsley.readthedocs.org/en/latest/tutorial.html

Parsley is a pattern matching and parsing tool for Python programmers.

Most Python programmers are familiar with regular expressions, as provided by
Python’s re module. To use it, you provide a string that describes the pattern y
ou want to match, and your input.

For example::

    >>> import re
    >>> x = re.compile("a(b|c)d+e")
    >>> x.match("abddde")
    <_sre.SRE_Match object at 0x7f587af54af8>

You can do exactly the same sort of thing in Parsley::

    >>> import parsley
    >>> x = parsley.makeGrammar("foo = 'a' ('b' | 'c') 'd'+ 'e'", {})
    >>> x("abdde").foo()
    'e'

From this small example, a couple differences between regular expressions and
Parsley grammars can be seen.



