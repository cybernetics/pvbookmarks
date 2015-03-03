


.. _tut1_serial_csharp_communication:

======================================
Tutorial Serial C♯ Communication (1)
======================================


.. seealso::

   - http://msdn.microsoft.com/en-us/library/system.io.ports.serialport.aspx
   - :ref:`serial_communication`
   - :ref:`csharp_language`


.. contents::
   :depth: 3



Communicating with Serial Port in C#
====================================

.. seealso::

   - http://www.c-sharpcorner.com/uploadfile/eclipsed4utoo/communicating-with-serial-port-in-C-Sharp/


This article will demonstrate how to write and receive data from a device
connected to a serial port in C# and .NET.

We will be writing the received data to a TextBox on a form, so this will also
deal with threading.


SerialPort()
-------------

Initializes a new instance of the SerialPort class.



Properties
==========

PortName
--------

Gets or sets the port for communications, including but not limited to all
available COM ports.


IsOpen
------

Gets a value indicating the open or closed status of the SerialPort object.


NewLine
--------

Gets or sets the value used to interpret the end of a call to the ReadLine and
WriteLine methods.


ReadBufferSize
--------------

Gets or sets the size of the SerialPort input buffer.


ReadTimeout
------------

Gets or sets the number of milliseconds before a time-out occurs when a read
operation does not finish.

WriteBufferSize
---------------

Gets or sets the size of the serial port output buffer.



WriteTimeout
------------

Gets or sets the number of milliseconds before a time-out occurs when a
write operation does not finish.



Methods
=======

static GetPortNames
-------------------

Gets an array of serial port names for the current computer.


Open
----

Opens a new serial port connection.


Read(Byte[], Int32, Int32)
---------------------------

.. seealso:: http://msdn.microsoft.com/en-us/library/ms143549%28v=vs.100%29.aspx

Reads a number of bytes from the SerialPort input buffer and writes those bytes
into a byte array at the specified offset.

Returns the number of bytes read.


public string ReadExisting()
-----------------------------

.. seealso::  http://msdn.microsoft.com/en-us/library/system.io.ports.serialport.readexisting.aspx


This method returns the contents of the stream and internal buffer of the
SerialPort object as a string.

This method does not use a time-out.

Note that this method can leave trailing lead bytes in the internal buffer,
which makes the BytesToRead value greater than zero.

If it is necessary to switch between reading text and reading binary data from
the stream, select a protocol that carefully defines the boundary between text
and binary data, such as manually reading bytes and decoding the data


Write(Byte[], Int32, Int32)
----------------------------

Writes a specified number of bytes to the serial port using data from a buffer.


Close
-----

Closes the port connection, sets the IsOpen property to false, and disposes of the internal Stream object.



Events
======

DataReceived
------------

.. seealso:: http://msdn.microsoft.com/en-us/library/system.io.ports.serialport.datareceived.aspx

Represents the method that will handle the data received event of a
SerialPort object.

::

    using System;
    using System.IO.Ports;

    class PortDataReceived
    {
        public static void Main()
        {
            SerialPort mySerialPort = new SerialPort("COM1");

            mySerialPort.BaudRate = 9600;
            mySerialPort.Parity = Parity.None;
            mySerialPort.StopBits = StopBits.One;
            mySerialPort.DataBits = 8;
            mySerialPort.Handshake = Handshake.None;

            mySerialPort.DataReceived += new SerialDataReceivedEventHandler(DataReceivedHandler);

            mySerialPort.Open();

            Console.WriteLine("Press any key to continue...");
            Console.WriteLine();
            Console.ReadKey();
            mySerialPort.Close();
        }

        private static void DataReceivedHandler(
                            object sender,
                            SerialDataReceivedEventArgs e)
        {
            SerialPort sp = (SerialPort)sender;
            string indata = sp.ReadExisting();
            Console.WriteLine("Data Received:");
            Console.Write(indata);
        }
    }


ErrorReceived
-------------

Represents the method that handles the error event of a SerialPort object.


Binary bit processing
=====================

.. seealso:: http://stackoverflow.com/questions/7874980/c-sharp-serial-port-binary-stream-processing


::

    private void port_DataReceived(object sender, SerialDataReceivedEventArgs e)
    {
        int count = sp.BytesToRead;
        byte[] data = new byte[count];
        sp.Read(data, 0, data.Length);
        file.WriteLine(BitConverter.ToString(data));
    }



