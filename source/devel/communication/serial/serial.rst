
.. index::
   pair: Serial ; Communication
   pair: Série ; Serial
   ! Console
   ! RS232

.. _serial_communication:

======================
Serial Communication
======================


.. seealso::
                                                      
   - http://en.wikipedia.org/wiki/Virtual_serial_port
   - http://www.webalice.it/fede.tft/serial_port/serial_port.html
   - http://en.wikibooks.org/wiki/Serial_Programming/Serial_Linux

.. contents::
   :depth: 3

Introduction
============

The serial port protocol is one of the most long lived protocols currently
in use.

According to wikipedia, it has been standardized in 1969. First, a note: here
we're talking about the RS232 serial protocol. This note is necessary because
there are many other serial protocols, like SPI, I2C, CAN, and even USB and SATA.

Some time ago, when the Internet connections were done using a 56k modem,
the serial port was the most common way of connecting a modem to a computer.
Now that we have ADSL modems, the serial ports have disappeared from newer
computers, but the protocol is still widely used.

In fact, most microcontrollers, even the newer ones have one or more peripherals
capable of communicating using this protocol, and from the PC side, all operating
systems provide a way of interfacing with serial devices.
The problem of the lack of serial ports on computers was solved with USB to serial
converters, often embedded into the device itself.

One of such devices is the Arduino. While the first models had a serial
port connector, newer models has an USB port. However, nothing has changed on
the microcontroller side, nor on the PC side.

Simply the newer Arduinos have a chip that performs the serial to USB conversion.


Implementation
==============

.. toctree::
   :maxdepth: 4

   c/index
   cplusplus/index
   csharp/index
   python/index
   terminal_emulators/terminal_emulators





