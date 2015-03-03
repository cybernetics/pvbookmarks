



.. _setuptools_0.7.0:

===================================
Setuptools 0.7.0
===================================


.. contents::
   :depth: 3

Introduction
=============

**Merged Setuptools and Distribute**

See docs/merge.txt for details.

Added several features that were slated for setuptools 0.6c12:

Index URL now defaults to HTTPS
================================

Added experimental environment marker support
=============================================

Now clients may designate a :ref:`PEP-426 <python_pep_0426>` environment 
marker for "extra" dependencies. 

Setuptools uses this feature in setup.py for optional SSL and certificate 
validation support on older platforms. 

Based on Distutils-SIG discussions, the syntax is somewhat tentative. 

There should probably be a PEP with a firmer spec before the feature 
should be considered suitable for use.


Added support for SSL certificate validation 
=============================================

Added support for SSL certificate validation when installing packages 
from an HTTPS service.

