
.. index::
   pair: USB ; 2
   pair: USB ; 2
   pair: USB ; Command Verifier


.. _usb20cv:

===============================
USB 2.0 Command Verifier
===============================

.. seealso::

   - http://www.usb.org/developers/tools/
   - http://www.usb.org/developers/tools/USB20CV_Releasex86_R1.4.9.2.msi
   - http://www.usb.org/developers/tools/USB20CV_Releasex64_1.4.9.2.msi


.. contents::
   :depth: 3


Introduction
============


The installation utility, InstallUSB20CV1492.msi (8.6MB) contains USB Command
Verifier (USB20CV) version R1.4.9.2 and documentation. USB20CV is the compliance
test tool which evaluates High, Full and Low-speed USB devices for conformance
to the USB Device Framework (Chapter 9), Hub device class (Chapter 11), HID class,
and OTG specifications.

Also included are mass storage class and USB video class specification tests.

All USB peripherals are required to pass the Device Framework tests in order to
gain certification.  The other tests are mandatory for certification when supported.
If you have installed a previous version of the USB 2.0 Command Verifier, you
must uninstall it before installing the new version

USB20CV revision 1.4.9.2 is the official test tool for device framework testing.

As of April 2007, the mass storage class tests and the video class tests are
official and mandatory.  This software is provided courtesy of Intel Corporation.

The USB20CV x64Bit revision 1.4.9.2 can be downloaded here_.

.. _here: http://www.usb.org/developers/tools/USB20CV_Releasex64_1.4.9.2.msi


.. note:: Please do not install this tool on a machine that already has previous
   versions of USB20CV installed.

This software release will work on Windows XP SP2 (English version only) with
all critical patches installed, Windows Vista with User Access Control disabled,
or Windows 7 with User Access Control disabled.

This tool requires an Enhanced Host Controller Interface, EHCI.

If testing Full or Low-speed devices, an intervening Hi-Speed USB Hub is
required.  USB20CV R1.4.9.2 uses a special purpose driver for the Hi-Speed USB
Host Controller.

USB20CV R1.4.9.2 automatically replaces the standard Microsoft EHCI host driver
with its own test stack driver.

When USB20CV R1.4.9.2 exits, the original standard Microsoft EHCI host driver
is restored. Stack switching has been extensively tested with Microsoft EHCI
drivers only.

Stack switching has not been tested with USB 2.0 host controller drivers
provided by other vendors.  Please read the Release Notes for details.
