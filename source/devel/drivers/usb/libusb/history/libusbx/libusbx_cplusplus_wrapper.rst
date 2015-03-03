

.. index::
   pair: C++; libusbx



.. _libusbx_cplusplus_wrapper:

====================
libusbx C++ wrapper
====================

.. seealso::

   - https://github.com/zarthcode/Libusbpp


.. contents::
   :depth: 3


Overview (2012/9/5)
===================

::



    From: Anthony Clay <anthony.clay@zarthcode.com>
    Date: 2012/9/5
    Subject: [Libusbx-devel] Libusb++ is available.
    To: libusbx-devel@lists.sourceforge.net

Greetings all,

I've spent the last couple of weeks building a wrapper for libusb to save time
while developing native c++ applications.

It completely hides the libusb implementation inside of an object-oriented
framework.

It's based around a USB "Device" class that can be instanced easily using the
default factories.

From there, you can iterate through Configurations, Interfaces, and Endpoints,
and create specialized Transfer objects to communicate with your device in a
straight-forward manner.

In the example LibusbTest.cpp is a demonstration all of the available transfer
types, with only a few lines of code!)


The library does utilize C++11 standard library features, including threading
for effortless asynchronous background transfers.

However, the real power is shown when you inherit the base device class.

By doing this, you can create intuitive, easy-to-use libraries for your devices
in record time.

If you give it a try, I'd love some feedback on what you think about how I've
structured things, and where it can stand some improvement.
(It's untested in linux, though, I expect no issues other than needing a makefile.)




