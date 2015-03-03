
.. index::
   DBUS tools
   dbus-monitor
   dbus-send


.. _dbus_tools:

====================
DBUS tools
====================

.. seealso::

   - http://blog.fpmurphy.com/2011/08/introduction-to-udisks.html


.. _dbus_monitor:

dbus-monitor
============

::

    dbus-monitor --system


::

    signal sender=org.freedesktop.DBus -> dest=:1.58 serial=2 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameAcquired
       string ":1.58"
    signal sender=:1.7 -> dest=(null destination) serial=9 path=/org/freedesktop/Hal/Manager; interface=org.freedesktop.Hal.Manager; member=DeviceAdded
       string "/org/freedesktop/Hal/devices/usb_device_b81_200_01699449"
    signal sender=:1.7 -> dest=(null destination) serial=10 path=/org/freedesktop/Hal/Manager; interface=org.freedesktop.Hal.Manager; member=DeviceAdded
       string "/org/freedesktop/Hal/devices/usb_device_b81_200_01699449_if0"
    signal sender=:1.7 -> dest=(null destination) serial=11 path=/org/freedesktop/Hal/Manager; interface=org.freedesktop.Hal.Manager; member=DeviceRemoved
       string "/org/freedesktop/Hal/devices/usb_device_b81_200_01699449_if0"
    signal sender=:1.7 -> dest=(null destination) serial=12 path=/org/freedesktop/Hal/Manager; interface=org.freedesktop.Hal.Manager; member=DeviceRemoved
       string "/org/freedesktop/Hal/devices/usb_device_b81_200_01699449"



::

    dbus-monitor --session



.. _dbus_send:

dbus-send
=========




.. index::
   John Palmieri
   D-Feet

D-Feet graphical D-Bus debugging tool
=====================================

.. seealso::

   - http://live.gnome.org/DFeet/


Description
-----------

D-Feet is a D-Bus debugger written in PyGtk+ by `John Palmieri`_.


.. _`John Palmieri`:  http://www.j5live.com/


Design
------

D-Feet needs your help. The current design was a quick one off that doesn't
really fit any model other than showing off the internals of a D-Bus hierarchy.
It is not optimised for actual debugging workflows.

While it is a useful tool it can be much better.
I am requesting that anyone who has a D-Bus development workflow to write up
their day to day usage of D-Bus debugging tools.

Features
--------

Current Features

- View names on any bus
- View exported objects, interfaces, methods and signals
- View the full command line of services on the bus
- Execute methods with parameters on the bus and see their return values



.. index::
   HAL
   udisks


.. _udisks_1:

udisks (1)
==========

.. seealso::

   - http://blog.fpmurphy.com/2011/08/introduction-to-udisks.html
   - http://www.freedesktop.org/wiki/Software/udisks
   - udisks-tcp-bridge
   - http://library.gnome.org/users/palimpsest/


Udisks (formerly called DeviceKit-disks) is a replacement for part of the
functionality which used be provided by the now deprecated HAL (Hardware Abstraction Layer).
Essentially it is an abstraction for enumerating disk and storage devices and
performing operations on them.

Udisks provides:

- A daemon (udisks-daemon) that implements well-defined D-Bus interfaces that
  can be used to query and manipulate disk and storage devices.
- A command-line tool (udisks), that can be used to query and use the daemon.


::

    ps -ef | grep udisks



::

    udisks --help



::

    udisks --enumerate


::

    udisks --monitor




.. _udisks_2:

udisks2
==========


.. seealso:: http://people.freedesktop.org/~david/udisks2-20110628/index.html


DBUS_SESSION_BUS_ADDRESS
========================

::

    $ env | grep DBUS_SESSION_BUS_ADDRESS




