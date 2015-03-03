
.. index::
   pair: RS232; SerialPort


.. _serial_port:

===========
SerialPort
===========

.. seealso::

   - http://www.webalice.it/fede.tft/serial_port/serial_port.html
   - http://gitorious.org/serial-port


Description
============

This article explains how to interface with serial ports from C++.
Instead of presenting an API specific to a single operating system, the
Boost.asio library was used. This library provides portable, high performance
implementation of sockets and serial ports.

The chosen presentation is to provide code with a growing level of scalability,
and a growing level of complexity. It starts with a simple class to wrap Asio's
serial ports to provide string write and read, and expands to topics like binary
data transfer, timeouts, and asynchrounous operation.

All the example presented here are available for download at the end of the article.

This article presents some classes that wrap the asio library. They can be used
as-is, or its implementation can be studied to understand how to perform these
tasks with asio.









