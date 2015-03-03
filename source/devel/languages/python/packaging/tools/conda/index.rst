
.. index::
   pair: Python; Conda
   pair: Conda; Installer
   pair: Conda; Documentation
   pair: Conda; Anaconda
   pair: Python ; Scientific packages

.. _conda_installer:

=======================
Conda installation
=======================

.. seealso::

   - http://docs.continuum.io/conda/
   - http://conda.pydata.org/docs/intro.html
   - https://groups.google.com/a/continuum.io/forum/#!forum/conda
   - https://store.continuum.io/cshop/anaconda/
   - https://python-packaging-user-guide.readthedocs.org/en/latest/platforms.html
   - :ref:`conda_installer_bis`



.. contents::
   :depth: 3


Introduction
============

The conda command is the primary interface for managing Anaconda 
installations. 

It can query and search the Anaconda package index and current Anaconda 
installation, create new Anaconda environments, and install and update 
packages into existing Anaconda environments.


Conda documentation
===================

.. seealso::

   - http://conda.pydata.org/docs/intro.html
   
   

Regarding conda
================

.. seealso::

   - https://bitbucket.org/pypa/python-packaging-user-guide/issue/37/add-a-dedicated-numpy-and-the-scientific


In terms of providing an answer to the question "Where does conda fit
in the scheme of packaging tools?", my conclusion from the thread is
that once a couple of security related issues are fixed (think PyPI
before the rubygems.org compromise for the current state of conda's
security model), and once the Python 3.3 compatibility issue is
addressed on Windows, it would be reasonable to recommend it as one of
the current options for getting hold of pre-built versions of the
scientific Python stack.

I think this is important enough to warrant a "NumPy and the
Scientific Python stack" section in the user guide (with Linux distro
packages, Windows installers and conda all discussed as options):


History
========

.. toctree::
   :maxdepth: 3
   
   2014/index
   2013/index
   
   

