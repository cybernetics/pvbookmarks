
.. index::
   pair: python; Line length


.. _python_line_length:


===================================================
Line length : maximum line length is 80 characters
===================================================

**Maximum line length is 80 characters**.

**Exception**
    lines importing modules may end up longer than 80 characters.

Make use of Python's implicit line joining inside parentheses, brackets and
braces.

If necessary, you can add an extra pair of parentheses around an expression.

Yes::

    fooBar(self, width, height, color='black', design=None, x='foo',
           emphasis=None, highlight=0)

    if ((width == 0) and (height == 0)
        and (color == 'red') and (emphasis == 'strong')):

When a literal string won't fit on a single line, use parentheses for implicit
line joining:

    x = ('This will build a very long long '
         'long long long long long long string')

Make note of the indentation of the elements in the line continuation examples
above; see the :ref:`indentation section <python_indentation>` for explanation.
