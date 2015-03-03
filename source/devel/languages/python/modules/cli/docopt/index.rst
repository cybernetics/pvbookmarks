

.. index::
   pair: CLI ; Docopt
   pair: cli ; Click

.. _python_docopt:

=======================
Python docopt module
=======================

.. seealso::

   - http://docopt.org/
   - https://github.com/docopt/docopt/
   - https://github.com/docopt
   - https://pypi.python.org/pypi/docopt


.. contents::
   :depth: 3
   
   
Description
============ 
   
Isn't it awesome how ``optparse`` and ``argparse`` generate help
messages based on your code?!


*Hell no!*  You know what's awesome?  It's when the option parser *is*
generated based on the beautiful help message that you write yourself!
This way you don't need to write this stupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

Pythonic argument parser, that will make you smile
docopt creates beautiful command-line interfaces

**docopt** helps you create most beautiful command-line interfaces
*easily*:

.. code:: python

    """Naval Fate.

    Usage:
      naval_fate.py ship new <name>...
      naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
      naval_fate.py ship shoot <x> <y>
      naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
      naval_fate.py (-h | --help)
      naval_fate.py --version

    Options:
      -h --help     Show this screen.
      --version     Show version.
      --speed=<kn>  Speed in knots [default: 10].
      --moored      Moored (anchored) mine.
      --drifting    Drifting mine.

    """
    from docopt import docopt


    if __name__ == '__main__':
        arguments = docopt(__doc__, version='Naval Fate 2.0')
        print(arguments)

Beat that! The option parser is generated based on the docstring above
that is passed to ``docopt`` function.  ``docopt`` parses the usage
pattern (``"Usage: ..."``) and option descriptions (lines starting
with dash "``-``") and ensures that the program invocation matches the
usage pattern; it parses options, arguments and commands based on
that. The basic idea is that *a good help message has all necessary
information in it to make a parser*.

Also, `PEP 257 <http://www.python.org/dev/peps/pep-0257/>`_ recommends
putting help message in the module docstrings.
