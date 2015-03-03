
.. index::
   pair: Libusbx ; 1.0.13


.. _libusbx_1.0.13:

============================
libusbx 1.0.13 (2012-09-20)
============================


.. seealso::

   - http://sourceforge.net/projects/libusbx/files/releases/1.0.13/


* [MAJOR] Fix a typo in the API with struct libusb_config_descriptor where
  MaxPower was used instead of bMaxPower, as defined in the specs. If your
  application was accessing the MaxPower attribute, and you need to maintain
  compatibility with libusb or older versions, see APPENDIX A below.
* Fix broken support for the 0.1 -> 1.0 libusb-compat layer
* Fix unwanted cancellation of pending timeouts as well as major timeout related bugs
* Fix handling of HID and composite devices on Windows
* Introduce LIBUSBX_API_VERSION macro
* Add Cypress FX/FX2 firmware upload sample, based on fxload from
  http://linux-hotplug.sourceforge.net
* Add libusb0 (libusb-win32) and libusbK driver support on Windows. Note that while
  the drivers allow it, isochronous transfers are not supported yet in libusbx. Also
  not supported yet is the use of libusb-win32 filter drivers on composite interfaces
* Add support for the new get_capabilities ioctl on Linux and avoid unnecessary
  splitting of bulk transfers
* Improve support for newer Intel and Renesas USB 3.0 controllers on Windows
* Harmonize the device number for root hubs across platforms
* Other bug fixes and improvements

