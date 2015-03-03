

   

.. _python_packaging_1_juillet_2013:

===================================
Python packaging  1er juillet 2013
===================================

.. contents::
   :depth: 3

Courriel
========

::

    pypa-dev@googlegroups.com
    date:	 1 juillet 2013 04:36
    objet:	 RCs for pip and virtualenv
    liste de diffusion:	 pypa-dev.googlegroups.com Filtrer les messages de cette liste de diffusion



Introduction
============

Pypa

Tentative rc1's for pip and virtualenv have been tagged.  
A draft of the email I'd send out is below.  Please offer revisions and test the instructions.

Known issues to handle before a final:
  1) #1024: Daniel just submitted a pull for a wheel issue right after I tagged rc1.
  2) #1020: doc update when setuptools-0.8 is released 
  3) #1016: doc update when distribute-0.7.3 is released
  4) #1014: update docs regarding linux platform wheels being a "personal" solution
  5) #946: fix windows tests (most likely jenkins issues and not real bugs)



draft email
===========

pip and virtualenv users:

pip-1.4rc1 and virtualenv-1.10rc1 are available for testing from github.

A few highlights:

 - Added support for installing and building wheel archives.
 - virtualenv is now using the new merged setuptools, and no longer supports distribute.
 - pip now only installs stable versions by default, and offers a new --pre option to also find pre-releases.
 - Dropped support for Python 2.5.

Changelogs:

- pip: http://www.pip-installer.org/en/release-1.4/news.html
- virtualenv: http://www.virtualenv.org/en/release-1.10/news.html

Download Links
==============

pip
----

  gz: https://github.com/pypa/pip/archive/1.4rc1.tar.gz
    md5=c5f22dd158fe7648569bd90ccdb91417
  zip: https://github.com/pypa/pip/archive/1.4rc1.zip
    md5=dc9b4fd6de727d4052386126601b2fbd
    
    
virtualenv
----------

  gz: https://github.com/pypa/virtualenv/archive/1.10rc1.tar.gz
    md5=fdaffb737417966e7fe9fe9f148189a1
  zip: https://github.com/pypa/virtualenv/archive/1.10rc1.zip
    md5=ebf294329ab49b2ceb47c08b1a64a575

Installation
============

The easiest way to try them both and *not* affect your current system, is like so:
e.g. on Linux::

    $ curl -L -O https://github.com/pypa/virtualenv/archive/1.10rc1.tar.gz
    $ echo "fdaffb737417966e7fe9fe9f148189a1  1.10rc1.tar.gz" | md5sum -c
    1.10rc1.tar.gz: OK
    $ tar zxf 1.10rc1.tar.gz
    $ python virtualenv-1.10rc1/virtualenv.py myVE
    $ myVE/bin/pip --version
    
::
    
   pip 1.4rc1


Note
----

If instead, you choose to upgrade an existing pip (and setuptools), 
know this:

1) pip's wheel support requires setuptools>=0.8b2 (this will become final before pip is released final)
2) setuptools-0.8b2 is not on pypi and can be found here: https://bitbucket.org/pypa/setuptools/downloads
3) Older pip's can not currently upgrade distribute to setuptools (until distribute-0.7.3 is released on ~July-7th)
     (for more upgrade details: http://www.pip-installer.org/en/latest/installing.html#requirements)

Offering Feedback
==================

You can respond to this email, or log issues in our tracker:

- https://github.com/pypa/pip/issues?state=open
