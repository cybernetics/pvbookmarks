

.. index::
   pair: libpcsclite ; version 1.6.2


.. _libpcsclite_1.6.2:

=================
libpcsclite 1.6.2
=================


The libpcsclite 1.6.2 version is an important version which is adapted
to the :ref:`libccid 1.4.0 version <libccid_1.4.0>`

- http://ludovicrousseau.blogspot.com/2010/08/new-ccid-140-and-card-movement.html

The same day of the libcid 1.4.0 release I also released pcsc-lite 1.6.2.

Changes pcsc-lite-1.6.2: Ludovic Rousseau, 4 August 2010:

* implement a "Forced suicide" mechanism. After 3 Ctrl-C without much reaction
  from pcscd (in fact the drivers) we force the suicide. Sometimes libusb is
  blocked in a kind of dead-lock and kill -9 was the only option.
* Add support of TAG_IFD_STOP_POLLING_THREAD to request the stop of the driver
  polling function.
* Avoid a division by 0. Closes [#312555] "simclist bug in pcsc-lite"
* if pcscd is started by libpcsclite then close all file handles except stdin,
  stdout and stderr so that pcscd does not confiscate resources allocated by
  the application
* in case of auto exit create a new session so that Ctrl-C on the application
  will not also quit pcscd
* src/hotplug_libusb.c: port from libusb-0.1 to libusb-1.0
* default configuration is now $sysconfdir/reader.conf.d
* fix crash with empty config dir
* src/PCSC/winscard.h: Remove definitions of SCARD_READERSTATE_A,
  PSCARD_READERSTATE_A and LPSCARD_READERSTATE_A types
* some other minor improvements and bug corrections



















