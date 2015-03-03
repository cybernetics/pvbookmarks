
=============
pyusb install
=============


ldconfig and LD_LIBRARY_PATH
============================

:: 

	vim ld.so.conf
	

add /opt/libusb/current/lib


run ldconfig -v | grep libusb ::

    ldconfig -v | grep libusb 



	[root@houx etc]# ldconfig -v | grep libusb
	/opt/libusb/current/lib:
			libusb-1.0.so.0 -> libusb-1.0.so.0.0.0
			libusb-0.1.so.4 -> libusb.so
			libusbpp-0.1.so.4 -> libusbp
        
        
set the new library
===================

.. seealso:: http://docs.python.org/library/ctypes.html

:: 

	from ctypes import *
	import ctypes.util
	from ctypes.util import find_library
    libname_usb10 = find_library('libusb-1.0')

	def _load_library():
		candidates = ('usb-1.0', 'libusb-1.0', 'usb')
		for candidate in candidates:
			libname = find_library(candidate)
			if libname is not None: break
			

