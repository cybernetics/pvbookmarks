

.. index::
   pair: USB; usbmon
   ! usbmon

.. _usbmon:

======
usbmon
======

.. contents::
   :depth: 3

Introduction
============


The name "usbmon" in lowercase refers to a facility in kernel which is
used to collect traces of I/O on the USB bus. This function is analogous
to a packet socket used by network monitoring tools such as tcpdump(1)
or Ethereal. Similarly, it is expected that a tool such as usbdump or
USBMon (with uppercase letters) is used to examine raw traces produced
by usbmon.

The usbmon reports requests made by peripheral-specific drivers to Host
Controller Drivers (HCD). So, if HCD is buggy, the traces reported by
usbmon may not correspond to bus transactions precisely. This is the same
situation as with tcpdump.

* How to use usbmon to collect raw text traces

Unlike the packet socket, usbmon has an interface which provides traces
in a text format. This is used for two purposes. First, it serves as a
common trace exchange format for tools while more sophisticated formats
are finalized. Second, humans can read it in case tools are not available.

To collect a raw text trace, execute following steps.

debugfs and usbmon (if not built into the kernel)
=================================================

.. index::
   debugfs usbmon

Mount debugfs
-------------

Mount debugfs (it has to be enabled in your kernel configuration)::

    mount -t debugfs none_debugs /sys/kernel/debug


usbmon module
-------------

Load the usbmon module (if built as module). This step is skipped
if usbmon is built into the kernel::

    modprobe usbmon


In our linux kernel configuartion the usbmon module is built with the
kernel.


Verify that bus sockets are present.
------------------------------------

With linux 2.6.18


::

    [root@houx usbmon]# cd /sys/kernel/debug/usbmon; ls;pwd
    1s  1t  2s  2t  3s  3t  4s  4t  5s  5t  6s  6t
    /sys/kernel/debug/usbmon



Now you can choose to either:

- use the socket '0u' (to capture packets on all buses), and skip
  to step #3,
- or find the bus used by your device with step #2.

This allows to filter away annoying devices that talk continuously.

Find which bus connects to the desired device
=============================================

cat /proc/bus/usb/devices
-------------------------


Run::

    cat /proc/bus/usb/devices


and find the T-line which corresponds to the device.
Usually you do it by looking for the vendor string. If you have
many similar devices, unplug one and compare two /proc/bus/usb/devices outputs.
The T-line will have a bus number. Example::

    T:  Bus=04 Lev=01 Prnt=01 Port=01 Cnt=01 Dev#=  2 Spd=12  MxCh= 0
    D:  Ver= 2.00 Cls=ff(vend.) Sub=ff Prot=ff MxPS= 8 #Cfgs=  1
    P:  Vendor=0b81 ProdID=0103 Rev= 0.01
    S:  Manufacturer=id3 Semiconductors
    S:  Product=CERTIS 2
    S:  SerialNumber=0137064
    C:* #Ifs= 1 Cfg#= 1 Atr=80 MxPwr=200mA
    I:  If#= 0 Alt= 0 #EPs= 0 Cls=ff(vend.) Sub=00 Prot=00 Driver=(none)
    I:  If#= 0 Alt= 1 #EPs= 3 Cls=ff(vend.) Sub=00 Prot=00 Driver=(none)
    E:  Ad=83(I) Atr=01(Isoc) MxPS= 532 Ivl=1ms
    E:  Ad=02(O) Atr=02(Bulk) MxPS=  32 Ivl=0ms
    E:  Ad=82(I) Atr=02(Bulk) MxPS=  32 Ivl=0ms
    I:  If#= 0 Alt= 2 #EPs= 3 Cls=ff(vend.) Sub=00 Prot=00 Driver=(none)
    E:  Ad=83(I) Atr=01(Isoc) MxPS= 692 Ivl=1ms
    E:  Ad=02(O) Atr=02(Bulk) MxPS=  32 Ivl=0ms
    E:  Ad=82(I) Atr=02(Bulk) MxPS=  32 Ivl=0ms
    I:  If#= 0 Alt= 3 #EPs= 3 Cls=ff(vend.) Sub=00 Prot=00 Driver=(none)
    E:  Ad=83(I) Atr=01(Isoc) MxPS= 868 Ivl=1ms
    E:  Ad=02(O) Atr=02(Bulk) MxPS=  32 Ivl=0ms
    E:  Ad=82(I) Atr=02(Bulk) MxPS=  32 Ivl=0ms
    I:  If#= 0 Alt= 4 #EPs= 2 Cls=ff(vend.) Sub=00 Prot=00 Driver=(none)
    E:  Ad=02(O) Atr=02(Bulk) MxPS=  32 Ivl=0ms
    E:  Ad=82(I) Atr=02(Bulk) MxPS=  32 Ivl=0ms


lsusb
-----


or::

    lsusb


::

    [root@houx ~]# lsusb
    Bus 001 Device 001: ID 0000:0000
    Bus 001 Device 002: ID 0bda:0111 Realtek Semiconductor Corp. Card Reader
    Bus 003 Device 001: ID 0000:0000
    Bus 004 Device 002: ID 0b81:0103 id3 Semiconductors
    Bus 004 Device 001: ID 0000:0000
    Bus 005 Device 001: ID 0000:0000
    Bus 006 Device 001: ID 0000:0000
    Bus 002 Device 001: ID 0000:0000
    [root@houx ~]#



Bus=04 means it's bus 4

Start 'cat'
===========

::

    sudo cat /sys/kernel/debug/usbmon/4t > /tmp/usb.log


to listen on a single bus.


This process will be reading until killed. Naturally, the output can be
redirected to a desirable location. This is preferred, because it is going
to be quite long.

Perform the desired operation on the USB bus
============================================

This is where you do something that creates the traffic: plug in a flash key,
copy files, control a webcam, etc.

Kill cat
========

Usually it's done with a keyboard interrupt (Control-C).

At this point the output file (/tmp/1.mon.out in this example) can be saved,
sent by e-mail, or inspected with a text editor. In the last case make sure
that the file size is not excessive for your favourite editor.

Raw text data formats [1t, 1u]
==============================

Two formats are supported currently: the original, or '1t' format, and
the '1u' format.

1t format
---------

The '1t' format is deprecated in kernel 2.6.21.


1u format
---------

The '1u' format adds a few fields, such as ISO frame descriptors, interval, etc.
It produces slightly longer lines, but otherwise is a perfect superset
of '1t' format.

If it is desired to recognize one from the other in a program, look at the
"address" word (see below), where '1u' format adds a bus number. If 2 colons
are present, it's the '1t' format, otherwise '1u'.

Any text format data consists of a stream of events, such as URB submission,
URB callback, submission error. Every event is a text line, which consists
of whitespace separated words. The number or position of words may depend
on the event type, but there is a set of words, common for all types.

Here is the list of words, from left to right:

- URB Tag. This is used to identify URBs, and is normally an in-kernel address
  of the URB structure in hexadecimal, but can be a sequence number or any
  other unique string, within reason.

- Timestamp in microseconds, a decimal number. The timestamp's resolution
  depends on available clock, and so it can be much worse than a microsecond
  (if the implementation uses jiffies, for example).

- Event Type. This type refers to the format of the event, not URB type.
  Available types are: S - submission, C - callback, E - submission error.

- "Address" word (formerly a "pipe"). It consists of four fields, separated by
  colons: URB type and direction, Bus number, Device address, Endpoint number.
  Type and direction are encoded with two bytes in the following manner:

    * Ci Co   Control input and output
    * Zi Zo   Isochronous input and output
    * Ii Io   Interrupt input and output
    * Bi Bo   Bulk input and output

  Bus number, Device address, and Endpoint are decimal numbers, but they may
  have leading zeros, for the sake of human readers.

- URB Status word. This is either a letter, or several numbers separated
  by colons: URB status, interval, start frame, and error count. Unlike the
  "address" word, all fields save the status are optional. Interval is printed
  only for interrupt and isochronous URBs. Start frame is printed only for
  isochronous URBs. Error count is printed only for isochronous callback
  events.

  The status field is a decimal number, sometimes negative, which represents
  a "status" field of the URB. This field makes no sense for submissions, but
  is present anyway to help scripts with parsing. When an error occurs, the
  field contains the error code.

  In case of a submission of a Control packet, this field contains a Setup Tag
  instead of an group of numbers. It is easy to tell whether the Setup Tag is
  present because it is never a number. Thus if scripts find a set of numbers
  in this word, they proceed to read Data Length (except for isochronous URBs).
  If they find something else, like a letter, they read the setup packet before
  reading the Data Length or isochronous descriptors.

- Setup packet, if present, consists of 5 words: one of each for bmRequestType,
  bRequest, wValue, wIndex, wLength, as specified by the USB Specification 2.0.
  These words are safe to decode if Setup Tag was 's'. Otherwise, the setup
  packet was present, but not captured, and the fields contain filler.

- Number of isochronous frame descriptors and descriptors themselves.
  If an Isochronous transfer event has a set of descriptors, a total number
  of them in an URB is printed first, then a word per descriptor, up to a
  total of 5. The word consists of 3 colon-separated decimal numbers for
  status, offset, and length respectively. For submissions, initial length
  is reported. For callbacks, actual length is reported.

- Data Length. For submissions, this is the requested length. For callbacks,
  this is the actual length.

- Data tag. The usbmon may not always capture data, even if length is nonzero.
  The data words are present only if this tag is '='.

- Data words follow, in big endian hexadecimal format. Notice that they are
  not machine words, but really just a byte stream split into words to make
  it easier to read. Thus, the last word may contain from one to four bytes.
  The length of collected data is limited and can be less than the data length
  report in Data Length word.
