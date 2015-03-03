.. module:: USB_muscle_news 
    :synopsis: pcsc muscle news 

    
===========
libusb_news
===========


Testers welcome for libusb-win32 snapshot release 20100505
==========================================================

::

	from	Xiaofan Chen <xiaofanc@gmail.com>
	to	libusb-devel@lists.sourceforge.net
	date	Thu, May 6, 2010 at 1:39 AM
	subject	[Libusb-devel] FYI: Testers welcome for libusb-win32 snapshot release 20100505
	mailing list	libusb-devel.lists.sourceforge.net Filter messages from this mailing list
	mailed-by	lists.sourceforge.net
	unsubscribe	Unsubscribe from this mailing-list
	
hide details May 6
	
Travis Robinson has pushed the new snapshot release 20100505, Please
go to libusb-win32 project page at Sourceforge to download this release.
http://sourceforge.net/projects/libusb-win32/

Major changes:

1. Travis is now the lead developer for libusb-win32 project.
2. License is updated to LGPL V3 (library) and GPL V3 (driver,
   installer, test program).
3. Fixed bug 2658937 (Filter driver should not be power policy owner).
   This should make the filter safer to use under XP/Vista/Win7.
4. If running as a device driver, default configuration will be set.
   If running as a filter driver, no configuration will be set.
5. Drop support for Windows 98SE and Windows ME. Win2k
   will the minimum required OS version.
6. Bump up the version (1.1.14.0) to facilitate Microsoft WHQL submission.
7. Change the build system to Microsoft WDK.
8. For more detailed changes, please refer to the subversion
   repository changelog.
   http://libusb-win32.svn.sourceforge.net/viewvc/libusb-win32/trunk/libusb/

We have done reasonable tests under different operating systems
for both the filter driver mode and the device driver mode. We are
reasonably sure that the new filter driver would not cause BSODs
or make the USB subsystem malfunction. Nevertheless, this is
a snapshot release and quite possibly there are still bugs so that
you still need to carry out due diligence especially with the filter driver.

Early adopters are welcome to test this new snapshot release and
send in success/failure reports.

The support facilities are described here.
http://sourceforge.net/projects/libusb-win32/support

Mailing list is the preferred support channel. Bug report, patches and
feature request are also welcome through the tacker system. The
forum and support requests at SourceForge will be closed in the future.

The project website is now redirected to the following Trac Wiki.
http://sourceforge.net/apps/trac/libusb-win32/wiki



Identify the physical USB ports used by a driver handle
=======================================================


:: 

    from    Xiaofan Chen <xiaofanc@gmail.com>
    reply-to    libusb-win32-devel@lists.sourceforge.net
    to    libusb-win32-devel@lists.sourceforge.net
    date    Fri, Feb 19, 2010 at 3:47 PM
    subject    Re: [Libusb-win32-devel] Identify the physical USB ports used by a driver handle
    mailing list    <libusb-win32-devel.lists.sourceforge.net> Filter messages from this mailing list
    mailed-by    lists.sourceforge.net
    unsubscribe    Unsubscribe from this mailing-list
    
  
On Fri, Feb 19, 2010 at 6:10 PM, Patrik Thalin
<patrik.thalin@stericsson.com> wrote:
> Hi all,
>
> I am looking for a solution to identify the physical USB ports used by a
> device. I have looked at devcon in WDK to find the DeviceID eg.
> USB\VID_xxxx&PID_yyyy\6&6B42B9C&0&4. This seem to be a unique for the
> port used. I have successfully duplicated this to my application. By
> calling SetupDiGetDeviceRegistryProperty and SetupDiGetDeviceInstanceId.
> But I can't find a way to associate this to the driver handle. Can this
> be done?
>
>
> Any other suggestion on how identify the port is also welcome! Note that
> I can not use a serial number in the device it has to be unique for the
> USB port on the computer. Also note that I have several indentical units
> connected.
>

I do not know the answer. You may have better luck trying out
some other lists. The best one may be this newsgroup.
microsoft.public.development.device.drivers
http://groups.google.com/group/microsoft.public.development.device.drivers/topics

But it is said to be non-trivial for any OS.
http://old.nabble.com/Re%3A-how-to-get-device-info-from-mount-point-p16593540.html

Some say it is not possible under Windows.
http://www.winvistatips.com/uniquely-identify-usb-hid-device-t809662.html

Might be possible under Linux or Mac OS X.
http://old.nabble.com/How-to-get-the-Location-ID-and-Current-Available-information-on-linux--td25588308.html

--
Xiaofan http://mcuee.blogspot.com
- Show quoted text -

Question : libusb for 64-bit systems
====================================

::

    from    Don Raikes <DON.RAIKES@oracle.com>
    reply-to    libusb-win32-devel@lists.sourceforge.net
    to    libusb-win32-devel@lists.sourceforge.net
    date    Fri, Feb 26, 2010 at 9:16 PM
    subject    [Libusb-win32-devel] libusb for 64-bit systems
    mailing list    <libusb-win32-devel.lists.sourceforge.net> Filter messages from this mailing list
    mailed-by    lists.sourceforge.net
    

Hello,
I am new to this list, and in fact haven't used libusb-win32 at all yet.
I am upgrading to a 64-bit machine with windows 7 64-bit on it over this 
weekend. My question is:  is there a version of libusb-win that will 
work for windows 64-bit operating systems ?

Response 1
----------

There are many discussions of this topic in the mailing list. You can
check the archive.

Current version libusb-win32 already works under XP64. It will
also work under Vista 64 and Windows 7 64bit if you play some
tricks. The major problems is the digital signing of the kernel driver.
For example, this is a whole thread about this issue.
http://old.nabble.com/Windows-2008-x64-td24807435.html

Examples of the tricks if you can live with them:
http://forum.sparkfun.com/viewtopic.php?t=17655
http://nil-techno.blogspot.com/2008/08/installing-unsigned-drivers-on-vista-64.html

Now there is finally a viable alternative to libusb-win32: the
new libusb 1.0 Windows backend, it is now under pre-release mode
but there are issues to be sorted out so that it is integrated into the
main libusb 1.0 tree. It uses WinUSB and/or Windows HID as the
backend. Unless your device is using isochronous transfer, WinUSB
should work for you and it will work under all the 64bit Windows system.
URL: http://libusb.org/wiki/windows_backend

I have tried it and it works fine for me (both WinUSB backend and
HID backend). There are still issues (multi-thread and some other
issues) to be sorted out though. If you are interested, give it a try
and it will help if you subscribed to libusb mailing list. If you
encountered issues, do not hesitate to raise the questions there.
https://lists.sourceforge.net/lists/listinfo/libusb-devel
Archive: http://old.nabble.com/LibUSB-f14231.html


Response 2
----------

Of course, since one company has done the digital signing. If you are
doing things for your employer (Oracle), then you can probably get it
(paid by your company). The best is of course to contribute the things back
to the community and allow it to be used with their projects.
http://old.nabble.com/Building-Libusb-for-64-bit-Windows-Vista-and-Seven-td27260978.html

I am not sure if Pruftechnik will allow others to use their driver (WHQLed)
for other projects. If yes, then people can use it as well.

The driver is now ptlibusb0.sys (not libusb0.sys).
According to the following libusb-win32 forum thread (log-in to access
it), you need
to change the driver name but it seems the dll is still okay.
https://sourceforge.net/projects/libusb-win32/forums/forum/266688/topic/3536300

Quote:
It took me quite some effort and testing to come to this solution. I
could have lived with running windows in testmode, but this solution
is of course much better.

Now we only need to find out, which information in the inf file can be
changed without breaking the certification. Some things can be
renamed, but not everything.

Ciao,
Steffen

PS: While the driver and dll are renamed from libusb0 to ptlibusb0 which would
make it necessary to change the application which uses the lib, it
seems that the
original libusb0.dll can be used with the ptlibusb0.sys, so even
existing binaries
linking to libusb0.dll can work with this driver.

Response 3
----------

On Tue, Mar 2, 2010 at 6:36 AM, Don Raikes <DON.RAIKES@oracle.com> wrote:
> Hello,
> So I am in the process of installing libwinbackend.
>
> I have downloaded the files, and went into device manager to
> determine the vendor/product id for the device.
>
> I see the device listed in device manager as
> "alva satellite 544" but it has no device driver installed. I cannot figure
> out how to get the necessary vid and pid information. I checked all three
> tabs and none of them listed any numbers that would indicate these values.

There is information about VID/PID in device manager (called hardware id).

Anyway, you should use USBView instead since it is easier and give
you more information. It is part of WDK.
http://www.microsoft.com/whdc/devtools/wdk/wdkpkg.mspx

But if you do not want to download WDK (huge download), you can
get it here (FTDI's version).
http://www.ftdichip.com/Resources/Utilities.htm
http://www.ftdichip.com/Resources/Utilities/usbview.zip

You can of course get the information from Linux as well

:: 

    lsusb -vvv
    
    

.. index::
   autoinstaller
   inf windows wizard
   http://git.libusb.org/?p=libusb-pbatard.git;a=shortlog;h=refs/heads/winusb-autoinstall
   http://libusbdotnet.sourceforge.net/V2/html/8c7cc7dc-5b65-4fab-b2a2-54cf0b727a19.htm
   wizard
   libusb 1.0
   INF wizard
  
http://libusbdotnet.sourceforge.net/V2/Index.html
=================================================
  
libusbdotnetV2_ seems to have some big improvement.

.. _libusbdotnetV2: http://libusbdotnet.sourceforge.net/V2/Index.html


It supports libusb 1.0 under Linux and libusb-win32/WinUSB
under Windows. Maybe this will be of some interests to
some C# or DotNet users. I can only barely use C myself.

I found out this from the following Microchip forum thread.
http://www.microchip.com/forums/tm.aspx?m=480008



Some nice features I tested:
1) INF wizard to generate the INF file for WinUSB and libusb-win32
2) Device notification
http://libusbdotnet.sourceforge.net/V2/html/8c7cc7dc-5b65-4fab-b2a2-54cf0b727a19.htm

Example output if I reset the device::

    [DeviceType:DeviceInterface] [EventType:DeviceRemoveComplete]
    FullName:USB#VID_0925&PID_1456#5&207b166d&0&7#{a5dcbf10-6530-11d2-901f-00c04fb951ed}
    Vid:0x0925
    Pid:0x1456
    SerialNumber:5&207b166d&0&7
    ClassGuid:a5dcbf10-6530-11d2-901f-00c04fb951ed
    [DeviceType:DeviceInterface] [EventType:DeviceArrival]
    FullName:USB#VID_0925&PID_1456#5&207b166d&0&7#{a5dcbf10-6530-11d2-901f-00c04fb951ed}
    Vid:0x0925
    Pid:0x1456
    SerialNumber:5&207b166d&0&7
    ClassGuid:a5dcbf10-6530-11d2-901f-00c04fb951ed


:: 

    > Some nice features I tested:
    > 1) INF wizard to generate the INF file for WinUSB and libusb-win32
    > 2) Device notification

For what is worth, both of these features will be added to libusb after
our first release, and there's actual active development going on for
the inf/autoinstaller feature (that is, when other libusb stuff leaves
enough time for that): See

http://git.libusb.org/?p=libusb-pbatard.git;a=shortlog;h=refs/heads/winusb-autoinstall

But being able to check working auto-notification code on Windows might
prove quite helpful actually ;)

.. seealso:: :ref:`usbids`


.. index::
   Unified inf file
   inf
   libusb0.sys
   
Unified .inf
============

:: 


	from	Graeme Gill <graeme2@argyllcms.com>
	reply-to	graeme@argyllcms.com
	to	libusb-devel <libusb-devel@lists.sourceforge.net>
	date	Fri, Mar 19, 2010 at 6:12 AM
	subject	[Libusb-devel] Unified .inf
	mailing list	libusb-devel.lists.sourceforge.net Filter messages from this mailing list
	mailed-by	lists.sourceforge.net
	unsubscribe	Unsubscribe from this mailing-list
	
	Here <http://www.argyllcms.com/example.inf> is an example of a unified libusb0.sys
	& WinUSB .inf file, that I've had some success with, when combined with my libusb
	V1.0 libusb0.sys support.

	You can set which driver install (libusb0.sys, WinUSB with the CoInstallers, or
	WinUSB without the CoInstallers) for each Platform version (Win2K/XP/Vista/Win7/64).

	cheers,

	Graeme Gill.
	
	
.. index::
   libusb on cygwin
   http://cygwin.com/cgi-bin2/package-grep.cgi?grep=libusb
   
   
libusb-1.0 Windows Backend on cygwin
====================================

.. seealso:: http://cygwin.com/cgi-bin2/package-grep.cgi?grep=libusb


I accidentally found out libusb-1.0 Windows Backend is already inside
Cygwin packages yesterday during an installation of Cygwin.
http://www.cygwin.com/ml/cygwin-announce/2010-03/msg00005.html
http://cygwin.com/cgi-bin2/package-grep.cgi?grep=libusb

I have not tried it yet. The version is called libusb1.0-1.0.5+git03e9371a.	


::

	from	Xiaofan Chen <xiaofanc@gmail.com>
	to	René Hansen <renehh@gmail.com>
	cc	libusb-devel@lists.sourceforge.net
	date	Tue, Jun 1, 2010 at 3:53 AM
	subject	Re: [Libusb-devel] Windows-backend.
	mailing list	libusb-devel.lists.sourceforge.net Filter messages from this mailing list

On Tue, Jun 1, 2010 at 1:51 AM, René Hansen <renehh@gmail.com> wrote:

> I've been in contact with a company called All.com and on their
> behalf, I'm currently looking into the feasibility of porting a
> library like libgpod cross platform, with initial focus on Windows.
> Being able to to sync media devices like iPods and so on without
> iTunes is key for their project.

Not so sure if this helps. Yesterday I happened to come across
this library usbmuxd by Hector Martin.
http://www.libusb.org/wiki/Libusb1.0
http://marcansoft.com/blog/iphonelinux/usbmuxd/

As it is using libusb-1.0 and with bulk tarnsfer, probably the porting of
the libusb layer to Windows is not that difficult (with WinUSB backend).
It seems to use asynchronous transfer which is not heavily tested
for the Windows backend as far as I know. But hopefully it should
work.

Is libgpod using usbmuxd?

I do not have any iPod/iPhone though since I do not buy things
from Apple (and Sony except Sony Radios) in general.
