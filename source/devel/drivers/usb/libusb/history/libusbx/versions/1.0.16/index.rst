
.. index::
   pair: Libusbx ; 1.0.16


.. _libusbx_1.0.16:

============================
libusbx 1.0.16 (2013-07-11)
============================


.. seealso::

   - http://sourceforge.net/projects/libusbx/files/releases/1.0.16/



Announce
========

::

    Hans de Goede <hdegoede@redhat.com> via lists.sourceforge.net 
    à:	 linux-usb <linux-usb@vger.kernel.org>,
    "libusbx-devel@lists.sourceforge.net" <libusbx-devel@lists.sourceforge.net>,
    Libusb mailing list <libusb-devel@lists.sourceforge.net>
    date:	 11 juillet 2013 11:52


Hi All,

I'm very happy to announce the official libusbx-1.0.16 release!

Highlights of changes since 1.0.15
-----------------------------------


As Nathan Hjelm already announced in his "libusb and libusbx
merging" mail, Nathan has taken over libusb maintenance and
this release is a combined effort between the libusb and
libusbx projects!

* Hotplug support for Darwin and Linux

* Superspeed endpoint companion and BOS descriptor support

* We finally have a libusb_strerror API

You can download the 1.0.16 tarbal here:
http://downloads.sourceforge.net/libusbx/libusbx-1.0.16.tar.bz2

Please give it a thorough testing, and report any issues you
find.

For those interested the full ChangeLog is below.

Regards,

Hans


2013-07-11: v1.0.16
--------------------

* Add hotplug support for Darwin and Linux (#9)
* Add superspeed endpoint companion descriptor support (#15)
* Add BOS descriptor support (#15)
* Make descriptor parsing code more robust
* New libusb_get_port_numbers API, this is libusb_get_port_path without
  the unnecessary context parameter, libusb_get_port_path is now deprecated
* New libusb_strerror API (#14)
* New libusb_set_auto_detach_kernel_driver API (#17)
* Improve topology API docs (#95)
* Logging now use a single write call per log-message, avoiding log-message
  "interlacing" when using multiple threads.
* Android: use Android logging when building on Android (#101)
* Darwin: make libusb_reset reenumerate device on descriptors change (#89)
* Darwin: add support for the LIBUSB_TRANSFER_ADD_ZERO_PACKET flag (#91)
* Darwin: add a device cache (#112, #114)
* Examples: Add sam3u_benchmark isochronous example by Harald Welte (#109)
* Many other bug fixes and improvements

The (#xx) numbers are libusbx issue numbers, see ie:

https://github.com/libusbx/libusbx/issues/9


