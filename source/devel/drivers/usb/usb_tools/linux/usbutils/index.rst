

.. index::
   pair: USB ; Utils
   pair: People ; Greg Kroah (USB)


.. _usbutils:

========
Usbutils
========

.. seealso::

   - http://github.com/gregkh/usbview/


.. contents::
   :depth: 3

Introduction
============


A version of USBView is available for Linux from  http://www.kroah.com/linux-usb/.
As with the Windows version, this displays a connection tree of all the USB
devices connected to the PC.  A version compiled for x86_64 Linux can be
downloaded here_ .

.. _here: http://www.ftdichip.com/Resources/Utilities/usbview_x86_64.tar.gz



News
====

http://lkml.org/lkml/2010/8/12/372
----------------------------------

Here's the 0.90 release of usbutils.

Big thing is support for the audio class descriptors.

Other than that, it's just a lot of little things, as can be seen
in the changelog below.

The package can be downladed from kernel.org:
    http://www.kernel.org/pub/linux/utils/usb/usbutils/

We've switched over to using git for development now, which makes things
much easier than the old cvs tree.  The tree can be found on both
kernel.org and github.com if you want to fork it and send us changes
easier:

- http://git.kernel.org/?p=linux/kernel/git/gregkh/usbutils.git
- http://github.com/gregkh/usbutils/tree/master

thanks,
