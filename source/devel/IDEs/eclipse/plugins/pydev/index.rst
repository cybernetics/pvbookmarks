
.. index::
   pair: Eclipse ; Pydev
   pair: Django ; Pydev
   ! Pydev


.. _pydev_eclipse_plugins:

=================
Pydev plugin
=================


.. seealso::

   - http://pydev.org/index.html
   - :ref:`liclipse_fund`
   - http://pydev.blogspot.com.br/2013/05/pydev-crowdfunding-finished.html
   - http://pydev.org/manual_101_root.html


.. figure:: pydev_banner2.gif
   :align: center

.. contents::
   :depth: 3

What is PyDev ?
===============

PyDev is a Python IDE for Eclipse, which may be used in Python, Jython and
IronPython development.

It comes with many goodies such as:

- Django integration
- Code completion
- Code completion with auto import
- Syntax highlighting
- Code analysis
- Go to definition
- Refactoring
- Mark occurrences
- Debugger
- Remote debugger
- Tokens browser
- Interactive console
- Unittest integration


Feature matrix
==============

.. seealso:: 

   - http://pydev.org/manual_adv_features.html

For more details on the provided features, check the `Features Matrix`_.

.. _`Features Matrix`: http://pydev.org/manual_adv_features.html


PyDev installation
===================

.. toctree::
   :maxdepth: 3
   
   install/index
   

PyDev and Django
================

.. seealso:: http://pydev.org/manual_adv_django.html

Pre-requisites
---------------

To get started with Django in PyDev, the pre-requisite is that Django is 
installed in the Python / Jython / IronPython interpreter you want to use 
(so, "import django" must properly work – if you're certain that Django 
is there and PyDev wasn't able to find it during the install process, you 
must go to the interpreter configuration and reconfigure your interpreter 
so that PyDev can detect the change you did after adding Django).

If you don't have Django installed, follow the steps from http://www.djangoproject.com/.

Note that this tutorial won't teach you Django. It'll only show how the 
Django integration is available in PyDev, so, if you're not familiar 
with Django, it's useful to learn a bit about how it works and then use 
this help to know how the PyDev Django integration can help you. 


Pydev versions
==============

.. toctree::
   :maxdepth: 3
   
   versions/index
   
   
Pydev tutorials
================

.. toctree::
   :maxdepth: 3
   
   tutorials   
   
Pydev tips
================

.. toctree::
   :maxdepth: 3
   
   tips/index
         






