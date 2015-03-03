
.. index::
   pair: Codequery; Java
   

.. codequery_java:

======================================
How to use codequery with Java code ?
======================================

.. contents::
   :depth: 3
      

1. Change directory to the base folder of your source code 
==========================================================

::

    cd c:\projects\myproject\src


2. Create a cscope.files file with all the Java source files listed in it
==========================================================================

::

    dir /b/a/s *.java > cscope.files 


3. Create a cscope database 
===========================

::

    cscope -cbR


4. Create a ctags database
===========================

::

    ctags --fields=+i -n -R -L cscope.files


5. Run cqmakedb to create a CodeQuery database out of the cscope and ctags databases
====================================================================================

::

    cqmakedb -s .\myproject.db -c cscope.out -t tags -p


6. Open myproject.db using the CodeQuery GUI tool 
==================================================

Wild card search (* and ?) supported if Exact Match is switched off.

Or use cqsearch, the CLI-version of CodeQuery (type `cqsearch -h` for more info).

Use cqmakedb -h to get help on cqmakedb command line arguments.



