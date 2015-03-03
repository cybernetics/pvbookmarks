

.. index::
   pair: USB ; CDC
   ! CDC


.. _usb_cdc:

==================================
USB Composite Class Devices (CDC)
==================================


USB Composite Class Devices

The USB specification defines a composite class device as a device whose
device-descriptor fields for device class (bDeviceClass) and device subclass
(bDeviceSubClass) both have the value 0. A composite class device appears to
the system as a USB device using a single bus address that may present multiple
interfaces, each of which represents a separate function.

A good example of a composite class device is a multifunction device, such as a
device that performs printing, scanning, and faxing. In such a device, each
function is represented by a separate interface.

In Mac OS X, the I/O Kit loads the AppleUSBComposite device driver for composite
class devices that do not already have vendor-specific device drivers to drive
them.

The AppleUSBComposite driver configures the device and causes drivers to be
loaded for each USB interface.

Although most multifunction USB devices are composite class devices, not all
composite class devices are multifunction devices.

The manufacturer of a single-function USB device is at liberty to classify
the device as a composite class device as long as the device meets the USB
specifications.

