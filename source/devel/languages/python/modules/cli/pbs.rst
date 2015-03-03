

.. index::
   pair: cli ; pbs
   pair: cli ; pbs



.. _python_pbs:
.. _python_sh:

======================================
Python ``sh`` module (previously pbs)
======================================

.. seealso::

   - https://amoffat.github.io/sh/#
   - https://github.com/amoffat/sh
   - :ref:`python_sarge`


.. contents::
   :depth: 3

Description
============


sh (previously [pbs](http://pypi.python.org/pypi/pbs)) is a full-fledged
subprocess interface for Python 2.6 - 3.2
that allows you to call any program as if it were a function::

    from sh import ifconfig
    print ifconfig("eth0")

    sh is not a collection of system commands implemented in Python.

    # Installation

        $> pip install sh

    # Complete documentation @ http://amoffat.github.com/sh






