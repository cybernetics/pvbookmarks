

.. index::
   pair: java; pyjnius


.. _pyjnius:

==================
pyjnius
==================


.. seealso::

   - http://pyjnius.readthedocs.org/en/latest/index.html


Description
============

Pyjnius is a Python library for accessing Java classes.



Example
=======


.. code-block:: python

    from jnius import autoclass

    Stack = autoclass('java.util.Stack')
    stack = Stack()
    stack.push('hello')
    stack.push('world')

    print stack.pop() # --> 'world'
    print stack.pop() # --> 'hello'

