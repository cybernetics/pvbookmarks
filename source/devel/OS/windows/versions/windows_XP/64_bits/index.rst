
.. index::
   pair: Windows OS; windows XP 64bits

.. _windows_XP_64bits:

===================
Windows XP 64 (5.2)
===================

.. seealso:: http://en.wikipedia.org/wiki/Windows_XP_64-bit_Edition

Windows XP Professional x64 Edition uses version 5.2.3790.1830 of core operating
system binaries, the same version used by Windows Server 2003 SP1 as they were
the latest versions during the operating system's development.
Even service packs and updates for Windows XP x64 and Windows Server 2003 x64
are distributed in unified packages, much in the manner as Windows 2000 Professional
and Server editions for x86.

Windows backend on XP x64
=========================

::

    from    Xiaofan Chen <xiaofanc@gmail.com>
    to  Pete Batard <pbatard@gmail.com>
    cc  libusb-devel@lists.sourceforge.net
    date    Thu, Apr 15, 2010 at 2:23 PM
    subject Re: [Libusb-devel] Windows backend on XP x64

On Thu, Apr 15, 2010 at 6:45 PM, Pete Batard <pbatard@gmail.com> wrote:
> On 2010.04.15 02:42, Jerome Vuarand wrote:
>> I know that there is no way to have WinUSB on that OS,
>
> Is that true? WinUSB is available for XP 32, and we have the 64 bit
> drivers for Vista and later, which I would assume are compatible with XP
> 64. Is that not the case?

It is true that WinUSB is not officially supported by Microchip
on Windows Server 2003 and XP64.

http://msdn.microsoft.com/en-us/library/ff540196%28VS.85%29.aspx

Just take note XP64 is not XP actually. 

**It is Win 2003 in terms of the kernel**

...

http://en.wikipedia.org/wiki/Microsoft_Windows
XP 64 is the same as Windows server 2003 (NT5.2).
So you need to detect that as well.


::


    from    Jerome Vuarand <jerome.vuarand@gmail.com>
    to  Xiaofan Chen <xiaofanc@gmail.com>
    cc  libusb-devel@lists.sourceforge.net
    date    Thu, Apr 15, 2010 at 2:48 PM
    subject Re: [Libusb-devel] Windows backend on XP x64



> http://en.wikipedia.org/wiki/Microsoft_Windows
> XP 64 is the same as Windows server 2003 (NT5.2). So you
> need to detect that as well.

I think that's the source of the problem. The following page list
Windows versions :

http://msdn.microsoft.com/en-us/library/ms724832.aspx

And as Xiaofan Chen mentionned, Windows XP x64 has version 5.2. But
the libusb code looks like that.

.. code-block:: c

   windows_version = WINDOWS_UNSUPPORTED;
   if ((GetVersionEx(&os_version) != 0) && (os_version.dwPlatformId ==
   VER_PLATFORM_WIN32_NT)) {
       if ((os_version.dwMajorVersion == 5) && (os_version.dwMinorVersion == 1)) {
           windows_version = WINDOWS_XP;
       } else if (os_version.dwMajorVersion >= 6) {
           windows_version = WINDOWS_VISTA_AND_LATER;
       }
   }


The third line should be changed to

.. code-block:: c

   if ((os_version.dwMajorVersion == 5) && (os_version.dwMinorVersion >= 1)) {



That should fix the issue for both XP x64 and Server 2003 versions of Windows.

