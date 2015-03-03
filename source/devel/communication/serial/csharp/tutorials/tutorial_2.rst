


.. _tut2_serial_csharp_communication:

======================================
Tutorial Serial C♯ Communication (2)
======================================


.. seealso::

   - http://codesamplez.com/programming/serial-port-communication-c-sharp



Introduction
=============

Serial communications can be done via either direct to physical serial port 
connected to the computer or via a USB to serial converter interface. 

If the device do require a serial port and your computer don’t have any, you 
can make use of such converters easily.


Retrieve List Serial Ports:

OK, lets first see whether we can detect the serial ports from within our 
application. 

As a prerequisite, you need to make sure that, while the application is running, 
the windows user must need to have access to the ports. 

The following C# code examples will return a list of Serial port names connected 
to the computer::

	
    public List<string> GetAllPorts()
    {
         List<String> allPorts = new List<String>();
         foreach (String portName in System.IO.Ports.SerialPort.GetPortNames())
         {
             allPorts.Add(portName);
         }
         return allPorts;
    }
