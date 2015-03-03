

.. index::
   pair: Thread; QThread
   pair: QTimer; QThread
   ! QThread


.. _qthread:

=========================================================
Using QThread (Low-Level API with Optional Event Loops)
=========================================================


.. seealso::

   - http://doc-snapshot.qt-project.org/qt5-stable/threads-technologies.html
   - http://doc-snapshot.qt-project.org/qt5-stable/qthread.html
   - :ref:`nzmqt_library`


.. contents::
   :depth: 3

Introduction
============

The ``QThread`` class provides a platform-independent way to manage threads.

A QThread object manages one thread of control within the program. 

QThreads  begin executing in run(). By default, run() starts the event loop by 
calling exec() and runs a Qt event loop inside the thread.


Managing threads
=================

QThread will notifiy you via a signal when the thread is started() and finished(), 
or you can use isFinished() and isRunning() to query the state of the thread.

You can stop the thread by calling exit() or quit(). In extreme cases, you may 
want to forcibly terminate() an executing thread. However, doing so is dangerous 
and discouraged. Please read the documentation for terminate() and 
setTerminationEnabled() for detailed information.

From Qt 4.8 onwards, it is possible to deallocate objects that live in a thread 
that has just ended, by connecting the finished() signal to QObject::deleteLater().

Use wait() to block the calling thread, until the other thread has finished 
execution (or until a specified time has passed).

QThread also provides static, platform independent sleep functions: sleep(), 
msleep(), and usleep() allow full second, millisecond, and microsecond 
resolution respectively. These functions were made public in Qt 5.0.

Note: wait() and the sleep() functions should be unnecessary in general, since 
Qt is an event-driven framework. Instead of wait(), consider listening for the 
finished() signal. 

.. note:: Instead of the sleep() functions, consider using QTimer.

The static functions currentThreadId() and currentThread() return identifiers 
for the currently executing thread. The former returns a platform specific ID 
for the thread; the latter returns a QThread pointer.

To choose the name that your thread will be given (as identified by the command 
ps -L on Linux, for example), you can call setObjectName() before starting the 
thread. If you don't call setObjectName(), the name given to your thread will 
be the class name of the runtime type of your thread object (for example, 
"RenderThread" in the case of the Mandelbrot Example, as that is the name of 
the QThread subclass). 
Note that this is currently not available with release builds on Windows.



QThread articles
=================

.. toctree::
   :maxdepth: 3
   
   articles/index
   
   





