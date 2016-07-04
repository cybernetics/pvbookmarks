

.. index::
   pair: sphinx ; conf.py


.. _conf.py:

========================
:file:`conf.py` Examples
========================

.. seealso::

  - http://sphinx-doc.org/latest/config.html?highlight=conf#conf

The configuration directory must contain a file named :file:`conf.py`.
This file (containing Python code) is called the "build configuration file" and
contains all configuration needed to customize Sphinx input and output behavior.

The configuration file is executed as Python code at build time (using
:func:`execfile`, and with the current directory set to its containing
directory), and therefore can execute arbitrarily complex code.

Sphinx then reads simple names from the file's namespace as its configuration.


pypi Example
============

.. seealso::

   - http://packages.python.org/an_example_pypi_project/sphinx.html#conf-py


In your ``doc/source`` directory is now a python file called ``conf.py``.

This is the file that controls the basics of how sphinx runs when you run a
build.  Here you can do this like:

   *  Change the version/release number by setting the ``version`` and ``release``
      variables.

   *  Set the project name and author name.

   *  Setup a project logo.

   *  Set the default style to ``sphinx`` or ``default``.  Default is what
      the standard python docs use.

and much much more.

Browsing through this file will give you an understanding of the basics.


Exclude patterns
================

.. toctree::
   :maxdepth: 4

   exclude_patterns






