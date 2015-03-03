

.. index::
   Java (JNI JavaCPP)
   Samuel Audet


.. _java_cpp:

==================
Java CPP
==================


.. seealso::

   - http://code.google.com/p/javacpp/
   - https://groups.google.com/forum/#!forum/javacpp-project
   - http://www.cs.brown.edu/courses/csci1290/results/final/sbnguyen/
   - http://www.ok.ctrl.titech.ac.jp/~saudet/
   - http://stackoverflow.com/users/523744/samuel-audet
   - http://code.google.com/p/javacv/



JavaCPP provides efficient access to native C++ inside Java, not unlike the way
some C/C++ compilers interact with assembly language.
No need to invent a whole new language, whatever Microsoft may opine about it.
Under the hood, it uses JNI, so it works with all Java implementations,
including Android. In contrast to other approaches (SWIG, JNIWrapper, Platform
Invoke, JNI Direct, JNA, JniMarshall, J/Invoke, HawtJNI, BridJ, etc.), it
supports naturally many features of the C++ language often considered
problematic, including overloaded operators, template classes and functions,
member function pointers, callback functions, nested struct definitions,
variable length arguments, nested namespaces, large data structures containing
arbitrary cycles, multiple inheritance, passing/returning by value/reference/vector,
anonymous unions, bit fields, exceptions, destructors and garbage collection.

Copyright (C) 2011 Samuel Audet <samuel.audet at gmail.com>
Personal home page: http://www.ok.ctrl.titech.ac.jp/~saudet/
Licensed under the GNU General Public License version 2 (GPLv2) with Classpath exception.


Why choosing javacpp instead swig ?
===================================

.. seealso:: http://www.cs.brown.edu/courses/csci1290/results/final/sbnguyen/


- JNI is a pain to work with
- Using SWIG to generate config file. Overhead of learning new things and
  headach when it breaks.
- Only 1 or 2 actual samples program and no instruction to create your own new projects.

After spending a few hours trying to get my SWIG config file to work, I scrapped
the whole things. If it's that hard just to get a sample program working then
it's not going to be much better than the N900.

**You have to define your method 3 times: in Java, in C++ and in SWIG. That's not fun.**


.. seealso:: http://stackoverflow.com/questions/5201292/a-good-java-wrapper-for-tapi-2

0 down vote favorite
share [fb] share [tw]


Does anyone know of a good JNI/Java wrapper for TAPI 2? ...


You could try to use one of the following tools, among others, to make the task more trivial.

- SWIG: http://www.swig.org/
- JNA: http://jna.java.net/
- JavaCPP: http://code.google.com/p/javacpp/

Being the author_ of the third there, I recommend that one :)

.. _author: http://stackoverflow.com/users/523744/samuel-audet


javacpp download
================

.. seealso:: http://code.google.com/p/javacpp/downloads/list

Put javacpp.jar into C:\Program Files\Java\jdk1.7.0\jre\lib\ext

::

    Répertoire de C:\Program Files\Java\jdk1.7.0\jre\lib\ext
    04/10/2011  13:15    <REP>          .
    04/10/2011  13:15    <REP>          ..
    03/10/2011  15:52             8 934 dnsns.jar
    04/10/2011  09:56            76 906 javacpp.jar
    04/10/2011  12:45           253 160 junit-4.10.jar
    03/10/2011  15:52         1 019 934 localedata.jar
    03/10/2011  15:52               682 meta-index
    03/10/2011  15:52            15 817 sunec.jar
    03/10/2011  15:52           198 063 sunjce_provider.jar
    03/10/2011  15:52            30 518 sunmscapi.jar
    03/10/2011  15:52           237 686 sunpkcs11.jar
    03/10/2011  15:52            68 496 zipfs.jar



.. toctree::
   :maxdepth: 4

   examples/index




