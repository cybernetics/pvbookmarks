

.. index::
   pair: Python; 3156
   pair: PEP; 3156
   pair: Python; Asynchronous IO Support

.. _python_pep_3156:

==================================================
pep 3156 Asynchronous IO Support Rebooted
==================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-3156/
   - :ref:`async_tulip`



Abstract
=========

This is a proposal for asynchronous I/O in Python 3, starting with Python 3.3.

Consider this the concrete proposal that is missing from PEP 3153.

The proposal includes a pluggable event loop API, transport and protocol
abstractions similar to those in Twisted, and a higher-level scheduler based
on yield from (PEP 380).

A reference implementation is in the works under the code name Tulip.

The Tulip repo is linked from the References section at the end.





