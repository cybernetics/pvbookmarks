

.. index::
   pair: Time; PEP 0418
   pair: Python; monotonic


.. _python_time:

============
Python Time
============

.. seealso::

   -  http://www.python.org/dev/peps/pep-0418/


.. contents::
   :depth: 3


Abstract
=========

Add time.monotonic() and time.get_clock_info(name) functions to Python 3.3.


Use cases
=========

- Display the current time to a human (e.g. display a calendar or draw a wall clock):
  use system clock, i.e. time.time() or datetime.datetime.now().
- Event scheduler, timeout: time.monotonic().
- Benchmark, profiling: time.clock() on Windows, time.monotonic(), or fallback
  to time.time()


Definitions
===========

Monotonic
----------

A monotonic clock cannot go backward. It may give the same value for two close
reads depending on the clock resolution.

On Linux, CLOCK_MONOTONIC is a monotonic clock but its rate is adjusted by NTP.




