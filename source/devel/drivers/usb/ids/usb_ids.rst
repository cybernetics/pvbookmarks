

.. index::
   pair: USB ; VendorID
   pair: USB; ProductID

.. _usbids:

=======
usb.ids
=======

::

    2 #       List of USB ID's
    3 #
    4 #       Maintained by Stephen J. Gowdy <sgowdy+usb.ids@gmail.com>
    5 #       If you have any new entries, send them to the maintainer.
    6 #       Send entries as patches (diff -u old new).
    7 #       The latest version can be obtained from
    8 #               http://www.linux-usb.org/usb.ids


.. seealso::

   - http://www.linux-usb.org/usb.ids


http://www.linux-usb.org/usb-ids.html
======================================

This is a public repository of all known ID's used in USB devices:
ID's of vendors, devices, subsystems and device classes. It is used in
various programs (e.g., The USB Utilities) to display full human-readable
names instead of cryptic numeric codes.


.. seealso::

   - https://usb-ids.gowdy.us/read/UD/
   - http://sourceforge.net/projects/pciids/


.. index::
   pair: id3 Technologies; VID

.. _id3_vendor_id:

id3semiconductors Vendor ID (VID) 0x0b81
----------------------------------------

The id3semiconductors Vendor ID (VID) is **0x0b81**


The id3semiconductor's VID should be in this list:

- https://usb-ids.gowdy.us/read/UD/


.. index::
   pair: 0x0b81 ; id3 Technologies


.. _id3_products_id:

id3semiconductors Product IDs (PID)
-----------------------------------

============  ============================
Product ID    Product Name
============  ============================
0001          Biothentic II smartcard reader with fingerprint sensor
0002          DFU-Enabled Devices (DFU)
0012          BioPAD biometric module (DFU + CDC)
0102          Certis V1 fingerprint reader
0103          Certis V2 fingerprint reader
0200          CL1356T / CL1356T5 / CL1356A smartcard readers (CCID)
0201          CL1356T / CL1356T5 / CL1356A smartcard readers (DFU + CCID)
0220          CL1356A FFPJP smartcard reader (CCID + HID)
0221          CL1356A smartcard reader (DFU + CCID + HID)
============  ============================



.. index::
   pair: Stephen J. Gowdy ; USB ids maintainer
   pair: USB ; ids maintainer


History
=======

Update the list by the web. But be careful, the update is not immediate
and must be approved by Stephen J. Gowdy <sgowdy+usb.ids@gmail.com>.

::

    From - Fri Mar 05 08:29:35 2010
    Date: Thu, 4 Mar 2010 17:21:48 +0100 (CET)
    From: "Stephen J. Gowdy" <gowdy@cern.ch>
    X-X-Sender: gowdy@localhost
    To: Patrick Vergain <patrick.vergain@id3.eu>
    Subject: Re: diff -u usb.ids usb_with_id3.ids


    It needed approved. I've just down that. They should appear online
    overnight.

    On Thu, 4 Mar 2010, Patrick Vergain wrote:

    > Le 04/03/2010 16:49, Stephen J. Gowdy a écrit :
    > can you try using the web interface?
    >
    > I did try but unfortunately the vendor and product names do not appear and I don't know for which reasons.
    >



First insertion of id3 Semiconductors vendorId
----------------------------------------------


::

    $ diff -u usb.ids usb_with_id3.ids


::

    --- usb.ids 2010-03-03 17:07:04.718750000 +0100
    +++ usb_with_id3.ids    2010-03-04 15:06:03.406250000 +0100
    @@ -8863,6 +8863,11 @@
     0b7b  Taiko Denki Co., Ltd
     0b7c  ITRAN Communications, Ltd
     0b7d  Astrodesign, Inc.
    +0b81  id3 Semiconductors
    +   0102 Certis V1 fingerprint reader
    +   0103 Certis V2 fingerprint reader
    +   0200 CL1356T/T5 smarcard reader
    +   0220 CL1356A smarcard reader
     0b84  Rextron Technology, Inc.
     0b85  Elkat Electronics, Sdn., Bhd.
     0b86  Exputer Systems, Inc.



The usb.ids file on centos
==========================

::

    // found with the command
    // locate usb.ids
    // ===============================
    #define FILE_USB_IDS "/usr/share/hwdata/usb.ids"


.. _update_usb_ids_on_ubuntu:

update usb.ids on debian/ubuntu
===============================

::

    sudo update-usbids

Locations of usb.ids on ubuntu
------------------------------

::

    /usr/share/hwdata/usb.ids
    /usr/share/misc/usb.ids
    /var/lib/usbutils/usb.ids



