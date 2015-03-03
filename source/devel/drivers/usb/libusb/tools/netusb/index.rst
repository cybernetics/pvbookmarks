


.. index::
   pair: USB; dotnet


.. _usbdotnet:

===========
USB dotnet
===========

.. seealso::

   - http://www.icsharpcode.net/OpenSource/SharpUSBLib/default.aspx


usblib (SharpUSBLib) is a wrapper around the `libusb project`_ (WIN32), thus you
must have it installed prior to using #usblib.

Mike started this project because he wanted to program a power switch
(GEMBIRD SIS-PM) with a USB port and didn't find any .NET USB library.

One goal is to provide a platform independent (Linux/Win32 solution) USB access
layer for .NET.


.. _`libusb project`:  http://libusb-win32.sourceforge.net/


License
=======


The library is dual-licensed: GPL or LGPL. The latter allows you to use the
library in closed-source applications (when you link against the library,
including the source code is still not allowed - it has to be in a separate assembly).

Download
========


Downloads are hosted on sf.net together with our #develop and #ziplib projects:
Get the latest version (source, binary, samples, documentation)
