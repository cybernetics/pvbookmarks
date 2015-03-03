


.. index::
   pair: Building tool ; Waf
   ! Waf


.. _waf_building_tool:

===
Waf
===

.. seealso::
  
   - https://code.google.com/p/waf/
   - https://fr.wikipedia.org/wiki/Waf_%28logiciel%29


.. figure:: waf_logo.png
   :align: center
   

Description
============

Waf is a Python-based framework for configuring, compiling and installing applications. 

Here are perhaps the most important features of Waf:

- Automatic build order: the build order is computed from input and output files, 
  among others
- Automatic dependencies: tasks to execute are detected by hashing files and commands
- Performance: tasks are executed in parallel automatically, the startup time 
  is meant to be fast (separation between configuration and build)
- Flexibility: new commands and tasks can be added very easily through subclassing, 
  bottlenecks for specific builds can be eliminated through dynamic method replacement
- Extensibility: though many programming languages and compilers are already 
  supported by default, many others are available as extensions
- IDE support: Eclipse, Visual Studio and Xcode project generators (waflib/extras/)
- Documentation: the application is based on a robust model documented in 
  The Waf book and in the API docs
- Python compatibility: cPython 2.4 to 3.4, Jython 2.5, IronPython, and Pypy 

Waf is used in particular by innovative companies such as Avalanche studios. 

In the open-source world, Waf is used by a few projects such as Samba. Learn 
more about Waf by reading The Waf book. 

