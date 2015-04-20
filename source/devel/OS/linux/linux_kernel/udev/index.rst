
.. index::
   pair: Linux ; Udev
   pair: Udev; Systemd
   ! Udev


.. _udev:

==================
udev (see systemd)
==================

.. image:: udev-tux.png


.. seealso::

   - https://secure.wikimedia.org/wikipedia/en/wiki/Udev
   - :ref:`systemd`


Introduction
=============

``udev`` is the device manager for the Linux kernel.

Primarily, it manages device nodes in /dev. It is the successor of devfs and
hotplug, which means that it handles the /dev directory and all user space
actions when adding/removing devices, including firmware load.


.. _udev_source_code:

Udev Source code
================

.. seealso::

   - http://git.kernel.org/?p=linux/hotplug/udev.git;a=summary

Last commit for udev (Wed, 18 Apr 2012 16:20:57 +0000)
------------------------------------------------------

.. seealso::

   - http://git.kernel.org/?p=linux/hotplug/udev.git;a=commitdiff;h=a7d841f57f096da365a7066bf218e9ce3a23130b;hp=310f4a9a84ed20a5df43427f16a62a34528fbf0b


::

    diff --git a/README b/README
    index 38459c6..a9e04a4 100644 (file)
    --- a/README
    +++ b/README
    @@ -1,3 +1,13 @@
    +***********************************************************
    + The udev development has moved to:
    +   http://www.freedesktop.org/wiki/Software/systemd
    +   http://cgit.freedesktop.org/systemd/systemd/
    +
    + This tree will no longer be updated after April 2012:
    +   http://thread.gmane.org/gmane.linux.hotplug.devel/17392
    +
    +***********************************************************
    +



Manual installation
===================


- download the archive under /tmp

- cd /tmp; unzip the archive

- ./autogen.sh


Architecture
============

The system is divided into three parts:

- The library libudev, that allows access to device information.
- The daemon udevd, in user space, that manages the virtual /dev.
- The administrative command udevadm for diagnostics.

The system gets calls from the kernel via netlink socket.

Earlier versions used hotplug, adding a link to themselves in
/etc/hotplug.d/default with this purpose.



.. seealso:: http://git.kernel.org/?p=linux/hotplug/udev.git;a=tree

Its goals are the following:

-  Run in userspace
-  Create a dynamic /dev.
-  Provide consistent device naming, if wanted.
-  Provide a userspace API to access info about current system devices.

The first item, “run in userspace,” is easily done by harnessing the fact that
/sbin/hotplug generates an event for every device that is added or removed from
the system, combined with the ability of sysfs to show all needed information
about all devices.

The rest of the goals enable the udev project to be split into three separate
subsystems:

1. namedev – handles all device naming
2. libsysfs – a standard library for accessing device information on the system.
3. udev – dynamic replacement for /dev


The udev program will be responsible for talking to both the namedev and
libsysfs libraries to accomplish the device naming policy that has been
specified.
The udev program is run whenever /sbin/hotplug is called by the kernel.
It does this by adding a symlink to itself in the /etc/hotplug.d/default
directory, which is searched by the /sbin/hotplug multiplexer script

udev links
----------

.. toctree::
   :maxdepth: 4

   README
   udev_versus_devfs
   udev_rules
   linux_udev
   rules/index
   udev_tools


