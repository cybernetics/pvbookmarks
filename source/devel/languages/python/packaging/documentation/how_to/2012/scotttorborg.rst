

.. index::
   pair: Python ; Packaging (Howto, 2012)


.. _howto_packaging_python_scott_2012:

=======================================================
How to package your python code (scotttorborg, 2012)
=======================================================

.. seealso::

   - http://www.scotttorborg.com/python-packaging/index.html

This tutorial aims to put forth an opinionated and specific pattern to make 
trouble-free packages for community use. 

It doesn't describe the *only* way of doing things, merely one specific approach 
that works well.

In particular, packages should make it easy:

* To install with ``pip`` or ``easy_install``.
* To specify as a dependency for another package.
* For other users to download and run tests.
* For other users to work on and have immediate familiary with the basic 
  directory strucuture.
* To add and distribute documentation.

We'll walk through the basic steps of building up a contrived package **funniest** 
to support these things.


.. note::

   At this time, this documentation focuses on Python 2.x only, and may not be *as* 
   applicable to packages targeted to Python 3.x.

