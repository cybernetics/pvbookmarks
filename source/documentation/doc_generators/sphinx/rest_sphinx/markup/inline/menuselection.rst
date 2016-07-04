

.. index::
   pair: sphinx ; menuselection


.. _sphinx_menuselection_s:

==============================
menuselection
==============================


.. contents::
   :depth: 3


Introduction
=============

Menu selections should be marked using the menuselection role. This is used to
mark a complete sequence of menu selections, including selecting submenus and
choosing a specific operation, or any subsequence of such a sequence.

The names of individual selections should be separated by ``-->``.


Example  1
==========

For example, to mark the selection ``Start -> Programs``, use this markup::

     :menuselection:`Start --> Programs`


:menuselection:`Start --> Programs`

When including a selection that includes some trailing indicator, such as the
ellipsis some operating systems use to indicate that the command opens a dialog,
the indicator should be omitted from the selection name.



Example 2  ampersand accelerators
=================================

menuselection also supports ampersand accelerators just like :doc:`guilabel`.


::

    :menuselection:`Start --> &Programs`


:menuselection:`Start --> &Programs`

