

.. index::
   Java (Java Native Access Generator)
   FFI (Java Native Access)


.. _java_native_access:

==================
Java Native Access
==================

.. image:: jna_logo.jpg


.. seealso::

   - http://en.wikipedia.org/wiki/Java_Native_Access
   - http://code.google.com/p/bridj/wiki/FAQ#JNA
   - http://code.google.com/p/jnaerator/
   - http://www.javaworld.com/javaworld/jw-02-2008/jw-02-opensourcejava-jna.html
   - :ref:`python_ctypes_module`



Java Native Access provides Java programs easy access to native shared libraries
without using the `Java Native Interface`_.
JNA's design aims to provide native access in a natural way with a minimum of
effort. No boilerplate or generated glue code is required.


.. _`Java Native Interface`: http://en.wikipedia.org/wiki/Java_Native_Interface


History
=======

.. seealso:: http://www.javaworld.com/javaworld/jw-02-2008/jw-02-opensourcejava-jna.html?page=5

JNA is a project with a long history (stretching back to 1999) but it was first
released in November 2006. Since then it has been slowly gaining the attention
of developers who need to integrate native C code into Java-based projects.

JNA has also made some waves among JRuby programmers because it can be used to
work around one of JRuby's pervasive problems, lack of support for POSIX calls.
JNA has also been proposed as a solution for extending Ruby with low-level C code.

I enjoyed working with JNA and believe you will find it easier and safer to use
than JNI for accessing native code. Needless to say, there is more to JNA than
I could cover in a single article.
See the Resources section to learn more about this open source Java project.
Experiment with it and share your experiences in the discussion forum for this
series. I'll be back next month with another lesser known open source project
that could benefit your everyday Java development.



Readme
======

.. seealso:: https://github.com/twall/jna#readme

**JNA** provides Java programs easy access to native shared libraries (DLLs on Windows)
without writing anything but Java code—no JNI or native code is required.
This functionality is comparable to Windows' Platform/Invoke and Python's ctypes.
Access is dynamic at runtime without code generation.

**JNA** allows you to call directly into native functions using natural Java method
invocation. The Java call looks just like it does in native code. Most calls
require no special handling or configuration; no boilerplate or generated code
is required.

The **JNA** library uses a small native library stub to dynamically invoke native
code. The developer uses a Java interface to describe functions and structures
in the target native library. This makes it quite easy to take advantage of
native platform features without incurring the high overhead of configuring
and building JNI code for multiple platforms.

While some attention is paid to performance, correctness and ease of use take
priority.

JNA includes a platform library with many native functions already mapped as
well as a set of utility interfaces that simplify native access.


Getting started
===============

.. seealso:: https://github.com/twall/jna/blob/master/www/GettingStarted.md

Java Native Access (JNA) has a single component, jna.jar; the supporting native
library (jnidispatch) is included in the jar file. JNA is capable of extracting
and loading the native library on its own, so you don't need additional
configuration. JNA falls back to extraction if the native library is not already
installed on the local system somwhere accessible to System.loadLibrary.

The native library is also available in platform-specific jar files for use with
Java Web Start.

Begin by downloading the latest release of JNA and referencing jna.jar in your
project's CLASSPATH.

.. note:: with the Netbeans IDE simply add the jar files.

If the C header files for your library are available, you can auto-generate a
library mapping by using `Olivier Chafik's`_ excellent JNAerator_ utility.
This is especially useful if your library uses long or complicated structures
where translating by hand can be error-prone.

.. _JNAerator: http://code.google.com/p/jnaerator/
.. _`Olivier Chafik's`: http://ochafik.com/blog

Architecture
============

The JNA library uses a small native library called foreign function interface
library (libffi_) to dynamically invoke native code.
The JNA library uses native functions allowing code to load a library by name
and retrieve a pointer to a function within that library, and uses libffi
library to invoke it, all without static bindings, header files, or any compile
phase. The developer uses a Java interface to describe functions and structures
in the target native library.

**This makes it quite easy to take advantage of native platform features without
incurring the high development overhead of configuring and building JNI code.**

JNA is built and tested on Mac OS X, Microsoft Windows, FreeBSD / OpenBSD,
Solaris, and Linux. It is also possible to tweak and recompile the native build
configurations to make it work on other platforms. For example, it is known to
work on Windows Mobile, even if it is not tested for this platform by the
development team.


.. _libffi:  http://en.wikipedia.org/wiki/Libffi


Why to use JNA
==============

.. seealso:: http://stackoverflow.com/questions/1556421/use-jni-instead-of-jna-to-call-native-code

It's difficult to answer such a generic question. I suppose the most obvious
difference is that with JNI, the type conversion is implemented on the native
side of the Java/native border, while with JNA, the type conversion is
implemented in Java. If you already feel quite comfortable with programming
in C and have to implement some native code yourself, I would assume that JNI
won't seem too complex. If you are a Java programmer and only need to invoke a
third party native library, using JNA is probably the easiest path to avoid the
perhaps not so obvious problems with JNI.


.. seealso:: http://stackoverflow.com/questions/3720563/access-c-shared-library-from-java-jni-jna-cni-or-swig

Which of the following (or other) method would you recommend for accessing a
C++ shared library from Java and why?

- JNI: I hear this has a number of pitfalls and is quite the undertaking?
- SWIG: Apparently this makes using JNI easier, but I've heard it has some
  problems too?
- JNA: I could write a C interface and then use JNA with it instead, which is
  apparently significantly easier than JNI ?
- CNI: Apparently this is easier than JNI ?
- Another library: it can't be commercial and I'd prefer something that is still
  well maintained (this would throw out JNIEasy, JNative, and JACE - I think).

I'm trying to go for minimal development time and problems down the road.
Any info on pros/cons of each of these would be appreciated.


For Java->C++, I've used JNI, JNA and played with SWIG.

**JNA is the easiest to use**, but as you note, requires hand-writing a C interface
to the C++ API. **It can also be slower than JNI by an order of magnitude**.
However, I measured individual calls at a few hundred nanoseconds on one machine,
so that's unlikely to matter except in a bottleneck.

JNA redundantly specifies C function signatures, in Java. JNI can redundantly
specify Java function signatures, in C strings. Discrepancies in either can
result in unexpected runtime behavior.

I personally would use JNA unless the interface is complex enough to make
hand-writing the C interface cumbersome for you, or the individual calls are
more than a few hundred nano seconds.

This week I've been faced with such an exception -- a rich C++ interface
with many classes and methods. I've started playing with SWIG, and it's
looking promising. It's been fairly easy to use, and automatically generates
the Java bindings and C implementation. Smart pointers did take a little
extra work -- you have to instruct SWIG to instantiate the templates.

EDIT (a year later):

SWIG is amazingly powerful. It can also be more complex to set up. For simple,
thin interfaces, I'd probably consider JNA or JNI first. But SWIG is handy
for thick interfaces.

I'm a little surprised that SWIG works, given the complexity of some C++ header
files. But SWIG appears to have little difficulty.

I did have to write some SWIG typemaps and macros containing C++/JNI code.
For example, passing std::strings by reference required a custom typemap.
Transforming thrown C++ exceptions to thrown Java exceptions required a
typemap and a macro.

No changes were needed to our header files except that SWIG fully instantiated
a smart-pointer template, which had been parameterized with some classes that
did not satisfy its expectation of a default constructor.

Solution: add a few default constructors.


How does JNA performance compare to custom JNI ?
================================================

.. seealso:: https://github.com/twall/jna/blob/master/www/FrequentlyAskedQuestions.md

JNA direct mapping can provide performance near that of custom JNI. Nearly all
the type mapping features of interface mapping are available, although
automatic type conversion will likely incur some overhead.

The calling overhead for a single native call using JNA interface mapping can
be an order of magnitude (~10X) greater time than equivalent custom JNI
(whether it actually does in the context of your application is a different question).

In raw terms, the calling overhead is on the order of hundreds of microseconds
instead of tens of microseconds. Note that that's the call overhead, not the
total call time. This magnitude is typical of the difference between systems
using dynamically-maintained type information and systems where type information
is statically compiled. JNI hard-codes type information in the method invocation,
where JNA interface mapping dynamically determines type information at runtime.

You might expect a speedup of about an order of magnitude moving to JNA direct
mapping, and a factor of two or three moving from there to custom JNI.

The actual difference will vary depending on usage and function signatures.
As with any optimization process, you should determine first where you need
a speed increase, and then see how much difference there is by performing
targeted optimizations. The ease of programming everything in Java usually
outweighs small performance gains when using custom JNI.



JNA versus JNI
==============

   .. seealso::  http://mbaron.developpez.com/javase/jnijna/ (JNA versus JNI)



