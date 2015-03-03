

.. index::
   pair: Python; Virtualenv
   ! Virtualenv


.. _python_virtualenv:
.. _virtualenv:

====================
Virtual environments
====================

.. seealso::

   - https://github.com/pypa/virtualenv
   - http://www.virtualenv.org/en/latest/
   - :ref:`python_pep_0405`
   - :ref:`pydev_virtualenv`


.. contents::
   :depth: 4



Obsoleted by pyvenv
====================



Why to use python virtual environments ?
=========================================

.. seealso:: 

   - http://www.michaelpollmeier.com/eclipse-pydev-and-virtualenv/
   
   
Out of the many good reasons to use virtualenv rather than installing 
the dependencies system-wide, I found those are the most important:

- projects with different dependencies are completely isolated from each 
  other, **no bad surprises** if you install a new dependency for some 
  other project
- **no bad surprises** if your os package manager decides to update a dependency
- dependencies can be defined within the project in a **requirements file**
- ability to **quickly switch between different versions of dependencies**


Python2 and Python3 virtualenv
==============================


.. toctree::
   :maxdepth: 5

   python2/index
   python3/index


virtualenv bootstrap
==============================

.. toctree::
   :maxdepth: 3

   bootstrap/index
   
 
Virtualenv tools
==============================

.. toctree::
   :maxdepth: 3

   tools/index 

Virtualenv versions
====================

.. toctree::
   :maxdepth: 3

   versions/index
   
      


