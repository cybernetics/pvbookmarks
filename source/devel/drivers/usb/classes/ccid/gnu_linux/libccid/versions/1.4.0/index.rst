

.. index::
   pair: libccid; 1.4.0
   pair: CCID; TAG_IFD_STOP_POLLING_THREAD

.. _libccid_1.4.0:

==========================
Changes for libccid 1.4.0
==========================

.. seealso::

   - http://ludovicrousseau.blogspot.com/2010/08/new-ccid-140-and-card-movement.html


4 days ago I released a new version 1.4.0 of my CCID driver (libccid).

Changes 1.4.0 - 4 August 2010, Ludovic Rousseau:

* add support of Kingtrust Multi-Reader, Dectel CI692, Todos CX00,
  C3PO LTC36, ACS AET65, Broadcom 5880, Tianyu Smart Card Reader,
  Gemalto Hybrid Smartcard Reader
* Add support of the SCM SDI 010 again. At least the contact
  interface can be used.
* Use :ref:`libusb-1.0 <libusb_1.0>` instead of libusb-0.1
* add support of TAG_IFD_STOP_POLLING_THREAD and use of the asynchronous
  libusb API to be able to stop a transfer.
* Request pcsc-lite 1.6.2 minimum (instead of 1.6.0) to have
  TAG_IFD_STOP_POLLING_THREAD defined
* The O2MICRO OZ776 patch (for OZ776, OZ776_7772, REINER_SCT and
  BLUDRIVEII_CCID) is no more supported with libusb-1.0
* correctly get the IFSC from the ATR (ATR parsing was not
  always correct)
* some minor bugs removed


The change that will interest us here is the support of TAG_IFD_STOP_POLLING_THREAD.
This is used so that pcscd can ask the driver to stop its polling function.

But the support of TAG_IFD_STOP_POLLING_THREAD has only be included in :ref:`pcsc-lite 1.6.2 <libpcsclite_1.6.2>`.
This is why you need pcsc-lite 1.6.2 to compile libccid 1.4.0.
