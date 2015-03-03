
.. index::
   pair: Parser ; LRParsing


.. _lrparsing:

===================
Python LR Parsing
===================

.. seealso::

   - http://ace-host.stuart.id.au/russell/files/lrparsing/doc/html/
   - https://pypi.python.org/pypi/lrparsing
   - http://www.matthieuamiguet.ch/pages/compilateurs




Introduction
============

An LR(1) parser hiding behind a pythonic interface

Lrparsing provides both an LR(1) parser and a tokeniser. 

It differs from other Python LR(1) parsers in using Python expressions as 
grammars, and offers simple to use disambiguation tools.

The result is something that is powerful yet concise. 

For simple tasks this means it can be thought of as an extension to Python's 
existing re module, used when regular expressions become too cumbersome. 

For complex tasks lrparsing offers a high speed parser (very roughly 25us per 
token from string to parse tree on a desktop CPU), pre-compilation of the 
grammar and error recovery hooks so parsing can continue after an error is found.

In addition to extensive documentation it comes with a parser for Sqlite3 data 
manipulation statements and a Lua 5.2 to Python compiler as examples. 

The documentation can be read online at http://www.stuart.id.au/russell/files/lrparsing/doc/html/.


