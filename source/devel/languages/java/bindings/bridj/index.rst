

.. index::
   Java (Bridj)
   FFI (Bridj)
   Bridj


.. _java_bridj:

==========
Java Bridj
==========

.. seealso::

   - http://code.google.com/p/bridj/wiki/FAQ
   - http://ochafik.com/blog/?p=674
   - http://twitter.com/#!/ochafik
   - http://stackoverflow.com/users/316785/zolive
   - http://code.google.com/p/bridj/
   - http://code.google.com/p/bridj/wiki/CurrentState
   - https://groups.google.com/forum/#!forum/nativelibs4java


It was inspired by JNA_ but it has:

- uncompromised speed (thanks to dyncall_ and assembler optimizations)
- more features : support for C++, COM, Objective-C...
- better usability : Java 1.5+ generics, annotations...
- a liberal BSD license (GPL-compatible)


.. _dyncall: :ref:`dyncall`



Key features
============

- Dynamic C / C++ / COM interop : call C++ methods, create C++ objects
  (and subclass C++ classes from Java !)
- You never need to compile any native code : we deal with the cross-compilation
  hassle for you once and for all in BridJ ! (works on Windows, Linux, MacOS X,
  Solaris, Android...)
- Full JNAerator support : stay away from C / C++ headers !
- Small library size (~ 600 kB all included)
- Straightforward type mappings with good use of generics


.. _JNA: :ref:`java_native_access`



C++
===

.. seealso:: http://code.google.com/p/bridj/wiki/CPlusPlus


Download
========

.. seealso::

   - http://code.google.com/p/bridj/wiki/Download
   - http://code.google.com/p/bridj/downloads/list


Build
=====

.. seealso:: http://code.google.com/p/bridj/wiki/Build



Mailing list
============

.. seealso:: https://groups.google.com/forum/#!topic/nativelibs4java/


.. toctree::
   :maxdepth: 4

   dyncall/index

