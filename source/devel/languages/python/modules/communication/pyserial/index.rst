
.. index::
   python modules (pyserial)

.. _python_pyserial:

=======================
pyserial
=======================

.. seealso::

   - http://pyserial.sourceforge.net


.. image:: pyserial.png


This module encapsulates the access for the serial port. It provides backends
for Python running on Windows, Linux, BSD (possibly any POSIX compliant system),
Jython and IronPython (.NET and Mono). The module named “serial” automatically
selects the appropriate backend.

Opening serial ports
====================

Open port 0 at "9600,8,N,1", no timeout::

    >>> import serial
    >>> ser = serial.Serial(0)  # open first serial port
    >>> print ser.portstr       # check which port was really used
    >>> ser.write("hello")      # write a string
    >>> ser.close()             # close port

Open named port at "19200,8,N,1", 1s timeout::

    >>> ser = serial.Serial('/dev/ttyS1', 19200, timeout=1)
    >>> x = ser.read()          # read one byte
    >>> s = ser.read(10)        # read up to ten bytes (timeout)
    >>> line = ser.readline()   # read a '\n' terminated line
    >>> ser.close()

Open second port at "38400,8,E,1", non blocking HW handshaking::

    >>> ser = serial.Serial(1, 38400, timeout=0,
    ...                     parity=serial.PARITY_EVEN, rtscts=1)
    >>> s = ser.read(100)       # read up to one hundred bytes
    ...                         # or as much is in the buffer







