# -*- coding: utf-8 -*-
"""
Copie des données doxygen.

Les données générées par doxygen sont dans le répertoire doxygen/html

Il faut copier ces données dans le répertoire sphinx/_build/html/_downloads

Précondition: le répertoire destination doit être vide.

.. function:: copytree(src, dst[, symlinks=False[, ignore=None]])

   Recursively copy an entire directory tree rooted at *src*.  The destination
   directory, named by *dst*, must not already exist; it will be created as well
   as missing parent directories.  Permissions and times of directories are
   copied with :func:`copystat`, individual files are copied using
   :func:`copy2`.


.. function:: rmtree(path[, ignore_errors[, onerror]])

   .. index:: single: directory; deleting

   Delete an entire directory tree; *path* must point to a directory (but not a
   symbolic link to a directory).  If *ignore_errors* is true, errors resulting
   from failed removals will be ignored; if false or omitted, such errors are
   handled by calling a handler specified by *onerror* or, if that is omitted,
   they raise an exception.

"""

from shutil import copytree, rmtree


destination = '_build/html/_downloads'

# le répertoire destination doit être vide
rmtree(destination)

# copie vers le répertoire destination
copytree(src='../doxygen/html', dst=destination)
