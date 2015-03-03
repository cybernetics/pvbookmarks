

.. index::
   pair: Building tool ; Pants
   ! Pants

.. _pants:

==========
Pants
==========

.. seealso::

   - https://pantsbuild.github.io/index.html



.. figure:: pants_logo.png
   :align: center
   

.. contents::
   :depth: 3
   


Welcome to the Pants build system
==================================

Pants is a build system for software projects in a variety of languages. 

It works particularly well for a source code repository that contains many 
distinct projects.


Source code
============

.. seealso::

   - https://github.com/pantsbuild/pants
   
   

Pants Conceptual Overview
=========================

Pants is a build system for software. 

It works particularly well for a source code repository that contains many 
distinct but interdependent pieces.

Pants is similar to make, maven, ant, gradle, sbt, etc.; but pants pursues 
different design goals. 

Pants optimizes for

- building multiple, dependent things from source
- building code in a variety of languages
- speed of build execution

A Pants build “sees” only the target it’s building and the transitive dependencies 
of that target. 

This approach works well for a big repository containing several things; a tool 
that builds everything would bog down.


Pants installation
==================

.. seealso::

   - https://pantsbuild.github.io/install.html


Languages
==========

.. toctree::
   :maxdepth: 3
   
   python/index
   
   
