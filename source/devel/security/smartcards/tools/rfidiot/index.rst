

.. index::
   pair: RFID; rfidiot

.. _rfidiot:

=======
rfidiot
=======

.. seealso::

   - https://github.com/AdamLaurie/RFIDIOt
   - http://rfidiot.org/


.. contents::
   :depth: 2

Introduction
============


RFIDIOt is an open source python library for exploring RFID devices.
It's called "RFIDIOt" for two reasons:

1. I like puns. This one stands for "RFID IO tools"
2. Since I haven't done any serious programming for a long time, I felt
   like an idiot having to learn a whole new language and the code probably
   looks like it's written by an idiot.
   However, python rocks, so it was worth it!

What does it do?
================

It currently drives a range of RFID readers made by ACG, called the HF Dual ISO and HF Multi ISO,
which are both 13.56MHz devices, and the LF MultiTag which is 125/134.2kHz.

Frosch Hitag reader/writers are also now supported. There's no reason it couldn't work with others,
these are just the first ones I got my hands on, and since they present themselves to
the O/S as standard serial devices without having to install any drivers, it made interfacing
very simple (but see the Technical Note section below as I've had some issues recently).

I have written some example programs to read/write tags and have started on the library
routines to handle the data structures of specific tags like MIFARE®. It is far from complete
but I thought I'd follow the "publish early, publish often" philosophy on this one...

PC/SC (MUSCLE) devices, such as the Omnikey CardMan are also supported.
I am curently testing with a CardMan 5321.

Source code
============

- https://github.com/AdamLaurie/RFIDIOt



Dependencies
============

RFIDIOt uses a number of external libraries which will also need to be installed:

- pySerial
- pyscard
- pycrypto
- pycrypto for Windows
- pyreadline for Windows
- PIL (Python Imaging Library)









