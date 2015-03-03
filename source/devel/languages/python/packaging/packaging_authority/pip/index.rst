

.. index::
   pair: Python tools; Pip
   pair: Chocolatey; Pip
   ! Pip


.. _pip:

====================
pip
====================

.. seealso::

   - https://pypi.python.org/pypi/pip
   - http://www.pip-installer.org
   - https://python-guide.readthedocs.org/en/latest
   - :ref:`virtualenv`
   - http://tech.marksblogg.com/better-python-package-management.html
   

.. contents::
   :depth: 3

Introduction
============


``pip`` is a tool for installing and managing Python packages, such as those 
found in the Python Package Index.

It's a replacement for easy_install.

The main website for pip is http://www.pip-installer.org.

You can also install the in-development version of pip with easy_install pip==dev.


Get pip
========

.. seealso:: http://www.pip-installer.org/en/latest/installing.html



Using get-pip
-------------

::

    $ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    $ [sudo] python get-pip.py




On windows with chocolatey
----------------------------

.. seealso::

   - http://chocolatey.org/packages/pip
   
By default, it will install the packages:

- :ref:`Virtualenv <virtualenv>`
- :ref:`Fabric <fabric>`
- :ref:`Ipython <ipython>` 
- :ref:`Django <django>`

Dependencies
+++++++++++++

- easy.install  (cinst easy.install)



Using virtualenv
----------------

The easiest way to install and use pip is with virtualenv, since every 
virtualenv has pip (and it’s dependencies) installed into it automatically.

This does not require root access or modify your system Python installation.

For instance::

    $ virtualenv my_env
    $ . my_env/bin/activate
    (my_env)$ pip install SomePackage

When used in this manner, pip will only affect the active virtual environment.

See the `virtualenv installation instructions`_.


.. _`virtualenv installation instructions`:  http://www.virtualenv.org/en/latest/#installation



Pip parameters
===============

.. toctree::
   :maxdepth: 3
   
   parameters/index
   


pip source code
================

.. seealso::

   - https://github.com/pypa/pip


Pip Usage
==========

.. toctree::
   :maxdepth: 3
   
   pip_usage
   pip_dev
   
   
Pip versions
=============

.. toctree::
   :maxdepth: 3
   
   versions/index
   
   
   
      
