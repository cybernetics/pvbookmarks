

.. index::
   pair: Java ; Language
   ! Java


.. _java_language:
.. _java:

=============
Java language
=============

.. seealso::

   - http://fr.wikipedia.org/wiki/Java_%28langage%29
   - http://en.wikipedia.org/wiki/Java_%28programming_language%29


.. contents::
   :depth: 3

Java libraries
==============

Make your target library available to your Java program. 

There are two ways to do this:

- The preferred method is to set the jna.library.path system property to the
  path to your target library. This property is similar to java.library.path,
  but only applies to libraries loaded by JNA.
- Change the appropriate library access environment variable before launching
  the VM. This is PATH on Windows, LD_LIBRARY_PATH on Linux,
  and DYLD_LIBRARY_PATH on OSX.


Java coding standards
=====================


.. toctree::
   :maxdepth: 4

   coding_standards/index
   glossaire_java


Java bindings
==============


.. toctree::
   :maxdepth: 4

   bindings/index


Java packages
====================


.. toctree::
   :maxdepth: 6

   packages/index

Java platforms
====================


.. toctree::
   :maxdepth: 6

   platforms/index


Java translations
====================


.. toctree::
   :maxdepth: 4

   to/index


