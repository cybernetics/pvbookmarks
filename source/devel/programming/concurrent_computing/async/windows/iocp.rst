

.. index::
   pair: Async ; IOCP


.. _iocp_async_programming:

==============================================
I/O Completion Ports (IOCP) Async Programming
==============================================

.. seealso::

   - http://msdn.microsoft.com/en-us/library/windows/desktop/aa365198%28v=vs.85%29.aspx


.. contents::
   :depth: 3



Introduction
============

I/O completion ports provide an efficient threading model for processing
multiple asynchronous I/O requests on a multiprocessor system.

When a process creates an I/O completion port, the system creates an associated
queue object for requests whose sole purpose is to service these requests.

Processes that handle many concurrent asynchronous I/O requests can do so more
quickly and efficiently by using I/O completion ports in conjunction with
a pre-allocated thread pool than by creating threads at the time they
receive an I/O request.
