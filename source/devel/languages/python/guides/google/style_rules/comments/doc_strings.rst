.. index::
   pair: python; Doc Strings


.. _python_doc_strings:

===========
Doc Strings
===========

Python has a unique commenting style using doc strings.

**A doc string is a string that is the first statement in a package, module,
class or function**.

These strings can be extracted automatically through the __doc__ member of the
object and are used by pydoc. (Try running pydoc on your module to see how
it looks.)

Our convention for doc strings is to use the three double-quote format for
strings.

A doc string should be organized as a summary line (one physical line)
terminated by a period, question mark, or exclamation point, followed by a
blank line, followed by the rest of the doc string starting at the same cursor
position as the first quote of the first line.

There are more formatting guidelines for doc strings below.

