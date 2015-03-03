
.. index::
   pair: C++ ; Thread libraries (Qt concurrent)
   ! Qt concurrent 


.. _qt_concurrent:

=====================================
Qt concurrent Using a High-level API
=====================================

.. seealso::

   - http://qt-project.org/doc/qt-5.0/qtconcurrent/qtconcurrent-index.html


.. contents::
   :depth: 3



Introduction
=============

The Qt Concurrent module provides high-level functions that deal with some 
common parallel computation patterns: map, filter, and reduce. 

Unlike using QThread and QRunnable, **these functions never require the use of 
low-level threading primitives such as mutexes or semaphores**. 
Instead, they return a QFuture object which can be used to retrieve the 
functions' results when they are ready. 

QFuture can also be used to query computation progress and to pause/resume/cancel 
the computation. For convenience, QFutureWatcher enables interactions with 
QFutures via signals and slots.

Qt Concurrent's map, filter and reduce algorithms automatically distribute 
computation across all available processor cores, so applications written today 
will continue to scale when deployed later on a system with more cores.

This module also provides the QtConcurrent::run() function, which can run any 
function in another thread. However, QtConcurrent::run() only supports a subset 
of features available to the map, filter and reduce functions. 

The QFuture can be used to retrieve the function's return value and to check if 
the thread is running. 

.. warning:: However, a call to QtConcurrent::run() uses one thread only, 
   cannot be paused/resumed/canceled, and cannot be queried for progress.



Description 
===========

The ``QtConcurrent`` namespace provides high-level APIs that make it possible to 
write multi-threaded programs **without using low-level threading primitives such 
as mutexes, read-write locks, wait conditions, or semaphores**. 

Programs written with QtConcurrent automatically adjust the number of threads 
used according to the number of processor cores available. 

This means that applications written today will continue to scale when deployed 
on multi-core systems in the future.


``QtConcurrent`` includes functional programming style APIs for parallel list 
processing, including a MapReduce and FilterReduce implementation for 
shared-memory (non-distributed) systems, and **classes for managing asynchronous 
computations in GUI applications**:

- QtConcurrent::map() applies a function to every item in a container, modifying 
  the items in-place.
- QtConcurrent::mapped() is like map(), except that it returns a new container 
  with the modifications.
- QtConcurrent::mappedReduced() is like mapped(), except that the modified 
  results are reduced or folded into a single result.
- QtConcurrent::filter() removes all items from a container based on the result 
  of a filter function.
- QtConcurrent::filtered() is like filter(), except that it returns a new container 
  with the filtered results.
- QtConcurrent::filteredReduced() is like filtered(), except that the filtered 
  results are reduced or folded into a single result.
- QtConcurrent::run() runs a function in another thread.
- QFuture represents the result of an asynchronous computation.
- QFutureIterator allows iterating through results available via QFuture.
- QFutureWatcher allows monitoring a QFuture using signals-and-slots.
- QFutureSynchronizer is a convenience class that automatically synchronizes 
  several QFutures.


Random access iterators can be faster in cases where Qt Concurrent is iterating 
over a large number of lightweight items, since they allow skipping to any point 
in the container. 

In addition, using random access iterators allows Qt Concurrent to provide 
progress information trough QFuture::progressValue() and QFutureWatcher::progressValueChanged().


Qt concurrent classes
=====================

.. toctree::
   :maxdepth: 3
   
   classes/index
   
   
Qt concurrent examples
=======================

.. toctree::
   :maxdepth: 3
   
   examples/index
   
      

