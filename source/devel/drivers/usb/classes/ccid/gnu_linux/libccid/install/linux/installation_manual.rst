
.. index::
   libccid installation


.. _libccid_manual_installation:

===========================
libccid manual Installation
===========================

Source: http://pcsclite.alioth.debian.org/ccid.html#CCID_compliant


.. warning:: pcsclite must be installed before libccid.


.. _libccid_installation_on_gnu_linux:

libccid Installation on GNU/Linux
=================================

::

    bunzip2 ccid-x.y.z.tar.bz2
    tar xvf ccid-x.y.z.tar
    cd ccid-x.y.z
    ./configure PCSC_CFLAGS=-I/opt/pcsclite/current/include/PCSC LIBUSB_CFLAGS=-I/opt/libusb/current/include/libusb-1.0 LIBUSB_LIBS="-L/opt/libusb/current/lib -lusb-1.0"  PCSC_LIBS="-L/opt/pcsclite/current/lib -lpcsclite"  -enable-usbdropdir=/opt/pcsclite/current/drivers 


Example for libccid 1.4.3
-------------------------

::

    ./configure PCSC_CFLAGS=-I/opt/pcsclite/current/include/PCSC LIBUSB_CFLAGS=-I/opt/libusb/current/include/libusb-1.0 LIBUSB_LIBS="-L/opt/libusb/current/lib -lusb-1.0"  PCSC_LIBS="-L/opt/pcsclite/current/lib -lpcsclite"  -enable-usbdropdir=/opt/pcsclite/current/drivers 


:: 


	libccid has been configured with following options:
	Version:             1.4.3
	User binaries:       /opt/ccid/1.4.3/bin
	Configuration files: /opt/ccid/1.4.3/etc
	Host:                i686-pc-linux-gnu
	Compiler:            gcc
	Preprocessor flags:  
	Compiler flags:      -g -O2
	Preprocessor flags:  
	Linker flags:        
	Libraries:           
	PCSC_CFLAGS:         -I/opt/pcsclite/current/include/PCSC
	PCSC_LIBS:           -L/opt/pcsclite/current/lib -lpcsclite
	PTHREAD_CFLAGS:      -pthread
	PTHREAD_LIBS:        
	BUNDLE_HOST:         Linux
	DYN_LIB_EXT:         so
	LIBUSB_CFLAGS:       -I/opt/libusb/current/include/libusb-1.0
	LIBUSB_LIBS:         -L/opt/libusb/current/lib -lusb-1.0
	SYMBOL_VISIBILITY:   -fvisibility=hidden
	NOCLASS:             
	libusb support:          yes
	composite as multislot:  no
	multi threading:         yes
	bundle directory name:   ifd-ccid.bundle
	USB drop directory:      /opt/pcsclite/current/drivers
	serial Twin support:     no
	serial twin install dir: /serial
	compiled for pcsc-lite:  yes
	class driver:            yes



make
----


make install
------------

::

	copy the src/92_pcscd_ccid.rules file in udev directory (/etc/udev/rules.d/)
	

After make install
++++++++++++++++++

.. seealso::  :ref:`usbids` 

::


	├── drivers
	│   └── ifd-ccid.bundle
	│       └── Contents
	│           ├── Info.plist
	│           └── Linux
	│               └── libccid.so
	├── include
	│   └── PCSC
	│       ├── debuglog.h
	│       ├── ifdhandler.h
	│       ├── pcsclite.h
	│       ├── reader.h
	│       ├── winscard.h
	│       └── wintypes.h
	├── lib
	│   ├── libpcsclite.la
	│   ├── libpcsclite.so -> libpcsclite.so.1.0.0
	│   ├── libpcsclite.so.1 -> libpcsclite.so.1.0.0
	│   ├── libpcsclite.so.1.0.0
	│   └── pkgconfig
	│       └── libpcsclite.pc
	├── sbin
	│   └── pcscd
	└── share
		├── doc
		│   └── pcsc-lite
		│       └── README.DAEMON
		└── man
			├── man5
			│   └── reader.conf.5
			└── man8
				└── pcscd.8




