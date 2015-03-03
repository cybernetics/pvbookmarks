

.. index::
   pair: python ; CFFI


.. _python_cffi:

====================================================================
python cffi (Foreign Function Interface for Python calling C code)
====================================================================

.. seealso:: 

   - http://cffi.readthedocs.org/


.. contents::
   :depth: 3


Version 0.1 (18 june 2012)
===========================


Hi all,

We (fijal and myself) finally released the beta-0.1 version of CFFI.

It is a(nother) simple Foreign Function Interface for Python calling C code.
I talked about it with a few python core people during the PyCon sprint; now
it's done, with a pure Python part and a compact (but still 3000 lines) piece
of C code.

The goal is for it to be simple yet as complete as possible; it can be used in
places where ctypes (say) is not applicable or only with platform-specific
difficulties, e.g. to rewrite a "_curses" module in pure Python, or access the
X libraries, etc.

Of course I'm not going to suggest that it should be part of the standard library
right now, but I do hope that over time, should it prove useful and used, I could
come back and make such a suggestion.

In any case it looks like we are going to write native and JITted PyPy support
for it, and change our pure Python "_ctypes" implementation to be based on "cffi".

As it is much more compact to support than the full _ctypes, it is also good for
Jython and IronPython.


A bientôt, Armin.


