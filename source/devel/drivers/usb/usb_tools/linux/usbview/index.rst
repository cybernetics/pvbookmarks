

.. index::
   pair: USB ; usbview (linux)


.. _linix_usbview:

=============
Linux Usbview
=============

.. seealso::

   - http://github.com/gregkh/usbview/


.. contents::
   :depth: 3

Introduction
============


A version of USBView is available for Linux from  http://www.kroah.com/linux-usb/.
As with the Windows version, this displays a connection tree of all the USB
devices connected to the PC.  A version compiled for x86_64 Linux can be
downloaded here_ .

.. _here: http://www.ftdichip.com/Resources/Utilities/usbview_x86_64.tar.gz


The source
==========

::

    git clone https://github.com/gregkh/usbview.git
    Cloning into usbview...
    remote: Counting objects: 312, done.
    remote: Compressing objects: 100% (171/171), done.
    remote: Total 312 (delta 168), reused 233 (delta 131)
    Receiving objects: 100% (312/312), 662.53 KiB | 195 KiB/s, done.
    Resolving deltas: 100% (168/168), done.


Tree
----

::


    |-- AUTHORS
    |-- COPYING
    |-- ChangeLog
    |-- INSTALL
    |-- Makefile.am
    |-- NEWS
    |-- README
    |-- TODO
    |-- about-dialog.c
    |-- autogen.sh
    |-- callbacks.c
    |-- config.h.in
    |-- configure-dialog.c
    |-- configure.in
    |-- debian
    |   |-- changelog
    |   |-- compat
    |   |-- control
    |   |-- copyright
    |   |-- rules
    |   |-- usbview.desktop
    |   |-- usbview.dirs
    |   |-- usbview.docs
    |   |-- usbview.manpages
    |   `-- usbview.menu
    |-- interface.c
    |-- main.c
    |-- showmessage.c
    |-- usb_icon.xpm
    |-- usbparse.c
    |-- usbparse.h
    |-- usbtree.c
    |-- usbtree.h
    |-- usbview.8
    |-- usbview.spec
    |-- usbview_logo.xcf
    `-- usbview_logo.xpm

Installation
============

> ./autogen.sh
>
