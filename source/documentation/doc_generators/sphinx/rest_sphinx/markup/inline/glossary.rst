

.. index::
   sphinx (glossary)

=========
glossary
=========

This directive must contain a reST definition-list-like markup with terms and
definitions.  The definitions will then be referencable with the
:rst:role:`term` role.  Example::

  .. glossary::

     environment
        A structure where information about all documents under the root is
        saved, and used for cross-referencing.  The environment is pickled
        after the parsing stage, so that successive runs only need to read
        and parse new and changed documents.

     source directory
        The directory which, including its subdirectories, contains all
        source files for one Sphinx project.

In contrast to regular definition lists, *multiple* terms per entry are
allowed, and inline markup is allowed in terms.  You can link to all of the
terms.  For example::

  .. glossary::

     term 1
     term 2
        Definition of both terms.

(When the glossary is sorted, the first term determines the sort order.)

.. versionadded:: 0.6
  You can now give the glossary directive a ``:sorted:`` flag that will
  automatically sort the entries alphabetically.

.. versionchanged:: 1.1
  Now supports multiple terms and inline markup in terms.
