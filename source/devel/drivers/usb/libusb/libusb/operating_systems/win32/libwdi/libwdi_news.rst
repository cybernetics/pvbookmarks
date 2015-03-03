.. module:: libwdi_news
    :synopsis: libwdi news
    :platform: windows XP, Vista, windows 7

.. index:: 
   libwdi news
  
===========
libwdi news
===========

libwdi news
===========


libusb 1.0 Windows backend WDI branch testing (Tue, Mar 30, 2010 at 4:18 PM)
----------------------------------------------------------------------------


:: 


	from	Xiaofan Chen <xiaofanc@gmail.com>
	to	libusb-devel@lists.sourceforge.net
	date	Tue, Mar 30, 2010 at 4:18 PM
	subject	[Libusb-devel] libusb 1.0 Windows backend WDI branch testing
	mailing list	libusb-devel.lists.sourceforge.net Filter messages from this mailing list
	mailed-by	lists.sourceforge.net
	unsubscribe	Unsubscribe from this mailing-list
		
	hide details 4:18 PM (1 hour ago)
		
	I just build the WDI branch with WDK and it seems to work. Tested
	with the libusbdotnet Benchmark firmware (just change the PID to 0054
	instead of 0053 and can celled the Windows wizard).

	C:\cygwin\home\mcuee\mcu\libusb1win32\git\wdi\libusb-pbatard\WDK\Win32>setdrv.exe
	libwdi:debug [wdi_create_list] got hardware ID: USB\VID_04D8&PID_0054&REV_0000
	libwdi:debug [wdi_create_list] Driverless USB device (11): USB\VID_04D8&PID_0054
	\6&1DA2B8C1&0&3
	libwdi:debug [wdi_create_list] Device description: Microchip WinUSB
	Example Device
	Found driverless USB device: "Microchip WinUSB Example Device"
	(VID_04D8:PID_0054)
	Do you want to install a driver for this device (y/n)?
	y
	libwdi:debug [extract_binaries] successfully extracted files to C:\test
	libwdi:debug [wdi_create_inf] succesfully created C:\test\libusb-device.inf
	libwdi:debug [wdi_install_driver] all clean
	libwdi:debug [process_message] [installer process] got parameter
	libusb-device.inf
	libwdi:debug [process_message] got request for device_id
	libwdi:debug [process_message] [installer process] got device_id:
	USB\VID_04D8&PID_0054\6&1DA2B8C1&0&3
	libwdi:debug [process_message] got request for hardware_id
	libwdi:debug [process_message] [installer process] got hardware_id: USB\VID_04D8
	&PID_0054&REV_0000
	libwdi:debug [process_message] switching timeout to infinite
	libwdi:debug [process_message] [installer process] Installing driver -
	please wait...
	libwdi:debug [process_message] switching timeout back to finite
	libwdi:debug [process_message] [installer process] driver update completed
	libwdi:debug [process_message] [installer process] re-enumerating driver node
	USB\VID_04D8&PID_0054\6&1DA2B8C1&0&3...
	libwdi:debug [process_message] [installer process] re-enumeration succeeded...

	--
	Xiaofan http://mcuee.blogspot.com


Re: [Libusb-devel] libusb 1.0 Windows backend WDI branch testing Tue, Mar 30, 2010 at 4:55 PM
---------------------------------------------------------------------------------------------


:: 


	from	Pete Batard <pbatard@gmail.com>
	to	libusb-devel@lists.sourceforge.net
	date	Tue, Mar 30, 2010 at 4:55 PM
	subject	Re: [Libusb-devel] libusb 1.0 Windows backend WDI branch testing
	mailing list	libusb-devel.lists.sourceforge.net Filter messages from this mailing list
	mailed-by	lists.sourceforge.net
	unsubscribe	Unsubscribe from this mailing-list
		
	hide details 4:55 PM (54 minutes ago)
		
	On 2010.03.30 15:18, Xiaofan Chen wrote:
	> I just build the WDI branch with WDK and it seems to work.

	Yeah, I was meaning to make a formal announcement about that once I have
	a GUI version of the setdvr application, but if you're in a hurry, and
	need a one size fits all WinUSB installer, you can pick up the 32+64 bit
	precompiled setdrv.exe, from the "Driver Installation" section on the
	Windows Backend page (http://libusb.org/wiki/windows_backend).

	setdrv, which relies on the Windows Driver Installer library - libwdi,
	will detect and install a WinUSB driver for any plugged USB device that
	doesn't have a driver, for any Windows platform starting with XP
	(including 64 bit ones). Ultimately, it'll also install libusb0.sys or
	any other USB driver we might require for the backend.

	One of the main goals of libwdi is to be able to produce libusb
	executables that also contain *all* the required driver files, so that a
	single executable can be redistributed, without worrying about users
	having to manually download and install their drivers.

	libdwi can also be used standalone, for the writing of installer type
	applications. I'm also examining the possibility of optionally providing
	the ability to use downloadable driver content, instead of embedded,
	which would reduce the general footprint of the library where needed (a
	32+64 bit compatible version is about 4.8 MB because of WinUSB DLLs).

	Note that eventhough the current git tree is a branch of libusb, libwdi
	doesn't share or use any files from libusb and can be compiled as a
	standalone.

	More info: http://libusb.org/wiki/libwdi

	Regards,

	/Pete

	PS: I'm still planning to make a formal announcement once I have a more
	presentable, and foolproof, GUI installer application.
	
	
	