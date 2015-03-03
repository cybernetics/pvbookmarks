



.. index::
   pair: Kivy ; Pyjnius
   pair: Java ; Pyjnius


.. _kivy_pyjnius:

==========================================
Pyjnius Access to Java class from Python ! 
==========================================

.. seealso:: 

   - https://github.com/kivy/pyjnius
   - http://txzone.net/2012/08/pyjnius-accessing-java-classes-from-python/
   - http://pyjnius.readthedocs.org/en/latest/
   - http://blog.tshirtman.fr/2012/11/13/debugging-python-for-android-with-gdb


Introduction
=============


Python module to access Java class as Python class, using JNI.

(Work in progress.)

Quick overview
--------------

::

    >>> from jnius import autoclass
    >>> autoclass('java.lang.System').out.println('Hello world')
    Hello world

    >>> Stack = autoclass('java.util.Stack')
    >>> stack = Stack()
    >>> stack.push('hello')
    >>> stack.push('world')
    >>> print stack.pop()
    world
    >>> print stack.pop()
    hello

Usage on desktop
----------------

You need a java JDK installed (openjdk will do), cython, and make to build it

    make

That's it! you can run the tests with

    make tests

To make sure everything is running right.

Usage with python-for-android
-----------------------------

* Get http://github.com/kivy/python-for-android
* Compile a distribution with `-m "pyjnius kivy"`
* Then, you can do this kind of things:

::

    from time import sleep
    from jnius import autoclass

    Hardware = autoclass('org.renpy.android.Hardware')
    print 'DPI is', Hardware.getDPI()

    Hardware.accelerometerEnable()
    for x in xrange(20):
        print Hardware.accelerometerReading()
        sleep(.1)

It will output something like::

    I/python  ( 5983): Android kivy bootstrap done. __name__ is __main__
    I/python  ( 5983): Run user program, change dir and execute main.py
    I/python  ( 5983): DPI is 160
    I/python  ( 5983): [0.0, 0.0, 0.0]
    I/python  ( 5983): [-0.0095768067985773087, 9.3852710723876953, 2.2218191623687744]
    I/python  ( 5983): [-0.0095768067985773087, 9.3948478698730469, 2.2218191623687744]
    I/python  ( 5983): [-0.0095768067985773087, 9.3948478698730469, 2.2026655673980713]
    I/python  ( 5983): [-0.028730420395731926, 9.4044246673583984, 2.2122423648834229]
    I/python  ( 5983): [-0.019153613597154617, 9.3852710723876953, 2.2026655673980713]
    I/python  ( 5983): [-0.028730420395731926, 9.3852710723876953, 2.2122423648834229]
    I/python  ( 5983): [-0.0095768067985773087, 9.3852710723876953, 2.1835119724273682]
    I/python  ( 5983): [-0.0095768067985773087, 9.3756942749023438, 2.1835119724273682]
    I/python  ( 5983): [0.019153613597154617, 9.3948478698730469, 2.2122423648834229]
    I/python  ( 5983): [0.038307227194309235, 9.3852710723876953, 2.2218191623687744]
    I/python  ( 5983): [-0.028730420395731926, 9.3948478698730469, 2.2026655673980713]
    I/python  ( 5983): [-0.028730420395731926, 9.3852710723876953, 2.2122423648834229]
    I/python  ( 5983): [-0.038307227194309235, 9.3756942749023438, 2.2026655673980713]
    I/python  ( 5983): [0.3926490843296051, 9.3086557388305664, 1.3311761617660522]
    I/python  ( 5983): [-0.10534487664699554, 9.4331550598144531, 2.1068975925445557]
    I/python  ( 5983): [0.26815059781074524, 9.3469638824462891, 2.3463177680969238]
    I/python  ( 5983): [-0.1149216815829277, 9.3852710723876953, 2.31758713722229]
    I/python  ( 5983): [-0.038307227194309235, 9.41400146484375, 1.8674772977828979]
    I/python  ( 5983): [0.13407529890537262, 9.4235782623291016, 2.2026655673980713]

Advanced example
----------------

When you use autoclass, it will discover all the methods and fields 
within the object, and resolve it.

For now, it can be better to declare and use only what you need.
The previous example can be done manually:

::

    from time import sleep
    from java import MetaJavaClass, JavaClass, JavaMethod, JavaStaticMethod

    class Hardware(JavaClass):
        __metaclass__ = MetaJavaClass
        __javaclass__ = 'org/renpy/android/Hardware'
        vibrate = JavaStaticMethod('(D)V')
        accelerometerEnable = JavaStaticMethod('(Z)V')
        accelerometerReading = JavaStaticMethod('()[F')
        getDPI = JavaStaticMethod('()I')
        
    # use that new class!
    print 'DPI is', Hardware.getDPI()

    Hardware.accelerometerEnable()
    for x in xrange(20):
        print Hardware.accelerometerReading()
        sleep(.1)

Support/Discussion
------------------

mailto:pyjnius-dev@googlegroups.com


Blog
====

.. seealso:: http://kivy.org/planet/2012/08/pyjnius-accessing-java-classes-from-python/


We’re pleased to announce the Pyjnius project. It’s a Python library to 
access Java classes from Python, on the desktop or on Android.

We found others libraries such as JPype or Py4j, but we weren’t happy 
with the design and the usability. Using Jython wasn’t an option either, 
because we wanted to use the library within our python for android project.

Kivy pyjnius documentation
==========================


.. seealso:: http://pyjnius.readthedocs.org



Pyjnius source code
===================

.. seealso:: 

   - https://github.com/kivy/pyjnius
