
.. index::
   pair: Logging ; g2log


.. _cplusplus_g2log:

==================================================
g2log An efficient asynchronous logger using C++11
==================================================


.. seealso:: 

   - https://bitbucket.org/KjellKod/g2log/src
   - http://www.codeproject.com/Articles/288827/g2log-An-efficient-asynchronous-logger-using-Cplus


Introduction
============

``g2log`` was made to be a simple, efficient, and easy to understand asynchronous 
logger. 

The core of g2log is only a few, short files and it should be easy to modify to 
suit your needs. 

It comes with logging, design-by-contract CHECK macros, and catching and logging 
of fatal signals such as SIGSEGV (illegal memory access) and 
SIGFPE (floating point error) and more. 

It is cross-platform, tested on both Linux and Windows.

What separates g2log from other logger utilities is that it is asynchronous. 

By using the Active Object pattern g2log does the slow disk access in the 
background. 

LOG calls are asynchronous and thereby g2log gets improved application performance.

A comparison with the pseudo asynchronous Google glog (v.0.3.1) shows that g2log 
is much more efficient, especially in a worst case scenario. 
