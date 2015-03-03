

.. index::
   pair: Data ; Graph
   pair: Tool ; Graph

.. _python_graph_tool:

========================
Python C++ Graph tools
========================


.. seealso::

   - http://projects.skewed.de/graph-tool/
   - http://projects.skewed.de/graph-tool/doc/index.html
   - http://projects.skewed.de/graph-tool/doc/quickstart.html
   - http://projects.skewed.de/graph-tool/wiki/RelatedSoftware


.. contents::
   :depth: 3

What is graph-tool ?
====================

graph-tool is an efficient python module for manipulation and statistical analysis
of graphs (a.k.a. networks).

Contrary to most other python modules with similar functionality, the core data
structures and algorithms are implemented in C++, making extensive use of
template metaprogramming, based heavily on the Boost Graph Library.

This confers a level of performance which is comparable (both in memory usage and
computation time) to that of a pure C/C++ library.


graph-tool is fast !
====================

Despite its nice, soft outer appearance of a regular python module, the core
algorithms and data structures of graph-tool are written in C++, making use of
the Boost Graph Library and template metaprogramming, with performance in mind.

Most of the time, you can expect the algorithms to run just as fast as if
graph-tool were a pure C/C++ library.

Furthermore, many algorithms are implemented in parallel using OpenMP_, which
provides excellent performance on multi-core architectures, without degrading
the performance on single-core machines.


.. _OpenMP: http://en.wikipedia.org/wiki/OpenMP

graph-tool is fully documented !
================================

Every single function in the module is documented in the docstrings and in the
online documentation_, which is full of examples.

.. _documentation:  http://projects.skewed.de/graph-tool/doc/index.html


Getting started
================

You should probably start by the `quick start guide`_, which gives a short overview
of the basic features, with some usage examples.

.. _`quick start guide`:  http://projects.skewed.de/graph-tool/doc/quickstart.html

Related software
================

See the `related software list`_, for some information of other software out there
which is somehow related to graph-tool.


.. _`related software list`:  http://projects.skewed.de/graph-tool/wiki/RelatedSoftware



