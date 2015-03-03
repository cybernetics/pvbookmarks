
.. index::
   pair: Firmware; Binwalk
   pair: Reverse engineering; Binwalk



.. _binwalk:

==============
Binwalk
==============

.. seealso::

   - http://code.google.com/p/binwalk/
   - http://code.google.com/p/binwalk/source/browse/trunk/docs/README


.. contents::
   :depth: 3
   
About
======

Binwalk is a firmware analysis tool designed to assist in the analysis, 
extraction, and reverse engineering of firmware images and other binary 
blobs. 

It is simple to use, fully scriptable, and can be easily extended via 
custom signatures, extraction rules, and plugin modules.

Binwalk supports various types of analysis useful for inspecting and 
reverse engineering firmware, including:

- Embedded file identification and extraction
- Executable code identification
- Type casting
- Entropy analysis and graphing
- "Smart" strings analysis 

Binwalk's file signatures are (mostly) compatible with the magic signatures 
used by the Unix file utility, and include customized/improved signatures 
for files that are commonly found in firmware images such as 
compressed/archived files, firmware headers, kernels, bootloaders, 
filesystems, etc. 


Source code
===========

.. seealso::

   - http://code.google.com/p/binwalk/source/browse/#svn%2Ftrunk%2Fsrc%2Fbinwalk
   - http://www.devttys0.com/2013/02/binwalk-v1-0-now-with-python/
   
   
   
