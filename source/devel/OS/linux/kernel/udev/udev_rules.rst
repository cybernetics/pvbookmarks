

.. index::
   pair: udev ; rules



.. _udev_rules:

==========
udev rules
==========

.. seealso::

   - http://doc.ubuntu-fr.org/udev (in french)
   - http://www.reactivated.net/writing_udev_rules.html
   - http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev_vs_devfs
   - <http://www.kroah.com/linux/talks/ols_2003_udev_paper/Reprint-Kroah-Hartman-OLS2003.pdf>


Introduction
============

**udev rules** are flexible and very powerful. Here are some of the things
you can use rules to achieve:

* Rename a device node from the default name to something else.
* Provide an alternative/persistent name for a device node by creating
  a symbolic link to the default device node.
* Name a device node based on the output of a program.
* **Change permissions and ownership of a device node**
* Launch a script when a device node is created or deleted (typically
  when a device is attached or unplugged)
* Rename network interfaces

Writing rules is not a workaround for the problem where no device nodes
for your particular device exist. Even if there are no matching rules,
udev will create the device node with the default name supplied by the kernel.

History
========

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
======================

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


.. index::
   groupadd
   gpasswd
   plugdev group
   group plugdev
   udevadm control --reload-rules


.. _plugdev_group:

Create a plugdev group
======================

.. seealso:: http://www.linux-usb.org/usb.ids


Before creating the rules, you have to create a ``plugdev`` group.


Before creating the udev rule we must:

- create a ``plugdev`` group (if it does not already exist)::

        groupadd plugdev


- add the users who will use the ``CL1356A+`` smartcard reader to this group::

    sudo gpasswd -a $USERNAME plugdev


::

    > groups $USERNAME

::

    user : user adm dialout cdrom plugdev fuse lpadmin netdev admin sambashare



For "udev" systems
==================

In /etc/udev/rules.d/41-flip.rules I have (I am part of the group "flip")::

    #add support AT89C5132 AT89C51SND1 AT89C51SND2 ATOCDTARGET
    ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2fff", GROUP="flip", MODE="0660"

    #add support AT89C5130 AT89C5131
    ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2ffd", GROUP="flip", MODE="0660"

    #add support AT90USB1286 AT90USB1287
    ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2ffb", GROUP="flip", MODE="0660"

    #add support AT90USB162
    ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2ffa", GROUP="flip", MODE="0660"

    #add support AT90USB647 AT90USB646
    ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2ff9", GROUP="flip", MODE="0660"

    #add support AT32UC3A0128 AT32UC3A0256 AT32UC3A0512 AT32UC3A1128 AT32UC3A1256 AT32UC3A1512
    ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2ff8", GROUP="flip", MODE="0660"

    #add support AT90USB82
    ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2ff7", GROUP="flip", MODE="0660"

    #add support AT32UC3B0128 AT32UC3B0256 AT32UC3B064 AT32UC3B1128 AT32UC3B1256 AT32UC3B164
    ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2ff6", GROUP="flip", MODE="0660"



Remember to run '/sbin/udevstart' after adding the file. Also add group 'flip' and add necessary users.

There is a file that came with batchisp and it reads
The Linux platform used different systems for device drivers.
Older systems uses hotplug while newer systems uses udev.




Most current solution: use udev
===============================

The latest and greatest way of managing hotplugged (and cold-plugged) devices
under Linux is called `udev <udev_readme>`. This is a development of the older "hotplug"
system (see below).

When a device is connected, the kernel will call the program /sbin/udev
in order to create a device node in the /dev/ file hirerarchy.
It will also remove devices from this hierarchy when they are unplugged.

Traditionally, all devices plugged into a Linux system are expected to have
a kernel device driver, or to load one on-the-fly when a new device is connected.

Libusb cannot use these device drivers, instead it attempts to access the raw
device nodes from user mode, not as a kernel module.

In order for libusb to find the device node, it needs to locate it in the
/dev filesystem.


The recommended way to let udev create nodes in the /dev filesystem is
to add a udev rule like the following into some foo.rules file inside the
/etc/udev/rules.d/ directory:

# usbfs-like devices
SUBSYSTEM=="usb", PROGRAM="/bin/sh -c 'K=%k; K=$${K#usbdev}; \
printf bus/usb/%%03i/%%03i $${K%%%%.*} $${K#*.}'", \ NAME="%c"

This layout is used by for example the Debian distribution and Fedora Core.
This rule creates a device tree identical to the earlier /proc/bus/usb/ tree,
but under /dev/bus/usb/ instead. If this device tree exists, libusb will
default to use it. It will look like this::

    /dev
    /bus
    /usb
    /001
    /001
    /002
    /003
    /002
    /001
    /002
    ...

However notice that the permissions on the nodes will be default
permissions: often this means they are only accessible for writing by the
root user, whereas non-root users often can access it read-only.

The way of controlling access to a device node differs between systems,
but a typical way of complementing udev rules with apropriate permissions
is to use PAM (pluggable Authentication Modules), with some sort of
configuration under /etc/security/ (For details on this, see below.)

The use of /dev nodes is also different from the old usbfs solution in that it
enables the use of ACL:s (Access Control Lists) to control access for the USB
device nodes.

.. warning::  ACL:s could not be used on the /proc filesystem.

A less good alternative that may however be useful for debugging would be to
supply the argument MODE="666" to the above udev rule, or, slightly better,
to tag on: MODE="660", GROUP="foo"

where "foo" is a group of users (e.g. desktop users) that need to access the
device in read/write mode.

If libusb cannot find a device hierarchy below /dev/bus/usb/ (as is the case if
you are not using udev, or not using it with the above rule), it will fall back
on using /proc/bus/usb/ instead.

Additionally, you may want to trigger unique actions for your device at the same time.
To do this, create a rules file /etc/udev/rules.d/bar.rules with these lines:

SUBSYSTEM=="usb", ACTION=="add", ATTRS{idVendor}=="1234", \ ATTRS{idProduct}=="4321"

At the end of this line you can then tag on any device-specific actions for
device 1234/4321, for example::

    MODE="660", GROUP="baz" to set mode and group
    RUN="/usr/local/bin/baz" to run a script on plug-in
    SYMLINK+="foo" to create a symlink device node with this name in /dev

You can read more about udev in its own documentation.


.. index::
   permissions under linux
   PAM

Permissions setting with PAM
============================

In addition to the udev rule for creating the device node you will want to change
the  permissions on the new node, unless it defaults to something that is globally
writeable and readable.

Making anything that is plugged in on the USB bus writeable and readable by ALL
users is typically a bad idea, because what you most typically want to do is to make
it writeable and readable for the console user, i.e. the person that happens to sit
behind the screen and keyboard of this very computer.

Managing this by groups is a bit kludgy: it means you set up a group for all
console users and add all users that may use the console to this group.
This also means that one user that is a member of this group could be at the console
plugging his USB keydrive in, while another user of the same group is logged in
remotely, and making a blank copy of the same keydrive at the same time, for example.

Since Linux is used in a strict multi-user context, this has to be solved:
**give permissions to hotplugged devices only to the console user**.

Fedora Core 5 and later does this by using PAM. Whenever something happens in udev,
PAM is called to modify the permissions on anything that appeared in the file system
in accordance to a set of security rules.

The trick is to create a symbolic link for your new device, then let PAM match the
name of this link and change the permissions of it.

For example, in /etc/udev/rules.d/foo.rules you write::

    SUBSYSTEM=="usb", ACTION=="add", ATTRS{idVendor}=="1234", \ ATTRS{idProduct}=="4321", SYMLINK+="foo-%k"


This will create a symlink named "/dev/foo-nn" where nn is some unique number for
each added device matching this VID and PID.

You then set up PAM console rules in accordance, by adding a /etc/security/console.perms.d/foo.perms
containing::

    <foo>=/dev/foo*
    <console> 0600 <foo> 0600 root

This instructs PAM to give the console user (and root) read and write permissions
to the new  symlink, whenever it appears. The permission change on the symlink
will then fall through to the new device node.


Previous solution: use hotplug
==============================

Before udev another system, generally considered less elegant, known simply as
"hotplug" was used. In this case the program /sbin/hotplug would be called whenever
devices were connected or removed from the system, and the corresponding configuration
lives in /etc/hotplug/.

With hotplug not using udev at the same time, all devices are accessed using the
usbfs hierarchy below /proc/bus/usb/. Again, thishttp://mihd.net/y7w20q will be
used by libusb, since libusb does not use any device drivers.
The hierarchy will look like this:::

    /proc
    /bus
    /usb
    /001
    /001
    /002
    /003
    /002
    /001
    /002
    ...

When USB devices are plugged in, their corresponding device node is created in
/proc/bus/usb/ by the kernel, without any external program intervention (as is
the case with udev).

However, to correct the permissions on these device nodes, if your device requires
anything else than read access, you need to supply a script in /etc/hotplug/usb/
that detects your device and change its permissions, for example this /etc/hotplug/usb/foo.usermap::

    # Foo device with VID=1234 and PID=4321
    bar 0x0003 0x1234 0x4321 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000

(All this need to be in one line.)

The first string "bar" points out the name of a script placed in /etc/hotplug/usb/bar,
with for example the following contents::

    #!/bin/bash
    if [ "${ACTION}" = "add" ] && [ -f "${DEVICE}" ] then chgrp baz "${DEVICE}"
    chmod 660 "${DEVICE}"
    fi

to let users in the group "baz" access the device for reading and writing.
There exist solutions similar to the PAM permission change for hotplug, but they
are all kind of hackish.

You can read more about hotplug and its usermaps in the hotplug documentation.
Maybe someone with more Linux experience can understand this better.


For "hotplug" systems
=====================

- The files libavrtools and libavrtools.usermap should be placed in /etc/hotplug/usb.
- The group avrtools should be created, containing the users which are allowed
  to use the JTAGICE mkII devices.

