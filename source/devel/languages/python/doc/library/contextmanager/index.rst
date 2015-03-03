

.. index::
   python (contextmanager)


.. _python_contextmanager:

=====================
python contextmanager
=====================

.. seealso:: 

   - http://docs.python.org/py3k/library/stdtypes.html#context-manager-types

Python’s with statement supports the concept of a runtime context defined by a 
context manager. This is implemented using a pair of methods that allow 
user-defined classes to define a runtime context that is entered before the 
statement body is executed and exited when the statement ends.

Python defines several context managers to support easy thread synchronisation, 
prompt closure of files or other objects, and simpler manipulation of the 
active decimal arithmetic context. The specific types are not treated specially 
beyond their implementation of the context management protocol. 

See the contextlib module for some examples.

Python’s generators and the contextlib.contextmanager decorator provide a 
convenient way to implement these protocols. If a generator function is 
decorated with the contextlib.contextmanager decorator, it will return a 
context manager implementing the necessary __enter__() and __exit__() methods, 
rather than the iterator produced by an undecorated generator function.

   
contextlib module
=================

.. seealso:: http://docs.python.org/py3k/library/contextlib.html#module-contextlib

With Statement Context Managers
================================


.. seealso:: http://docs.python.org/py3k/reference/datamodel.html#context-managers 
   
   
The with statement
==================

.. seealso:: http://docs.python.org/py3k/reference/compound_stmts.html#with

The with statement is used to wrap the execution of a block with methods 
defined by a context manager (see section With Statement Context Managers). 
This allows common try...except...finally usage patterns to be encapsulated for 
convenient reuse.   
   



