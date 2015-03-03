.. module:: usbutils_news
    :synopsis: usbutils linux
    :platform: GNU/Linux


.. index::
   pair: USB ; usbutils


.. _usb_utils_news:

=============
usbutils news
=============

usbutils 0.87 release
======================

::


    from    Greg KH <greg@kroah.com>
    to  linux-usb@vger.kernel.org
    cc  linux-kernel@vger.kernel.org
    date    Thu, Mar 18, 2010 at 2:51 AM
    subject usbutils 0.87 release
    mailing list    <linux-usb.vger.kernel.org> Filter messages from this mailing list
    mailed-by   vger.kernel.org

    hide details 2:51 AM (8 hours ago)

    Here's the 0.87 release of usbutils.

    There are some fixes for people having problems with the latest libusb
    version, minor code edits, and some new USB class logic.  The whole
    changelog is below.

    The package can be downladed from kernel.org:
           http://www.kernel.org/pub/linux/utils/usb/usbutils/

    We've switched over to using git for development now, which makes things
    much easier than the old cvs tree.  The tree can be found on both
    kernel.org and github.com if you want to fork it and send us changes
    easier:
           http://git.kernel.org/?p=linux/kernel/git/gregkh/usbutils.git
           http://github.com/gregkh/usbutils/tree/master

    thanks,

    greg k-h

    -----------

    Shortlog of changes since last release (0.86):

    Aurelien Jarno (1):
         lsusb.c: correctly dump ccid devices

    Greg Kroah-Hartman (11):
         lots of trailing whitespace removed.
         add autogen.sh script
         coding style cleanups for .h files.
         names.c: fix up some compiler warnings
         coding style cleanups for usbmisc.c
         names.c: fix lots of coding style issues
         devtree.c: coding style cleanups
         lsusb.c: coding style fixes
         lsusb.c: fix some build warnings.
         usb.ids: Reserve EEM Gadget id for the Linux Foundation
         add lsusb.py from Kurt Garloff <garloff@suse.de>

    Philip A. Prindeville (1):
         Fix build issue with libusb location



.. index::
   pair: USB ;  CLASS_CCID  0x0b
   pair: USB ;  CCID


lsusb.c correctly dump ccid devices
===================================


.. seealso:: http://github.com/gregkh/usbutils/commit/277327cd6a61d96f9c322289e055ec2b4a129096

::

    lsusb.c: correctly dump ccid devices

    CCID has now an official class according to: http://www.usb.org/developers/defined_class/

    This patch removes the hard-coded value and replace it by a #define,
    and also call dump_ccid_device() when use in a common class interface
    descriptor.

    Signed-off-by: Aurelien Jarno <aurelien@aurel32.net>
    Signed-off-by: Greg Kroah-Hartman <gregkh@suse.de>


::


    +#ifndef USB_CLASS_CCID
    +#define USB_CLASS_CCID      0x0b
    +#endif



