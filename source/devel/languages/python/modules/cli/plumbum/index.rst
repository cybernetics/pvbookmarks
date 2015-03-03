

.. index::
   pair: cli ; plumbum

.. _python_plumbum:

===================================
Python plumbum : Shell Combinators
===================================

.. seealso::

   - http://plumbum.readthedocs.org/en/latest/index.html
   - https://raw.github.com/tomerfiliba/plumbum/master/README.rst

.. contents::
   :depth: 3


About
======

The original purpose of Plumbum was to enable local and remote program 
execution with ease, assuming nothing fancier than good-old SSH. 

On top of this, a file-system abstraction layer was devised, so that working 
with local and remote files would be seamless.

I’ve toyed with this idea for some time now, but it wasn’t until I had to write 
build scripts for a project I’ve been working on that I decided I’ve had it 
with shell scripts and it’s time to make it happen. 

Plumbum was born from the scraps of the Path class, which I wrote for the 
aforementioned build system, and the SshContext and SshTunnel classes that 
I wrote for RPyC. 

When I combined the two with shell combinators (because shell scripts do have 
an edge there) the magic happened and here we are.

Readme
======

.. seealso::

   - https://raw.github.com/tomerfiliba/plumbum/master/README.rst


Ever wished the wrist-handiness of shell scripts be put into a real 
programming language? 

Say hello to Plumbum Shell Combinators. 

Plumbum (Latin for lead, which was used to create pipes back in the day) 
is a small yet feature-rich library for shell script-like programs in 
Python. 
The motto of the library is "Never write shell scripts again", and thus 
it attempts to mimic the shell syntax ("shell combinators") where it 
makes sense, while keeping it all **Pythonic and cross-platform**.

This is only a teaser; the full documentation can be found at 
`Read the Docs <http://plumbum.readthedocs.org/>` .


plumbum Source code
===================

.. seealso::

   - https://github.com/tomerfiliba/plumbum
   
   



