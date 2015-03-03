
.. index::
   pair: C#; HID
   pair: Simple; HID library


.. _csharp_simplehid:

====================
C# simplehidlibrary
====================

.. seealso::

   - http://simplehidlibrary.codeplex.com/


.. contents::
   :depth: 3


Project Description
===================

Simple and small managed HID library for .NET 4 x86/x64. Can communicate with
any HID USB device. Uses P/Invoke internally, no mixed mode assemblies or
unmanged code.


Project Goals
=============

.. seealso::

   - msdn.microsoft.com/en-us/library/windows/hardware/ff538865%28v=vs.85%29.aspx

This project aims to make it simple to communicate with a HID USB device.

This library will use the `HidD/HidP API`_. All "report parsing" is done, you will
not handle raw report data. This library uses Usage Page/Usage as input/output.

The project is created so that I can learn this API.


.. _`HidD/HidP API`: msdn.microsoft.com/en-us/library/windows/hardware/ff538865%28v=vs.85%29.aspx
