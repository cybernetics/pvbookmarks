
.. index::
   pair: zmq; versions


.. _zmq_versions:

==================
zmq releases
==================


.. contents::
   :depth: 2
   

Introduction
=================

We maintain four branches of ZeroMQ at present:

- 2.0.x is the deprecated 2.x release, which receives user-contributed bug 
  fixes only.
- 2.1.x is the stable 2.x release, which receives downstreamed bug fixes only.
- 2.2.x is the 2.x ongoing release, which receives downstreamed bug fixes, 
  new functionality, and additional layers, e.g. czmq. This is mainly a 
  placeholder for continuing 2.x maintenance after 2.1 is frozen. 
  One goal with 2.2.x is to expand the ZeroMQ distribution package to include 
  essential core language bindings.
- 3.1.0 is the new 3.x unstable release.

2.x and 3.1 implements the same wire level protocol, ZMTP/1.0. 3.0 (deprecated) 
uses an incompatible version of ZMTP.


Releases
========

.. toctree::
   :maxdepth: 4

   4/index
   3.1/index

