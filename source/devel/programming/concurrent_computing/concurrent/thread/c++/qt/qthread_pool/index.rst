

.. index::
   pair: Thread; QThreadPool
   ! QThreadPool


.. _qthread_pool:

=========================================================
QThreadPool and QRunnable: Reusing Threads
=========================================================


.. seealso::

   - http://doc-snapshot.qt-project.org/qt5-stable/threads-technologies.html
   - http://doc-snapshot.qt-project.org/qt5-stable/qthreadpool.html
   - :ref:`nzmqt_library`


.. contents::
   :depth: 3

Introduction
============

Creating and destroying threads frequently can be expensive. 
To reduce this overhead, existing threads can be reused for new tasks. 
QThreadPool is a collection of reuseable QThreads.

To run code in one of a QThreadPool's threads, reimplement QRunnable::run() and 
instantiate the subclassed QRunnable. Use QThreadPool::start() to put the 
QRunnable in the QThreadPool's run queue.
When a thread becomes available, the code within QRunnable::run() will execute 
in that thread.

Each Qt application has a global thread pool, which is accessible through 
QThreadPool::globalInstance(). This global thread pool automatically maintains 
an optimal number of threads based on the number of cores in the CPU. 
However, a separate QThreadPool can be created and managed explicitly.




Classes
========

.. toctree::
   :maxdepth: 3
   
   classes/index
   
   
