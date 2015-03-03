
.. index::
   pair: Wheel ; 2014 (January)


.. _wheel_29_january_2014:

===========================
Wheel January 29th 2014
===========================

.. contents::
   :depth: 3
   

Daniel Holth dholth@gmail.com
=============================

::

    Daniel Holth dholth@gmail.com
    à:	 DistUtils mailing list <distutils-sig@python.org>
    date:	 29 janvier 2014 15:55
    objet:	 [Distutils] problems with eggs?

Here are some of the problems with eggs that I tried to solve:

- Cannot be unzipped on top of each other due to the EGG-INFO directory. 
  Wheels repeat the package name in the dist-info directory and are more like 
  their installed layout, hopefully taking all the mystery out of the format.
- The egg naming scheme doesn't let you distinguish between Python
  interpreter implementations (not an important issue at the time).
- They include .pyc and so are always [at least somewhat] Python
  version specific. Wheels don't.
- Eggs do not have categories of files. Wheel uses subdirectories of the .data/ directory, 
  and are therefore a complete replacement for most other kinds of bdist_x
- And of course wheels use .dist-info which is also something that is newer than 
  eggs, and generally try to bring the useful packaging PEP work into reality.

I remember dealing with the zipped eggs hassle, and I remember having to wait 
too long for binary packages to be uploaded to pypi as eggs when a new Python 
version was released.


Vinay Sajip
============

::


    Vinay Sajip vinay_sajip@yahoo.co.uk
    à:	 DistUtils mailing list <distutils-sig@python.org>,
    Daniel Holth <dholth@gmail.com>
    date:	 29 janvier 2014 16:07

::

    > Here are some of the problems with eggs that I tried to solve:
    [snipped]
    
    
Right, and the wheel design has addressed those issues. 

I suppose what I was after was the kinds of problems that would arise from the
importability of wheels, which seems to be causing so much fear, uncertainty and doubt :-)

Regards,

Vinay Sajip

