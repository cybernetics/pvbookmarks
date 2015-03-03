

.. index::
   pair: python; asynchronously
   pair: python peps; pep 3148


.. _python_pep_3148:

==========================================================
PEP 3148 -- futures - execute computations asynchronously
==========================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-3148/
   - http://www.dalkescientific.com/writings/diary/archive/2012/01/19/concurrent.futures.html
   - :ref:`python_multithreading_libraries`


Abstract
========

This PEP proposes a design for a package that facilitates the evaluation of
callables using threads and processes.

Motivation
==========

Python currently has powerful primitives to construct multi-threaded and
multi-process applications but parallelizing simple operations requires a lot
of work i.e. explicitly launching processes/threads, constructing a work/results
queue, and waiting for completion or some other termination condition
(e.g. failure, timeout).

It is also difficult to design an application with a global process/thread
limit when each component invents its own parallel execution strategy.







