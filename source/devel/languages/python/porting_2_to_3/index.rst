
.. index::
   pair: python ; people
   pair: PEP; 0414



.. _porting_to_python_3:

==================
Porting to python3
==================


.. seealso::

    - https://bitbucket.org/loewis/django-3k/
    - http://docs.python.org/library/2to3.html3:http://pypi.python.org/pypi/six
    - http://python3porting.com/
    - http://tox.readthedocs.org/
    - http://docs.python.org/py3k/howto/pyporting.html
    - https://bitbucket.org/django/django/compare/features/py3k
    - http://www.python.org/dev/peps/pep-0414/



.. contents::
   :depth: 3


Pep 0414
========

.. seealso:: http://www.python.org/dev/peps/pep-0414/


That's all PEP 414 is about - lowering the friction of porting to
Python 3. Is it *necessary*? No, there are already enough successful
ports to prove that, if sufficiently motivated, porting to Python 3 is
feasible with the current toolset. However, that's the wrong question.
The right question is "Does PEP 414 make porting substantially
*easier*, by significantly reducing the volume of code that needs to
change in order to attain Python 3 compatibility?". And the answer to
*that* question is "Absolutely." Porting the web frameworks themselves
to Python 3 is only the first step in migrating those ecosystems to
Python 3, and because the web APIs exposed by those frameworks are so
heavily Unicode based this is an issue that will hit pretty much every
Python web app and library on the planet.


.. index::
   pair: Python 3; Ubuntu
   

Python 3 on ubuntu
==================

.. seealso:: https://wiki.ubuntu.com/Python/3


2 to 3 tools
=============

.. toctree::
   :maxdepth: 3
   
   tools/index
   
