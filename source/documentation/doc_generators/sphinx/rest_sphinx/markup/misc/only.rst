

.. index::
   pair: Sphinx ; only

.. _sphinx_only:

=======================================
only : including content based on tags
=======================================


.. contents::
   :depth: 3

Description
===========


.. rst:directive:: .. only:: <expression>

   Include the content of the directive only if the *expression* is true.  The
   expression should consist of tags, like this::

      .. only:: html and draft

   Undefined tags are false, defined tags (via the ``-t`` command-line option or
   within :file:`conf.py`) are true.  Boolean expressions, also using
   parentheses (like ``html and (latex or draft)``) are supported.

   The format of the current builder (``html``, ``latex`` or ``text``) is always
   set as a tag.

   .. versionadded:: 0.6


Example1
=========

in conf.py
----------

.. seealso::  

   - https://groups.google.com/forum/#!topic/sphinx-users/uUmSCiK-UtU

::

    # tags.add('student')
    # tags.add('stagiaire')
    tags.add('prof')



In a .rst file
---------------


::

    .. only prof
    
        Solution du problème
        



