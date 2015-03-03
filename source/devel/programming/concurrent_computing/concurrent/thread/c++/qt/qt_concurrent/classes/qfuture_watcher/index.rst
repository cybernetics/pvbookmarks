
.. index::
   pair: Qt concurrent ; Classes (QFuture watcher)
   pair: Asynchronous computation; QFuture watcher
   pair: QFutureWatcher ; cancel()
   ! QFuture watcher


.. _qfuture_watcher_class:

=====================
QFuture watcher class
=====================

.. seealso::

   - qt-project.org/doc/qt-5.0/qtcore/qfuturewatcher.html
   

.. contents::
   :depth: 3

Detailed Description
======================


The QFutureWatcher class allows monitoring a QFuture using signals and slots.

QFutureWatcher provides information and notifications about a QFuture. 

Use the setFuture() function to start watching a particular QFuture. 

The future() function returns the future set with setFuture().

For convenience, several of QFuture's functions are also available in 
QFutureWatcher: progressValue(), progressMinimum(), progressMaximum(), 
progressText(), isStarted(), isFinished(), isRunning(), isCanceled(), 
isPaused(), waitForFinished(), result(), and resultAt(). 

The cancel(), setPaused(), pause(), resume(), and togglePaused() functions are 
slots in QFutureWatcher.



void QFutureWatcher::cancel() [slot]
======================================

Cancels the asynchronous computation represented by the future(). 

Note that the cancelation is asynchronous. Use waitForFinished() after calling 
cancel() when you need synchronous cancelation.

Currently available results may still be accessed on a canceled QFuture, but 
new results will not become available after calling this function. 

Also, this QFutureWatcher will not deliver progress and result ready signals 
once canceled. This includes the progressValueChanged(), progressRangeChanged(), 
progressTextChanged(), resultReadyAt(), and resultsReadyAt() signals.

.. warning:: Be aware that not all asynchronous computations can be canceled. 
   For example, the QFuture returned by QtConcurrent::run() cannot be canceled; 
   but the QFuture returned by QtConcurrent::mappedReduced() can.

