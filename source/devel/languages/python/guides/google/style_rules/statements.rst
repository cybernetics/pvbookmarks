

.. index::
   pair: python; Statements


.. _python_statements:

========================================
Statements : only one statement per line
========================================

Generally only one statement per line.

However, you may put the result of a test on the same line as the test only
if the entire statement fits on one line. In particular, you can never do so
with try/except since the try and except can't both fit on the same line, and
you can only do so with an if if there is no else.

Yes::

    if foo: bar(foo)


No::

  if foo: bar(foo)
  else:   baz(foo)

  try:               bar(foo)
  except ValueError: baz(foo)

  try:
      bar(foo)
  except ValueError: baz(foo)
