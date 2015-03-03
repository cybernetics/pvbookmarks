

.. index::
   pair: Setuptools; 0.8


.. _setuptools_0.8:

===============================================
Setuptools 0.8 versions (5 juillet 2013 20:05)
===============================================


.. contents::
   :depth: 3

Announce
========

::

    Jason R. Coombs <jaraco@jaraco.com>
    à:   "distutils-sig@python.org" <distutils-sig@python.org>,
     pypa-dev <pypa-dev@googlegroups.com>
    date:    5 juillet 2013 20:05
    objet:   Setuptools 0.8 and Distribute 0.7.3 (legacy wrapper) now released


The PyPA is excited to announce the public release of Setuptools 0.8. 

This release of setuptools provides no additional functionality over 
Setuptools 0.7.x except that it no longer requires 2to3 to build/install 
on Python 3. 

What this means for packaging is that tools like pip and virtualenv can now 
invoke setuptools directly on all supported Python versions (currently 2.4+). 

This build enables more natural upgrades and helps address many of the bugs 
that the 2to3 conversion process triggered.

Additionally, Distribute 0.7.3 has also been released to PyPI. 

Distribute 0.7 was designed to ease the upgrade process from Distribute 0.6.x 
to Setuptools 0.7. 

This new version, 0.7.3, is a re-release of the legacy wrapper 0.7, but 
additionally bundles the Setuptools 0.8 code for the purposes of bootstrapping 
the upgrade. 

This version specifically eases upgrades on systems running older systems. 
Now, one can readily upgrade any environment with Distribute 0.6 by simply 
upgrading (using pip or easy_install) to Distribute 0.7.3, which will replace 
the ‘distribute’ package with an empty shell leaving setuptools >= 0.7 
(probably 0.8) installed.


Enjoy, and please report any issues with either of these packages at the 
Setuptools project page (https://bitbucket.org/pypa/setuptools).
