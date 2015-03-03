

.. index::
   pair: Python; Rose


.. _async_rose:

====================================================
Rose a PEP-3156 compatible event loop based on pyuv
====================================================


.. seealso::

   - https://github.com/saghul/rose
   - :ref:`async_rose_bis`



Overview
========

PEP-3156 is a proposal for asynchronous I/O in Python, starting with Python 3.3.

The reference implementation is codenamed "tulip" and can be found here.

Rose is an event loop implementation for Tulip based on pyuv.

Rose currently depends on pyuv master branch, you can install it by doing::

    pip install git+https://github.com/saghul/pyuv.git


Running the test suite
======================

From the toplevel directory, run::

    hg clone https://code.google.com/p/tulip/
    export PYTHONPATH=tulip/
    python runtests.py -v


