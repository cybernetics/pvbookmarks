
.. index::
   pair: Tutorials ; Pydev



.. _pydev_tutorials:

=================
Pydev tutorials
=================

.. seealso::

   - :ref:`virtualenv`
   - http://pydev.org/manual_101_root.html

.. contents::
   :depth: 3


Getting started guide
=====================

.. seealso:: http://pydev.org/manual_101_root.html

First time users are strongly advised to read the `Getting started`_ guide which
explains how to properly configure PyDev

.. _`Getting started`:  http://pydev.org/manual_101_root.html


.. _pydev_virtualenv:

Eclipse, PyDev and virtualenv
=============================

.. seealso:: 

   - http://www.michaelpollmeier.com/eclipse-pydev-and-virtualenv/
   - http://www.saltycrane.com/blog/2009/05/notes-using-pip-and-virtualenv-django/


On my current Django project we just moved away from using system-wide 
installed dependencies to using virtualenv. 

The transition is pretty straight forward and there’s a couple of good 
how-tos like this one_. 

Out of the many good reasons to use virtualenv rather than installing 
the dependencies system-wide, I found those are the most important:

- projects with different dependencies are completely isolated from each 
  other, no bad surprises if you install a new dependency for some other project
- no bad surprises if your os package manager decides to update a dependency
- dependencies can be defined within the project in a requirements file
- ability to quickly switch between different versions of dependencies


.. _one:  http://www.saltycrane.com/blog/2009/05/notes-using-pip-and-virtualenv-django/

