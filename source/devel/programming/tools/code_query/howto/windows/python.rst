
.. index::
   pair: Codequery; Python
   

.. codequery_python:

==========================================
How to use codequery with Python code ?
==========================================

.. seealso::

   - https://github.com/ruben2020/codequery/blob/master/windows-install/HOWTO-WINDOWS.txt


.. contents::
   :depth: 3

1. Change directory to the base folder of your source code 
==========================================================

::

    cd c:\projects\myproject\src


2. Create a cscope.files file with all the Python source files listed in it
============================================================================

::
   
    dir /b/a/s *.py    > cscope.files  


3. Create a cscope database 
===========================

::

    pycscope -i cscope.files


4. Create a ctags database
===========================

::

    ctags --fields=+i -n -R -L cscope.files


5. Run cqmakedb to create a CodeQuery database out of the cscope and ctags databases
====================================================================================

::

    cqmakedb -s .\myproject.db -c cscope.out -t tags -p
    
    
::

    cscope.out sanity check OK
    cscope.out detailed check OK
    Adding symbols ...
    Finalizing ...
    Processing ctags file ...
    Finalizing ...
    Compacting database ...    


6. Open myproject.db using the CodeQuery GUI tool 
==================================================

::

    28/06/2013  15:50            59 658 cscope.files
    28/06/2013  16:08         1 913 112 cscope.out
    28/05/2013  13:55    <DIR>          Easytest2
    28/06/2013  16:09         7 178 240 myproject.db
    28/05/2013  13:55    <DIR>          pyCL1356APlus
    28/05/2013  13:55    <DIR>          pycrypto
    28/05/2013  13:55    <DIR>          pyscard
    28/05/2013  13:55    <DIR>          pyserial
    28/06/2013  16:08         1 323 982 tags


Wild card search (* and ?) supported if Exact Match is switched off.

Or use cqsearch, the CLI-version of CodeQuery (type `cqsearch -h` for more info).

Use cqmakedb -h to get help on cqmakedb command line arguments.
