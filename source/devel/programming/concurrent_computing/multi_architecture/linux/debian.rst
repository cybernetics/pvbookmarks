

.. index::
   pair: Debian ; Multi-Architecture


.. _multi_arch_debian:

===============================
Multi-architecture on Debian
===============================

.. seealso::

   - http://wiki.debian.org/Multiarch/HOWTO
   - http://wiki.debian.org/Multiarch/Implementation


.. contents::
   :depth: 3

What is this Multiarch ?
=========================

.. seealso::

   - :ref:`debian_wheezy`

Multiarch lets you install library packages from multiple architectures 
on the same machine. 

This is useful in various ways, but the most common is installing both 
64 and 32-bit software on the same machine and having dependencies 
correctly resolved automatically. 

In general you can have libraries of more than one architecture installed 
together and applications from one architecture or another installed as 
alternatives. 

.. note:: it does not enable multiple architecture versions of applications 
   to be installed simultaneously. 
