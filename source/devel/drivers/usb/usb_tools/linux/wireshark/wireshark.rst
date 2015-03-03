

.. index::
   pair: USB ; Wireshark
   pair: Wireshark ; USB sniffer


.. _wireshark:

=========
Wireshark
=========

.. seealso::

   - :ref:`wireshark_secur`

.. contents::
   :depth: 3

Introduction
============

Sources:

- http://wiki.wireshark.org/CaptureSetup/USB
- http://fr.wikipedia.org/wiki/Wireshark

usbmon
------


To dump USB traffic on Linux, you need the :ref:`usbmon` module, which has
existed since Linux 2.6.11.

Information on that module is available in /usr/src/linux/Documentation/usb/usbmon.txt
in the Linux source tree.

Depending on the distribution you're using, and the version of that distribution,
that module might be built into the kernel, or might be a loadable module; if it's a
loadable module, depending on the distribution you're using, and the version of
that distribution, it might or might not be loaded for you.

.. note::
   On centos it's built into the kernel

If it's a loadable module, and not loaded, you will have to load it with the command::

    modprobe usbmon

which must be run as root.

libcap
------

libpcap releases prior to 1.0 do not include USB support, so you will need at
least libpcap 1.0.0.

.. warning::
   on centos we have libpcap-0.9.4-15.el5.i386


linux kernel
------------

For versions of the kernel prior to 2.6.21, the only USB traffic capture mechanism
available is a text-based mechanism that limits the total amount of data captured
for each raw USB block to about 30 bytes.

.. warning::
   on centos the linux kernel is 2.6.18


There is no way to change this without patching the kernel.


If debugfs is not already mounted on /sys/kernel/debug, ensure that it is mounted there
by issuing the following command as root::

      mount -t debugfs / /sys/kernel/debug

.. note::  For kernel version 2.6.21 and later, there is a binary protocol for
           tracing USB packets which doesn't have that size limitation.

For that kernel version, you will need :ref:`libpcap 1.1.0 or newer <libpcap>`, because
the libpcap 1.0.x USB support uses, but does not correctly handle, the memory-mapped
mechanism for USB traffic, which libpcap will use if available - it cannot be
made unavailable, so libpcap will always use it.

- In libpcap 1.0.x, the devices for capturing on USB have the name usbn,
  where n is the number of the bus.
- In libpcap 1.1.0 and later, they have the name usbmonn.


You will also need a **Wireshark 1.2.x or newer**.

.. warning::
   on centos we have wireshark-1.0.15-1.el5_5.1.i386


Wireshark Installation
======================

$Id: INSTALL 32440 2010-04-09 21:42:51Z gerald $

NOTE: this document applies to the Wireshark source releases and
buildbot source tarballs.

It does not apply to source code checked out directly from Subversion,
as files such as the configuration script are not checked into Subversion,
but need to be generated from the autoconf and automake files.

See http://wiki.wireshark.org/Development if you would like to build
the source code checked out directly from Subversion.


.. index::
   GTK

Installation on centos
======================

GTK configuration
-----------------

::

    export PATH=/opt/gtk2/bin:$PATH
    export PKG_CONFIG_PATH=/opt/gtk2/lib/pkgconfig
    export LD_LIBRARY_PATH=/opt/gtk2/lib:$LD_LIBRARY_PATH
    pkg-config glib-2.0 --modversion


2.24.1


libpcap configuration
---------------------


::

    --with-pcap=DIR
        Use this to tell Wireshark where you have libpcap installed, if
        it is installed in a non-standard location.



autogen.sh
----------

    >  ./autogen.sh

        Checking for python.
        You must have autoconf 2.60 or later installed to compile Wireshark.
        Download the appropriate package for your distribution/OS,
        or get the source tarball at ftp://ftp.gnu.org/pub/gnu/autoconf/


.. warning::  autoconf-2.59-12.noarch on centos


.. seealso:: :ref:`autoconf`

::

    > autogen.sh


Results

::

    $ wireshark-1.4.2$ ./autogen.sh
    checking for python.
    aclocal -I ./aclocal-fallback
    libtoolize --copy --force
    libtoolize: putting auxiliary files in `.'.
    libtoolize: copying file `./ltmain.sh'
    libtoolize: Consider adding `AC_CONFIG_MACRO_DIR([m4])' to configure.in and
    libtoolize: rerunning libtoolize, to keep the correct libtool macros in-tree.
    libtoolize: Consider adding `-I m4' to ACLOCAL_AMFLAGS in Makefile.am.
    autoheader
    automake --add-missing --gnu
    configure.in: installing `./ylwrap'
    autoconf
    Now type "./configure [options]" and "make" to compile Wireshark.


./configure --prefix=/opt/wireshark  --with-pcap=/opt/libpcap/current -with-python
----------------------------------------------------------------------------------

::

    ...
    checking for pkg-config... /usr/bin/pkg-config
    checking for GTK+ - version >= 2.4.0... yes (version 2.20.1)
    checking for pkg-config... (cached) /usr/bin/pkg-config
    checking for GLIB - version >= 2.4.0... yes (version 2.24.1)
    checking for GLIB - version >= 2.14.0... yes
    checking whether GLib supports loadable modules... yes
    ...

    > configure --prefix=/opt/wireshark  --with-pcap=/opt/libpcap/current -with-python
    The Wireshark package has been configured with the following options.
                        Build wireshark : yes
                           Build tshark : yes
                         Build capinfos : yes
                          Build editcap : yes
                          Build dumpcap : yes
                         Build mergecap : yes
                        Build text2pcap : yes
                          Build idl2wrs : yes
                          Build randpkt : yes
                           Build dftest : yes
                         Build rawshark : yes

      Install dumpcap with capabilities : no
                 Install dumpcap setuid : no
                      Use dumpcap group : (none)
                            Use plugins : yes
                        Use lua library : no
                     Use python binding : yes
                       Build rtp_player : no
                            Use threads : no
                 Build profile binaries : no
                       Use pcap library : yes
                       Use zlib library : yes
                       Use pcre library : no (using GRegex instead)
                   Use kerberos library : yes (MIT)
                     Use c-ares library : no
                   Use GNU ADNS library : no
                    Use SMI MIB library : no
                 Use GNU crypto library : yes
                 Use SSL crypto library : no
               Use IPv6 name resolution : yes
                     Use gnutls library : no
         Use POSIX capabilities library : yes
                      Use GeoIP library : no


.. index::
   pair: Python ;  Wireshark


Wireshark python
================

.. seealso:: http://wiki.wireshark.org/Python


- export LD_LIBRARY_PATH=/opt/libpcap/current:$LD_LIBRARY_PATH
- export PATH=/opt/wireshark/bin:$PATH


Extending Wireshark with Python
--------------------------------

Note: This isn't yet supported on Windows (see Bug 3500)

The projects aim is to give the possibility to developers to easily extend
Wireshark with Python.

It is a project in development and therefore is experimental.
It is better to not use this in production for now.
It is good though for prototyping as the syntax is rather concise.

It is better to have read doc/README.developer and doc/README.python before attempting to play with the Python API.

Requirements
------------

You must have a valid Python environment (python >= 2.3) and ctypes.
ctypes is part of the Python package from the version 2.5. If you have an older version, you have to install it yourself.

Compile with Python support::

    ./configure --with-python


export LD_LIBRARY_PATH=/opt/libpcap/current:$LD_LIBRARY_PATH
export PATH=/opt/wireshark/bin:$PATH

