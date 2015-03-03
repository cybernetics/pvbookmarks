
.. index::
   USB tool hal-device

   
.. _hal_device:


===
HAL
===

http://en.wikipedia.org/wiki/HAL_%28software%29


HAL is a software project providing a hardware abstraction layer for Unix-like  
computer systems. It aims to allow desktop applications to discover and use 
the hardware of the host system through a simple, portable and abstract API, 
regardless of the type of the underlying hardware.

HAL was originally envisioned by Havoc Pennington and is now a freedesktop.org 
project, being a key part of the software stack of the GNOME and KDE desktop 
environments. It is free software, dual-licensed under both the GNU General 
Public License and the Academic Free License.

.. warning:: 
   HAL is now deprecated, with functionality being merged into udev as of 2008–2010; 


HAL is deprecated
=================

As of 2009, distributions such as Ubuntu,  Debian, and Fedora,and projects  
such as GNOME and X.org are in the process of deprecating HAL as it has 
"become a large monolithic unmaintainable mess". 

It is in the process of being merged into udev (main udev, libudev, and 
udev-extras) and existing udev and kernel functionality. 

Ubuntu version 10.04 removes HAL from the boot process.

Initially a new daemon DeviceKit was planned to replace certain aspects 
of HAL, but in March 2009, DeviceKit was deprecated in favor of adding 
the same code to udev as a package: udev-extras, and some functions 
have now moved to udev proper.

hal_device
==========


::

    hal-device


An extract of this command is::
    

	1: udi = '/org/freedesktop/Hal/devices/usb_device_b81_103_0137064_if0'
	info.udi = '/org/freedesktop/Hal/devices/usb_device_b81_103_0137064_if0'  (string)
	linux.subsystem = 'usb'  (string)
	linux.hotplug_type = 1  (0x1)  (int)
	info.product = 'USB Vendor Specific Interface'  (string)
	usb.interface.protocol = 0  (0x0)  (int)
	usb.interface.subclass = 0  (0x0)  (int)
	usb.interface.class = 255  (0xff)  (int)
	usb.interface.number = 0  (0x0)  (int)
	usb.linux.sysfs_path = '/sys/devices/pci0000:00/0000:00:13.1/usb3/3-2/3-2:1.0'  (string)
	usb.configuration_value = 1  (0x1)  (int)
	usb.num_configurations = 1  (0x1)  (int)
	usb.num_interfaces = 1  (0x1)  (int)
	usb.device_class = 255  (0xff)  (int)
	usb.device_subclass = 255  (0xff)  (int)
	usb.device_protocol = 255  (0xff)  (int)
	usb.vendor_id = 2945  (0xb81)  (int)
	usb.product_id = 259  (0x103)  (int)
	usb.vendor = 'id3 Semiconductors'  (string)
	usb.product = 'USB Vendor Specific Interface'  (string)
	usb.device_revision_bcd = 1  (0x1)  (int)
	usb.max_power = 200  (0xc8)  (int)
	usb.num_ports = 0  (0x0)  (int)
	usb.linux.device_number = 2  (0x2)  (int)
	usb.serial = '0137064'  (string)
	usb.speed_bcd = 4608  (0x1200)  (int)
	usb.version_bcd = 512  (0x200)  (int)
	usb.is_self_powered = false  (bool)
	usb.can_wake_up = false  (bool)
	usb.bus_number = 3  (0x3)  (int)
	info.bus = 'usb'  (string)
	info.parent = '/org/freedesktop/Hal/devices/usb_device_b81_103_0137064'  (string)
	linux.sysfs_path_device = '/sys/devices/pci0000:00/0000:00:13.1/usb3/3-2/3-2:1.0'  (string)
	linux.sysfs_path = '/sys/devices/pci0000:00/0000:00:13.1/usb3/3-2/3-2:1.0'  (string)

	2: udi = '/org/freedesktop/Hal/devices/usb_device_b81_103_0137064'
	info.udi = '/org/freedesktop/Hal/devices/usb_device_b81_103_0137064'  (string)
	linux.subsystem = 'usb'  (string)
	linux.hotplug_type = 1  (0x1)  (int)
	usb_device.bus_number = 3  (0x3)  (int)
	usb_device.can_wake_up = false  (bool)
	usb_device.is_self_powered = false  (bool)
	usb_device.version_bcd = 512  (0x200)  (int)
	usb_device.speed_bcd = 4608  (0x1200)  (int)
	usb_device.serial = '0137064'  (string)
	usb_device.linux.device_number = 2  (0x2)  (int)
	usb_device.num_ports = 0  (0x0)  (int)
	usb_device.max_power = 200  (0xc8)  (int)
	usb_device.device_revision_bcd = 1  (0x1)  (int)
	info.product = 'CERTIS 2'  (string)
	usb_device.product = 'CERTIS 2'  (string)
	info.vendor = 'id3 Semiconductors'  (string)
	usb_device.vendor = 'id3 Semiconductors'  (string)
	usb_device.product_id = 259  (0x103)  (int)
	usb_device.vendor_id = 2945  (0xb81)  (int)
	usb_device.device_protocol = 255  (0xff)  (int)
	usb_device.device_subclass = 255  (0xff)  (int)
	usb_device.device_class = 255  (0xff)  (int)
	usb_device.num_interfaces = 1  (0x1)  (int)
	usb_device.num_configurations = 1  (0x1)  (int)
	usb_device.configuration_value = 1  (0x1)  (int)
	usb_device.linux.sysfs_path = '/sys/devices/pci0000:00/0000:00:13.1/usb3/3-2'  (string)
	info.linux.driver = 'usb'  (string)
	info.bus = 'usb_device'  (string)
	info.parent = '/org/freedesktop/Hal/devices/usb_device_0_0_0000_00_13_1'  (string)
	linux.sysfs_path_device = '/sys/devices/pci0000:00/0000:00:13.1/usb3/3-2'  (string)
	linux.sysfs_path = '/sys/devices/pci0000:00/0000:00:13.1/usb3/3-2'  (string)


