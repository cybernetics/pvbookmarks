

.. index::
   pair: sphinx extension; autodoc
   ! Autodoc

.. _autodoc_sphinx_extension:

===========================
autodoc sphinx extension
===========================

.. seealso::

   - http://sphinx-doc.org/ext/autodoc.html


.. index:: pair: automatic; documentation
           single: docstring

This extension can import the modules you are documenting, and pull in
documentation from docstrings in a semi-automatic way.

.. note::

   For Sphinx (actually, the Python interpreter that executes Sphinx) to find
   your module, it must be importable.  That means that the module or the
   package must be in one of the directories on :data:`sys.path` -- adapt your
   :data:`sys.path` in the configuration file accordingly.

For this to work, the docstrings must of course be written in correct
reStructuredText.  You can then use all of the usual Sphinx markup in the
docstrings, and it will end up correctly in the documentation.  Together with
hand-written documentation, this technique eases the pain of having to maintain
two locations for documentation, while at the same time avoiding
auto-generated-looking pure API documentation.
