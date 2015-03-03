

.. index::
   pair: libccid; 1.3.13


.. _libccid 1.3.13:

==========================
Changes for libccid 1.3.13
==========================


.. contents::
   :depth: 3


2010-06-04
==========

 Ludovic Rousseau

* [r4979] README, configure.in: release 1.3.13

2010-06-01
==========

Ludovic Rousseau

* [r4975] readers/GemPCTwin.txt: update
* [r4973] src/ccid.c, src/ccid.h, src/ccid_ifdhandler.h,
  src/ccid_serial.c, src/ccid_serial.h, src/ccid_usb.c,
  src/ccid_usb.h, src/commands.h, src/convert_version.pl,
  src/create_Info_plist.pl, src/debug.c, src/debug.h, src/defs.h,
  src/ifdhandler.c, src/parse.c, src/utils.c, src/utils.h: update
  copyright date
* [r4972] src/parse.c: No need to #include <usb.h> since revision
  4907
* [r4971] configure.in: remove duplicate errno.h in
  AC_CHECK_HEADERS()
* [r4970] configure.in, m4/as-ac-expand.m4: Correctly display
  $bindir and $sysconfdir values when they are not changed from the
  default values (instead of NONE/bin and NONE/etc)

2010-05-27
==========

Ludovic Rousseau

* [r4965] readers/Lenovo.txt: update
* [r4963] src/ccid_usb.c: OpenUSBByName(): allow the combination of
  USE_COMPOSITE_AS_MULTISLOT and libhal. It does work so do not
  prevent its use.

2010-05-20
==========

Ludovic Rousseau

* [r4956] src/ccid.h, src/ccid_serial.c, src/ccid_usb.c,
  src/ifdhandler.c: Add support of SCARD_ATTR_VENDOR_IFD_SERIAL_NO

2010-05-15
==========

Ludovic Rousseau

* [r4943] readers/GemPCPinpadv2.txt: Gemalto PC pinpad v1+

2010-05-10
==========

Ludovic Rousseau

* [r4939] src/commands.c: Revert revision 4936 (stupid me)
* [r4938] src/ifdhandler.c: IFDHCreateChannelByName() &
  IFDHCreateChannel(): use the low level CmdGetSlotStatus() instead
  of IFDHICCPresence() to be able to fix the read timeout.

  We use a read timeout of 100 milliseconds instead of 2 secondes.
  The maximum wait time is now 200 milliseconds instead of 4
  seconds.
  This increases the startup time a lot (up to 95%) when pcscd is
  auto started.
* [r4937] src/ccid.c, src/ccid.h, src/ccid_serial.c,
  src/ccid_usb.c, src/commands.c, src/defs.h, src/ifdhandler.c:
  change read timeout from second to millisecond unit to have a
  sub-second control
* [r4936] src/commands.c: SecurePINVerify() & SecurePINModify():
  use min() instead of max() to get a minimum of 30 seconds for the
  read timeout


