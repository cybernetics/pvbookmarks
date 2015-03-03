

.. index::
   pair: Python ; Pyformat
   pair: Dev ; Pyformat


.. _pyformat:

====================
Pyformat
====================

.. seealso::

   - https://pypi.python.org/pypi/pyformat



Presentation
============

*pyformat* formats Python code to follow a consistent style.


Features
========

- Formats code to follow the :ref:`PEP 8 <python_pep_0008>` style guide (using autopep8_).
- Removes unused imports (using autoflake_).
- Formats docstrings to follow PEP 257 (using docformatter_).
- Makes strings all use the same type of quote where possible (using unify_).



.. _autoflake: https://github.com/myint/autoflake
.. _autopep8: https://github.com/hhatto/autopep8
.. _docformatter: https://github.com/myint/docformatter
.. _unify: https://github.com/myint/unify

Example
=======

After running::

    $ pyformat --in-place example.py

This code:

.. code-block:: python

   def launch_rocket   ():



       """Launch
   the
   rocket. Go colonize space."""

   def factorial(x):
       '''

       Return x factorial.

       This uses math.factorial.

       '''
       import math
       import re
       import os
       return math.factorial( x );
   def print_factorial(x):
       """Print x factorial"""
       print( factorial(x)  )
   def main():
       """Main
       function"""
       print_factorial(5)
       if factorial(10):
         launch_rocket()


Gets formatted into this:

.. code-block:: python

   def launch_rocket():
       """Launch the rocket.

       Go colonize space.

       """


   def factorial(x):
       """Return x factorial.

       This uses math.factorial.

       """
       import math
       return math.factorial(x)


   def print_factorial(x):
       """Print x factorial."""
       print(factorial(x))


   def main():
       """Main function."""
       print_factorial(5)
       if factorial(10):
           launch_rocket()

Installation
=============

::

    C:\projects\devtools_doc>workon pythondev
    (pythondev) C:\projects\devtools_doc>pip install pyformat
    Downloading/unpacking pyformat
    Downloading pyformat-0.3.2.tar.gz
    Running setup.py egg_info for package pyformat

    Downloading/unpacking autoflake>=0.4.2 (from pyformat)
    Downloading autoflake-0.4.2.tar.gz
    Running setup.py egg_info for package autoflake

    Downloading/unpacking autopep8>=0.9.1 (from pyformat)
    Downloading autopep8-0.9.1.tar.gz (49kB): 49kB downloaded
    Running setup.py egg_info for package autopep8

    Downloading/unpacking docformatter>=0.4 (from pyformat)
    Downloading docformatter-0.4.3.tar.gz
    Running setup.py egg_info for package docformatter

    Downloading/unpacking unify>=0.1.4 (from pyformat)
    Downloading unify-0.1.5.tar.gz
    Running setup.py egg_info for package unify

    Downloading/unpacking pyflakes>=0.7.2 (from autoflake>=0.4.2->pyformat)
    Downloading pyflakes-0.7.2.tar.gz
    Running setup.py egg_info for package pyflakes

    Requirement already satisfied (use --upgrade to upgrade): pep8>=1.4.5 in c:\users\pvergain\envs\pythondev\lib\site-
    packages (from autopep8>=0.9.1->pyformat)
    Installing collected packages: pyformat, autoflake, autopep8, docformatter, unify, pyflakes
    Running setup.py install for pyformat

    Running setup.py install for autoflake

    Running setup.py install for autopep8

    Installing autopep8-script.py script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing autopep8.exe script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing autopep8.exe.manifest script to C:\Users\pvergain\Envs\pythondev\Scripts
    Running setup.py install for docformatter

    Running setup.py install for unify

    Running setup.py install for pyflakes

    Installing pyflakes-script.py script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing pyflakes.exe script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing pyflakes.exe.manifest script to C:\Users\pvergain\Envs\pythondev\Scripts
    Successfully installed pyformat autoflake autopep8 docformatter unify pyflakes
    Cleaning up...


