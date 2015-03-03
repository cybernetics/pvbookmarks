

.. index::
   pair: Patsy ; Python


.. _patsy:

===========================================================================
Patsy Describing statistical models in Python
===========================================================================

.. seealso::

   - http://patsy.readthedocs.org
   - https://github.com/pydata/patsy/blob/master/doc/overview.rst
   - https://pypi.python.org/pypi/patsy/
   

.. contents::
   :depth: 3
   
   
Introduction
============

:mod:`patsy` is a Python package for describing statistical models
(especially linear models, or models that have a linear component)
and building design matrices. It is closely inspired by and compatible
with the `formula <http://cran.r-project.org/doc/manuals/R-intro.html#Formulae-for-statistical-models>`_ mini-language used in `R
<http://www.r-project.org/>`_ and `S
<https://secure.wikimedia.org/wikipedia/en/wiki/S_programming_language>`_.

For instance, if we have some variable `y`, and we want to regress it
against some other variables `x`, `a`, `b`, and the `interaction
<https://secure.wikimedia.org/wikipedia/en/wiki/Interaction_%28statistics%29>`_
of `a` and `b`, then we simply write::

  patsy.dmatrices("y ~ x + a + b + a:b", data)

and Patsy takes care of building appropriate matrices.
