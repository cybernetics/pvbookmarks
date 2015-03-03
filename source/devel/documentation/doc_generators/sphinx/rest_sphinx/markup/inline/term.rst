

.. index::
   pair: sphinx ; term


.. _sphinx_term:

=====================
term (very important)
=====================

.. seealso:: http://sphinx-doc.org/latest/markup/inline.html


**Reference to a term in the glossary.**

The glossary is created using the ``glossary`` directive containing a definition
list with terms and definitions.

It does not have to be in the same file as the ``term`` markup, for example the
Python docs have one global glossary in the ``glossary.rst`` file.

If you use a term that's not explained in a glossary, you'll get a warning
during build.


Example::

    See :term:`Sphinx`


See :term:`Sphinx`

