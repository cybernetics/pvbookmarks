

.. index::
   pair: QThreadPool; Qrunnable
   ! Qrunnable


.. _qrunnable:

=========================================================
Qrunnable classes
=========================================================


.. seealso::

   - http://doc-snapshot.qt-project.org/qt5-stable/qrunnable.html


.. contents::
   :depth: 3

Description
============

The QRunnable class is the base class for all runnable objects.

The QRunnable class is an interface for representing a task or piece of code 
that needs to be executed, represented by your reimplementation of the run() function.

You can use QThreadPool to execute your code in a separate thread. 
QThreadPool deletes the QRunnable automatically if autoDelete() returns true 
(the default). 
Use setAutoDelete() to change the auto-deletion flag.

QThreadPool supports executing the same QRunnable more than once by calling 
QThreadPool::tryStart(this) from within the run() function. 
If autoDelete is enabled the QRunnable will be deleted when the last thread 
exits the run function. Calling QThreadPool::start() multiple times with the 
same QRunnable when autoDelete is enabled creates a race condition and is not 
recommended.


