


.. _python_semaphore:

==================================
Python semaphore
==================================

.. seealso::

   - :ref:`semaphore`
   - http://docs.python.org/library/threading.html#semaphore-objects


.. contents::
   :depth: 3


Introduction
=============


This is one of the oldest synchronization primitives in the history of computer
science, invented by the early Dutch computer scientist Edsger W. Dijkstra (he
used :meth:`P` and :meth:`V` instead of :meth:`acquire` and :meth:`release`).

A semaphore manages an internal counter which is decremented by each
:meth:`acquire` call and incremented by each :meth:`release` call.  The counter
can never go below zero; when :meth:`acquire` finds that it is zero, it blocks,
waiting until some other thread calls :meth:`release`.


Semaphore class
=================

.. class:: Semaphore([value])

   The optional argument gives the initial *value* for the internal counter; it
   defaults to ``1``. If the *value* given is less than 0, :exc:`ValueError` is
   raised.


Methods
-------

.. _python_sem_acquire:


Python Semaphore.acquire([blocking])
++++++++++++++++++++++++++++++++++++

.. seealso::

   - :ref:`csharp_sem_slim_acquire`

.. method:: acquire([blocking])

  Acquire a semaphore.

  When invoked without arguments: if the internal counter is larger than
  zero on entry, decrement it by one and return immediately.  If it is zero
  on entry, block, waiting until some other thread has called
  :meth:`release` to make it larger than zero.  This is done with proper
  interlocking so that if multiple :meth:`acquire` calls are blocked,
  :meth:`release` will wake exactly one of them up.  The implementation may
  pick one at random, so the order in which blocked threads are awakened
  should not be relied on.  There is no return value in this case.

  When invoked with *blocking* set to true, do the same thing as when called
  without arguments, and return true.

  When invoked with *blocking* set to false, do not block.  If a call
  without an argument would block, return false immediately; otherwise, do
  the same thing as when called without arguments, and return true.



release()
+++++++++

.. method:: release()

  Release a semaphore, incrementing the internal counter by one.  When it
  was zero on entry and another thread is waiting for it to become larger
  than zero again, wake up that thread.





