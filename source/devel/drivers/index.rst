.. module:: Drivers
    :synopsis: Drivers
    :platform: windows XP, Vista, windows 7, GNU/Linux
  
=======
Drivers 
=======

In computing, a device driver or software driver is a computer program 
allowing higher-level computer programs to interact with a hardware device.

A driver typically communicates with the device through the computer bus 
or communications subsystem to which the hardware connects. 
When a calling program invokes a routine in the driver, the driver issues 
commands to the device. Once the device sends data back to the driver, 
the driver may invoke routines in the original calling program. 
Drivers are hardware-dependent and operating-system-specific. 
They usually provide the interrupt handling required for any 
necessary asynchronous time-dependent hardware interface.


.. seealso:: 

   - http://fr.wikipedia.org/wiki/Pilote_informatique
   - http://en.wikipedia.org/wiki/Device_driver
   
 
.. _linux_windows_drivers:
   
linux module drivers
====================

.. seealso::

   - http://tjworld.net/books/ldd3
   - http://kernelnewbies.org/Drivers
   - http://kernelnewbies.org/USB   
   - http://www.linux-usb.org/
 

USB drivers 
===========


.. toctree::
   :maxdepth: 7
    
   usb/index


windows drivers
===============

.. toctree::
   :maxdepth: 7
    
   windows/index
