
.. index::
   pair: Sphinx; include
   ! include


.. _sphinx_include:

================
include
================


.. seealso::

   - http://packages.python.org/an_example_pypi_project/sphinx.html#includes



The syntax::

   .. include myfile.rst

Will 'inline' the given file.  A common convention I use is create a global
.rst file called ``global.rst`` and include that at the top of every page.

**Very useful** for links to common images or common files links, etc.



