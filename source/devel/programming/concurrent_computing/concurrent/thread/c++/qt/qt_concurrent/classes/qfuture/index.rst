
.. index::
   pair: Qt concurrent ; Classes (QFuture)
   pair: Asynchronous computation; QFuture 
   ! QFuture


.. _qfuture_class:

=====================
QFuture class
=====================

.. seealso::

   - http://qt-project.org/doc/qt-5.0/qtcore/qfuture.html
   

.. contents::
   :depth: 3

Detailed Description
======================

The ``QFuture class`` represents the result of an asynchronous computation.

To start a computation, use one of the APIs in the Qt Concurrent framework.


QFuture also offers ways to interact with a runnning computation. 

For instance, the computation can be canceled with the cancel() function. 
To pause the computation, use the setPaused() function or one of the pause(), 
resume(), or togglePaused() convenience functions. 

.. warning:: Be aware that not all asynchronous computations can be canceled or 
   paused. For example, the future returned by QtConcurrent::run() cannot be 
   canceled; but the future returned by QtConcurrent::mappedReduced() can.


