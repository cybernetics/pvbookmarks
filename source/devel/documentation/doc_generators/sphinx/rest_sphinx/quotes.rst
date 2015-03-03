.. highlightlang:: rest

.. index::
   pair: Rest ; List
   pair: Definition ; List
   ! List

.. _rest_lists_and_quotes:

================
Lists 
================



.. contents::
   :depth: 3

Description
============

List markup is natural: just place an asterisk at the start of a paragraph and
indent properly.  The same goes for numbered lists; they can also be
autonumbered using a ``#`` sign::

   * This is a bulleted list.
   * It has two items, the second
     item uses two lines.

   1. This is a numbered list.
   2. It has two items too.

   #. This is a numbered list.
   #. It has two items too.

Note that Sphinx disables the use of enumerated lists introduced by alphabetic
or roman numerals, such as ::

   A. First item
   B. Second item


Nested lists
=============

Nested lists are possible, but be aware that they must be separated from the
parent list items by blank lines::

   * this is
   * a list

     * with a nested list
     * and some subitems

   * and here the parent list continues


Definition lists
=================

Definition lists are created as follows::

   term (up to a line of text)
      Definition of the term, which must be indented

      and can even consist of multiple paragraphs

   next term
      Description.


Paragraphs are quoted by just indenting them more than the surrounding
paragraphs.


list-table
==========

.. seealso::

   - :ref:`list_table`

When dealing with a **long list of items**, use ``list-tables``.

