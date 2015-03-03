
.. index::
   pair: python; Shebang Line


.. _python_shebang_line:

============
Shebang Line
============

Most :file:`.py` files do not need to start with a #! line.

Start the main file of a binary with ``#!/usr/bin/python``.

This line is used by the kernel to find the Python interpreter, but is ignored
by Python when importing modules.

It is only necessary on a file that will be executed directly.

