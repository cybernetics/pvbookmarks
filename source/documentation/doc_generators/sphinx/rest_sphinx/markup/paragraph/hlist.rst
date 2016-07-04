

.. index::
   pair: sphinx ; hlist

======
hlist
======


.. seealso:: http://sphinx-doc.org/latest/markup/para.html


These directives create short paragraphs and can be used inside information
units as well as normal text:

.. rst:directive:: hlist

   This directive must contain a bullet list.  It will transform it into a more
   compact list by either distributing more than one item horizontally, or
   reducing spacing between items, depending on the builder.

   For builders that support the horizontal distribution, there is a ``columns``
   option that specifies the number of columns; it defaults to 2.  Example::

      .. hlist::
         :columns: 3

         * A list of
         * short items
         * that should be
         * displayed
         * horizontally

   .. versionadded:: 0.6
