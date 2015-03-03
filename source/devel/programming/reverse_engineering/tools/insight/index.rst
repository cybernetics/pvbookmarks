
.. index::
   pair: Reverse engineering ; Insight
   ! Insight


.. _insight:

==========================
Insight
==========================

.. seealso::

   - https://insight.labri.fr/trac


.. contents::
   :depth: 3

Description
============

The Insight project is devoted to binary analysis to serve several purposes such as:

- Binary verification
- Reverse engineering
- Binary test cases extraction
- Decompilation to higher-level languages 

We aim to have a full and efficient platform to easily try out novel algorithms 
or techniques. 

For this, we provide a full C++ framework designed for Unix systems (BSD, 
Linux, MacOS X, ...) which contains a wide-spectrum binary format loaders 
(ELF, PE, Mach-O, ...), a decoder translating from assembly code (i386 and amd64 
for now others will come) into our intermediate language, an interpreter to 
execute the program over a (potentially abstract) domain and several facilities 
to simplify, manipulate or transform the graph and the expressions extracted 
from the original program.

.. warning:: The insight framework is still not feature complete and is a work 
   in progress. Yet, one can try the tool cfgrecovery in insight/tools/cfgrecovery/ 
   directory once you have compiled everything. 
   
   

