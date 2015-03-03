.. module:: USB_DFU_introduction
   :synopsis: USB DFU introduction


.. index::
   pair: DFU ; USB

===============================
USB DFU Device Firmware Upgrade
===============================

.. seealso::

   - http://www.usb.org/developers/devclass_docs/usbdfu10.pdf
   - http://dfu-programmer.sourceforge.net/
   - :ref:`atmel_dfu_programmer`



.. _usb_dfu_firmware_upgrade:

DFU (Device Firmware Upgrade) overview
======================================

.. seealso::

   - http://www.usb.org/developers/devclass_docs/usbdfu10.pdf
   - :ref:`connexion_plug_and_play_enumeration`


Users that have purchased USB devices require the ability to upgrade the
firmware of those devices with improved versions as they become available
from manufacturers.

Device Firmware Upgrade is the mechanism for accomplishing that task.

**Any class of USB device can exploit this capability by supporting the
requirements  specified in this document.**

This document focuses on installing product enhancements and patches to
devices that are already deployed in the field.
Other potential uses for the firmware upgrade capability are beyond the
scope of this document.
Because it is impractical for a device to concurrently perform both DFU
operations and its normal runtime activities, those normal activities must
cease for the duration of the DFU operations. Doing so means that the device
must change its operating mode; i.e., a printer is not a printer while it is
undergoing a firmware upgrade; it is a PROM programmer.

However, a device that supports DFU is not capable of changing its mode of
operation on its own volition.
**External (human or host operating system) intervention is required.**



There are four distinct phases required to accomplish a firmware upgrade:



enumeration
-----------


The device informs the host of its capabilities. A DFU class-interface
descriptor and associated functional descriptor embedded within the device’s normal
run-time descriptors serves this purpose and provides a target for class-specific
requests over the control pipe.

reconfiguration
---------------

The host and the device agree to initiate a firmware upgrade.
The host issues a USB reset to the device, and the device then exports a second
set of descriptors in preparation for the Transfer phase.
This deactivates the run-time device drivers associated with the device and
allows the DFU driver to reprogram the device’s firmware unhindered by any other
communications traffic targeting the device.

transfer
--------

The host transfers the firmware image to the device. The parameters specified
in the functional descriptor are used to ensure correct block sizes and timing for
programming the nonvolatile memories.
Status requests are employed to maintain synchronization between the host and the device.

.. _usb_DFU_upgrade_manifestation:

manifestation
-------------

Once the device reports to the host that it has completed the reprogramming
operations, the host issues a USB reset to the device.
The device re-enumerates and executes the upgraded firmware.
**The device’s vendor ID, product ID, and serial number can be used to form an
identifier used by the host operating system to uniquely identify the device.**
However, certain operating systems may use only the vendor and product IDs
reported by a device to determine which drivers to load, regardless of the device
class code reported by the device.
(Host operating systems typically do not expect a device to change classes.)
Therefore, to ensure that only the DFU driver is loaded, it is considered necessary
to change the :ref:`idProduct <id3_products_id>` field of the device when it
enumerates the DFU descriptor set.
This ensures that the DFU driver will be loaded in cases where the operating system
simply matches the vendor ID and product ID to a specific driver.


.. note:: This document does not attempt to specify how a vendor might alter
   the device’s product ID except to suggest that adding one, setting the
   high bit, or using FFFFh are all valid possibilities.
   Vendors may use any scheme that they choose.



