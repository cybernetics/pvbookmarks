

.. index::
   pair: USB ; classes
   pair: USB ; 0x0b  Smart Card
   pair: 0x0b  ; Smart Card

.. _USB_device_classes:

==================
USB device classes
==================

USB defines class codes used to identify a device’s functionality and to load
a device driver based on that functionality.

**This enables every device driver writer to support devices from different
manufacturers that comply with a given class code.**

=========    ==============   ================================   ===================================================================================================
Class        Usage            Description                        Examples
=========    ==============   ================================   ===================================================================================================
0x00         Device           Unspecifiedclass 0                 (Device class is unspecified. Interface descriptors are used for determining the required drivers)
0x01         Interface        Audio                              Speaker, microphone, sound card
0x02         Both             Communications and CDC Control     Ethernet adapter, modem
0x03         Interface        Human Interface Device (HID)       Keyboard, mouse, joystick
0x05         Interface        Physical Interface Device (PID)    Force feedback joystick
0x06         Interface        Image                              Webcam, scanner
0x07         Interface        Printer                            Laser printer, inkjet printer, CNC machine
0x08         Interface        Mass Storage                       USB flash drive, memory card reader, digital audio player, digital camera, external drive
0x09         Device           USB hub                            Full bandwidth hub
0x0a         Interface        CDC-Data                           (This class is used together with class 02h - Communications and CDC Control.)
0x0b         Interface        Smart Card                         USB smart card reader
0x0d         Interface        Content Security                   fingerprint reader
0x0e         Interface        Video                              Webcam
0x0f         Interface        Personal Healthcare                -
0xdc         Both             Diagnostic Device                  USB compliance testing device
0xe0         Interface        Wireless Controller                Wi-Fi adapter, Bluetooth adapter
0xef         Both             Miscellaneous                      ActiveSync device
0xfe         Interface        Application Specific               IrDA Bridge, Test & Measurement Class (USBTMC), DFU
0xff         Both             Vendor Specific                    (This class code indicates that the device needs vendor specific drivers.)
=========    ==============   ================================   ===================================================================================================


.. seealso:: :ref:`usb_dfu_firmware_upgrade`



Application Specific class example
==================================


::


    /*
     * dfu-programmer
     *
     * $Id: dfu.c 2706 2010-03-04 13:27:49Z pvergain $
     *
     * This program is free software; you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation; either version 2 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program; if not, write to the Free Software
     * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
     */

    #include <stdio.h>
    #include <stdarg.h>
    #include <stdint.h>
    #include <stddef.h>
    #include <usb.h>
    #include <errno.h>
    #include "dfu.h"
    #include "util.h"
    #include "dfu-bool.h"

    /* DFU commands */
    #define DFU_DETACH      0
    #define DFU_DNLOAD      1
    #define DFU_UPLOAD      2
    #define DFU_GETSTATUS   3
    #define DFU_CLRSTATUS   4
    #define DFU_GETSTATE    5
    #define DFU_ABORT       6

    #define USB_CLASS_APP_SPECIFIC  0xfe

    ..

