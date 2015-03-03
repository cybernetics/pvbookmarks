

.. index::
   pair: libusb ; haskell


==============
libusb haskell
==============

.. seealso:: http://hackage.haskell.org/package/usb

The usb package
================

This library allows you to communicate with USB devices from userspace. It is implemented
as a high-level wrapper around bindings-libusb which is a low-level binding to the C library: libusb-1.*.

This documentation assumes knowledge of how to operate USB devices from a
software standpoint (descriptors, configurations, interfaces, endpoints,
control/bulk/interrupt/isochronous transfers, etc).
Full information can be found in the USB 2.0 Specification.

For an example how to use this library see the ls-usb package at:

- http://hackage.haskell.org/package/ls-usb

Also see the usb-safe package which wraps this package and provides some
strong safety guarantees for working with USB devices:

- http://hackage.haskell.org/package/usb-safe

Finally have a look at the usb-enumerator package which provides iteratee
enumerators for enumerating bulk and interrupt endpoints:

http://hackage.haskell.org/package/usb-enumerator

Besides this API documentation the following sources might be interesting:

- The libusb 1.0 documentation at: http://libusb.sourceforge.net/api-1.0/
- The USB 2.0 specification at: http://www.usb.org/developers/docs/
- The bindings-libusb documentation at: http://hackage.haskell.org/package/bindings-libusb
- "USB in a NutShell" at: http://www.beyondlogic.org/usbnutshell/usb1.htm









