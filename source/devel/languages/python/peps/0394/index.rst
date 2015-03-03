
.. index::
   pair: PEP; 0394

.. _python_pep_0394:

====================================================
pep 0394 The "python" Command on Unix-Like Systems
====================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0394/
   - :ref:`python_argparse`
   - :ref:`python_plac_parser`



.. contents::
   :depth: 3

Abstract
========

This PEP provides a convention to ensure that Python scripts can continue to 
be portable across nix systems, regardless of the default version of the Python 
interpreter (i.e. the version invoked by the python command).

- python2 will refer to some version of Python 2.x
- python3 will refer to some version of Python 3.x
- python should refer to the same target as python2 but may refer to python3 on some bleeding edge distributions

Recommendation
==============

Unix-like software distributions (including systems like Mac OS X and Cygwin)
should install the python2 command into the default path whenever a version of
the Python 2 interpreter is installed, and the same for python3 and the Python 3
interpreter.

When invoked, python2 should run some version of the Python 2 interpreter, and
python3 should run some version of the Python 3 interpreter.

Similarly, the more general python command should be installed whenever any
version of Python is installed and should invoke the same version of Python as
either python2 or python3.

For the time being, it is recommended that python should refer to python2
(however, some distributions have already chosen otherwise; see the Rationale
and Migration Notes below).

The Python 2.x idle, pydoc, and python-config commands should likewise be
available as idle2, pydoc2, and python2-config, with the original commands
invoking these versions by default, but possibly invoking the Python 3.x
versions instead if configured to do so by the system administrator.

In order to tolerate differences across platforms, all new code that needs to
invoke the Python interpreter should not specify python, but rather should
specify either python2 or python3 (or the more specific python2.x and python3.x
versions; see the Migration Notes).

This distinction should be made in shebangs, when invoking from a shell script,
when invoking via the system() call, or when invoking in any other context.

One exception to this is scripts that are deliberately written to be source
compatible with both Python 2.x and 3.x. Such scripts may continue to use python
on their shebang line without affecting their portability.

When reinvoking the interpreter from a Python script, querying sys.executable to
avoid hardcoded assumptions regarding the interpreter location remains the
preferred approach.

These recommendations are the outcome of the relevant python-dev discussions 
in March and July 2011 and February 2012.



Impact on PYTHON* Environment Variables
=======================================

The choice of target for the python command implicitly affects a distribution's
expected interpretation of the various Python related environment variables.

The use of .pth files in the relevant site-packages folder, the "per-user site
packages" feature (see python -m site) or more flexible tools such as virtualenv
are all more tolerant of the presence of multiple versions of Python on a system
than the direct use of PYTHONPATH.









