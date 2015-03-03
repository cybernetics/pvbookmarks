
.. index::
   pair: python; Whitespace

.. _python_whitespace:

===========
Whitespace
===========

Follow standard typographic rules for the use of spaces around punctuation.

No whitespace inside parentheses, brackets or braces.

Yes::

    spam(ham[1], {eggs: 2}, [])

No::

    spam( ham[ 1 ], { eggs: 2 }, [ ] )

No whitespace before a comma, semicolon, or colon.

Do use whitespace after a comma, semicolon, or colon except at the end of the
line.

Yes::

     if x == 4:
         print x, y
     x, y = y, x

No::

    if x == 4 :
         print x , y
     x , y = y , x

No whitespace before the open paren/bracket that starts an argument list,
indexing or slicing.

Yes::

    spam(1)

No::

    spam (1)

Yes::

    dict['key'] = list[index]

No::

    dict ['key'] = list [index]

Surround binary operators with a single space on either side for assignment (=),
comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), and Booleans
(and, or, not).

Use your better judgment for the insertion of spaces around arithmetic operators
but always be consistent about whitespace on either side of a binary operator.

Yes::

    x == 1

No::

    x<1

Don't use spaces around the '=' sign when used to indicate a keyword argument
or a default parameter value.

Yes::

    def complex(real, imag=0.0): return magic(r=real, i=imag)

No::

    def complex(real, imag = 0.0): return magic(r = real, i = imag)

Don't use spaces to vertically align tokens on consecutive lines, since it
becomes a maintenance burden (applies to :, #, =, etc.):

Yes::

  foo = 1000  # comment
  long_name = 2  # comment that should not be aligned

  dictionary = {
      "foo": 1,
      "long_name": 2,
      }

No::

  foo       = 1000  # comment
  long_name = 2     # comment that should not be aligned

  dictionary = {
      "foo"      : 1,
      "long_name": 2,
      }
