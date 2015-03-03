
.. index::
   Python c (f2pypy)

.. _python_f2pypy_module:

===========================
python f2pypy module
===========================

.. seealso::

   - http://www.dalkescientific.com/writings/diary/archive/2011/11/09/f2pypy.html

The above is talk and hand-waving. Code's also good. There was a PyPy sprint
this week and I decided to join in for a few days and prototype an idea I've
been thinking about: f2pypy. It's a variation of f2py which generates Python
ctypes bindings which PyPy could use to talk with shared libraries implemented
in Fortran.

At the end of several days of work, I got f2pypy to generate a Python module
based on the "fblas.pyf" code from SciPy. I could import that library in CPython
and (for the few functions I tested) get answers which matched the fblas module
in SciPy. I could also use pypy to call some of the functions, but PyPy's
"numpy" implementation is not mature enough. Its array objects don't support
the ctypes interface, so I was unable to call out to the shared library.
I could only call the scalar-based functions.

The code is definitely incomplete. Even my CPython-based tests fail some of
the the "test_blas.py" from SciPy (I don't implement "cblas" and I think one
of the tests depends on Fortran order instead of C order.) It's a proof-of-concept
which shows that this approach is definitely viable, and it shows some of the
difficulties in the approach.

My point though is that it opens new possibilites which aren't available in
NumPy. For example, suppose you want to use one of the BLAS functions in
your code. Every Mac includes a copy of BLAS as a built-in library. Instead
of making people install SciPy, what about shipping the ctypes module
description instead, and using that interface? You can ship pure Python code
and still take advantage of platform-optimized libraries!

I earlier highlighted the performance problems in CPython's ctypes interface.
But this is PyPy. They already have cross-module optimizations for Python
calling Python. There's no reason why those can't apply to ctypes-based
functions. (Or perhaps it's already there? I've not tested that.)

