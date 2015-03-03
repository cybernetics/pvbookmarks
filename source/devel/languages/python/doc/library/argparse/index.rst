

.. index::
   pair: Python ; Argparse


.. _python_argparse:

====================
python argparse
====================

.. seealso::

    - http://docs.python.org/py3k/library/argparse.html
    - :ref:`python_argument_parsers`
    - :ref:`python_pep_0389`


.. versionadded: 3.2


The argparse module makes it easy to write user-friendly command-line interfaces.

The program defines what arguments it requires, and argparse will figure out how
to parse those out of sys.argv.

The argparse module also automatically generates help and usage messages and
issues errors when users give the program invalid arguments.

Example
=======

The following code is a Python program that takes a list of integers and
produces either the sum or the max::

   import argparse

   parser = argparse.ArgumentParser(description='Process some integers.')
   parser.add_argument('integers', metavar='N', type=int, nargs='+',
                      help='an integer for the accumulator')
   parser.add_argument('--sum', dest='accumulate', action='store_const',
                      const=sum, default=max,
                      help='sum the integers (default: find the max)')

   args = parser.parse_args()
   print(args.accumulate(args.integers))

Assuming the Python code above is saved into a file called ``prog.py``, it can
be run at the command line and provides useful help messages::

   $ prog.py -h
   usage: prog.py [-h] [--sum] N [N ...]

   Process some integers.

   positional arguments:
    N           an integer for the accumulator

   optional arguments:
    -h, --help  show this help message and exit
    --sum       sum the integers (default: find the max)


When run with the appropriate arguments, it prints either the sum or the max of
the command-line integers::

   $ prog.py 1 2 3 4
   4

   $ prog.py 1 2 3 4 --sum
   10

If invalid arguments are passed in, it will issue an error::

   $ prog.py a b c
   usage: prog.py [-h] [--sum] N [N ...]
   prog.py: error: argument N: invalid int value: 'a'

The following sections walk you through this example.












