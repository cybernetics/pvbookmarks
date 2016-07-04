
.. index::
   pair:  doxygen; 1.8.4



.. _doxygen_1.8.4:

===========================
Doxygen 1.8.4 (19-05-2013)
===========================


.. seealso:: 

   - http://www.stack.nl/~dimitri/doxygen/changelog.html
   - http://www.stack.nl/~dimitri/doxygen/manual/changelog.html#log_1_8_4
   

.. contents::
   :depth: 3


Changes
========

- id 686384: When INLINE_SIMPLE_STRUCTS is enabled, also structs with simple typedefs will be inlined.
- Doxywizard: scrolling with mouse wheel no longer affects the values in the expert view.
- id 681733: More consistent warnings and errors. 

New features
============

- Added support for "clang assisted parsing", which allows the code to also be 
  parsed via libclang (C/C++ frontend of LLVM) and can improve the quality of 
  the syntax highting, cross-references, and call graphs, especially for template 
  heavy C++ code. To enable this feature you have to configure doxygen with the 
  --with-libclang option. Then you get two new configuration options: 
  CLANG_ASSISTED_PARSING to enable or disable parsing via clang and CLANG_OPTIONS 
  to pass additional compiler options needed to compile the files. 
  Note that enabling this feature has a significant performance penality.
- Included patch donated by Intel which adds Docbook support. This can be enabled 
  via GENERATE_DOCBOOK and the output location can be controlled using DOCBOOK_OUTPUT. 
  Docbook specific sections can be added using \docbookonly ... \enddocbookonly
- Added support for UNO IDL (interace language used in Open/Libre Office), thanks 
  to Michael Stahl for the patch.
  
Stores data gathered by doxygen in a **sqlite3** database  
----------------------------------------------------------
  
- Included patch by Adrian Negreanu which stores data gathered by doxygen in a 
  **sqlite3** database. 
  Currently still work in progress and can only be enabled using --with-sqlite3 
  during ./configure.
  
SVG
---
  
- For interactive SVG graphs, edges are now highlighted when hovered by the mouse.

Statistics
----------

- Include patch by Adrian Negreanu to show duration statistics after a run. 
  You can enable this by running doxygen with the **-d Time** option.
  
LATEX_EXTRA_FILES
------------------
  
- Included patch by Markus Geimer which adds a new option LATEX_EXTRA_FILES 
  which works similarily to HTML_EXTRA_FILES in that it copied specified files 
  to the LaTeX output directory.
  
C++11
----- 
  
- id 698223: Added support for C++11 keyword alignas


.. _dash_doxygen:

Added support for processing DocSets 
------------------------------------

- id 693178: Added support for processing DocSets with :ref:`Dash <dash>` 
  (thanks to Bogdan Popescu for the patch
  
Other
-----
  
- id 684782: Added option EXTERNAL_PAGES which can be used to determine whether 
  or not pages importated via tags will appear under related pages (similar to 
  EXTERNAL_GROUPS).
- id 692227: Added new MathJax command MATHJAX_CODEFILE which supports including 
  a file with MathJax related scripting to be inserted before the MathJax script 
  is loaded. Thanks to Albert for the patch.
- id 693537: Comments in the config file starting with ## will now be kept when 
  upgrading the file with doxygen -u (and doxygen -s -u). Thanks to Albert for the patch.
- id 693422: Adds support for Latvian (thanks to a patch by Lauris).
- Included language updates for Ukrainian, Romanian, and Korean 
