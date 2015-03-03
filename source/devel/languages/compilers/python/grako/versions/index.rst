

.. _grako_versions:

===============================
Grako versions
===============================

.. toctree::
   :maxdepth: 3
   

2.0.0
======

- Grako no longer assumes that parsers implement the semantics. 
  A separate semantics implementation must be provided. This allows for less 
  poluted namespaces and smaller classes.
- A last_node protocol allowed the removal of all mentions of variable _e from 
  generated parsers, which are thus more readable.
- Refactored closures to be more pythonic (there are no anonymous blocks in Python!).
- Fixes to the antlr2grako example to let it convert over 6000 lines of an 
  ANTLR gramar to Grako.
- Improved rendering of grammars by grammar models.
- Now tokens accept Python escape sequences.
- Added a simple Visitor Pattern for Renderer nodes. Used it to implement diagramming.
- Create a basic diagram of a grammar if pygraphviz is available. 
  Added the --draw option to the command-line tool.



