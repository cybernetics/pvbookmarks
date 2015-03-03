

.. index::
   pair: sphinx ; download


.. _sphinx_download:

======================
download
======================

.. seealso:: http://sphinx-doc.org/latest/markup/inline.html



This role lets you link to files within your source tree that are not reST
documents that can be viewed, but files that can be downloaded.

When you use this role, the referenced file is automatically marked for
inclusion in the output when building (obviously, for HTML output only).

All downloadable files are put into the _downloads subdirectory of the output
directory; duplicate filenames are handled.

An example::

    See :download:`this example script <../example.py>`.

The given filename is usually relative to the directory the current source file
is contained in, but if it absolute (starting with /), it is taken as relative
to the top source directory.

The example.py file will be copied to the output directory, and a suitable link
generated to it.

