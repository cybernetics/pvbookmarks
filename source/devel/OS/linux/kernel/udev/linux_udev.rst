
==========
udev rules
==========

.. seealso::

   - http://doc.ubuntu-fr.org/udev (in french)
   - http://www.reactivated.net/writing_udev_rules.html


Preambule
=========

udev is targeted at Linux kernels 2.6 and beyond to provide a userspace
solution for a dynamic /dev directory, with persistent device naming.

The previous /dev implementation, devfs, is now deprecated, and udev is
seen as the successor. udev vs devfs is a sensitive area of conversation

Over the years, the things that you might use udev rules for has changed,
as well as the flexibility of rules themselves. On a modern system, udev
provides persistent naming for some device types out-of-the-box,
eliminating the need for custom rules for those devices.



Terminology: devfs, sysfs, nodes, etc.
======================================

A basic introduction only, might not be totally accurate.

On typical Linux-based systems, the /dev directory is used to store
file-like device nodes which refer to certain devices in the system.
Each node points to a part of the system (a device), which might or
might not exist.

Userspace applications can use these device nodes to interface with the
systems hardware, for example, the X server will "listen to" /dev/input/mice
so that it can relate the user's mouse movements to moving the visual mouse pointer.

The original /dev directories were just populated with every device that
might possibly appear in the system. /dev directories were typically
very large because of this. devfs came along to provide a more manageable
approach (noticeably, it only populated /dev with hardware that is plugged
into the system), as well as some other functionality, but the system
proved to have problems which could not be easily fixed.

**udev** is the "new" way of managing /dev directories, designed to
  clear up some issues with previous /dev implementations, and provide
  a robust path forward. In order to create and name /dev device nodes
  corresponding to devices that are present in the system, udev relies
  on matching information provided by sysfs with rules provided by the user.
  This documentation aims to detail the process of rule-writing, one of
  the only udev-related tasks that must (optionally) be performed by the user.

**sysfs** is a new filesystem to the 2.6 kernels. It is managed by the
  kernel, and exports basic information about the devices currently
  plugged into your system. udev can use this information to create device
  nodes corresponding to your hardware. sysfs is mounted at /sys and is
  browseable. You may wish to investigate some of the files stored there
  before getting to grips with udev.


Why using udev rules ?
=======================

udev rules are flexible and very powerful. Here are some of the things
you can use rules to achieve:

* Rename a device node from the default name to something else
* Provide an alternative/persistent name for a device node by creating
  a symbolic link to the default device node
* Name a device node based on the output of a program
* **Change permissions and ownership of a device node**
* Launch a script when a device node is created or deleted (typically
  when a device is attached or unplugged)
* Rename network interfaces

Writing rules is not a workaround for the problem where no device nodes
for your particular device exist. Even if there are no matching rules,
udev will create the device node with the default name supplied by the kernel.

In our specific case, we want that any user in the `plugdev` group
can use the id3 certis2 fingerprint reader.


.. index::
   groupadd
   gpasswd
   plugdev group
   udevadm control --reload-rules


.. _fingerprint_udev_rules_bis:

99-id3-fingerprint-reader.rules
===============================

.. seealso:: :ref:`fingerprint_udev_rules`

Create a plugdev group
----------------------

Before creating the udev rule we must:

- create a ``plugdev`` group (if it does not already exist)::

        groupadd plugdev


- add the users who will use the ``Certis2`` reader to this group::

    gpasswd -a $USERNAME plugdev


::

    > groups $USERNAME

::

    user : user adm dialout cdrom plugdev fuse lpadmin netdev admin sambashare



Create the udev rule
--------------------

Any user in the ``plugdev`` group will be able to use the Certis2.


::

    > cd /etc/udev/rules.d
    > udevadm control --reload-rules
    > more 99-id3-fingerprint-reader.rules

::

    ATTRS{idVendor}=="0b81", ATTRS{idProduct}=="0103", SUBSYSTEMS=="usb", ACTION=="add", MODE="0666", GROUP="plugdev"


Test
----

If you type::

    > lsusb

You can see the Certis2 reader which is not the case if the user is not
``root`` or is not in the ``plugdev`` group::

    Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 011: ID 0b81:0103 id3 Semiconductors Certis V2 fingerprint reader
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 001 Device 003: ID 0bda:0111 Realtek Semiconductor Corp. Card Reader
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub



