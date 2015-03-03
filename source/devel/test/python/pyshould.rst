
.. index::
   pair: Test;  pyshould


.. _pyshould:

==========
pyshould
==========


.. seealso::

   - https://github.com/drslump/pyshould
   - :ref:`pyhamcrest`


.. contents::
   :depth: 3


Introduction
=============


PyShould is a Python DSL allowing to write expectations or assertions in almost
natural language.

The goal is to offer an expressive yet readable syntax to define the expectations
in detail.

Under the hood it uses the PyHamcrest library of matchers to build complex
matching predicates and offer great explanations when there is a mismatch.

Its primary use case is in unit testing, replacing the need for Python's native
assertX methods.

Its use is completely transparent to the unit testing runner used, since
mismatches are reported using the standard AssertionError.
