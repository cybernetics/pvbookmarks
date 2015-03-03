

.. index::
   sphinx sections

===============
Sphinx Sections
===============

Section headers are created by underlining (and optionally overlining) the
section title with a punctuation character, at least as long as the text::

   =================
   This is a heading
   =================


Normally, there are no heading levels assigned to certain characters as the
structure is determined from the succession of headings.  However, for the
Python documentation, we use this convention:

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections
* ``"``, for paragraphs


Explicit Markup
===============

"Explicit markup" is used in reST for most constructs that need special
handling, such as footnotes, specially-highlighted paragraphs, comments, and
generic directives.

An explicit markup block begins with a line starting with ``..`` followed by
whitespace and is terminated by the next paragraph at the same level of
indentation.  (There needs to be a blank line between explicit markup and normal
paragraphs.  This may all sound a bit complicated, but it is intuitive enough
when you write it.)


.. index::
   sphinx directives

Directives
==========

.. seealso:: http://sphinx-doc.org/latest/domains.html#directive-rst:role

A directive is a generic block of explicit markup.  Besides roles, it is one of
the extension mechanisms of reST, and Sphinx makes heavy use of it.

Basically, a directive consists of a name, arguments, options and content. (Keep
this terminology in mind, it is used in the next chapter describing custom
directives.)  Looking at this example, ::

   .. function:: foo(x)
                 foo(y, z)
      :bar: no

      Return a line of text input from the user.

``function`` is the directive name.  It is given two arguments here, the
remainder of the first line and the second line, as well as one option ``bar``
(as you can see, options are given in the lines immediately following the
arguments and indicated by the colons).

The directive content follows after a blank line and is indented relative to the
directive start.



Footnotes
=========

For footnotes, use ``[#]_`` to mark the footnote location, and add the footnote
body at the bottom of the document after a "Footnotes" rubric heading, like so::

   Lorem ipsum [#]_ dolor sit amet ... [#]_

   .. rubric:: Footnotes

   .. [#] Text of the first footnote.
   .. [#] Text of the second footnote.

You can also explicitly number the footnotes for better context.


Comments
========

Every explicit markup block which isn't a valid markup construct (like the
footnotes above) is regarded as a comment.


Source encoding
===============

Since the easiest way to include special characters like em dashes or copyright
signs in reST is to directly write them as Unicode characters, one has to
specify an encoding:

All Python documentation source files must be in UTF-8 encoding, and the HTML
documents written from them will be in that encoding as well.


Gotchas
=======

There are some problems one commonly runs into while authoring reST documents:

* **Separation of inline markup:** As said above, inline markup spans must be
  separated from the surrounding text by non-word characters, you have to use
  an escaped space to get around that.

.. XXX more?
