.. module:: pyGBL2SIM
    :synopsis: the python beagle simulator


.. index::
    twisted
    simulator
    rs232
    beagle record


The simulator python pyBGL2SIM_gen module
=========================================

voir P5E627/Concept/Soft/PC/XLOG9X324_python_Simul


Module csv
----------

.. seealso::

    http://docs.python.org/library/csv.html#module-csv


Module collections
------------------

.. code-block:: python

    from collections import namedtuple

    BeagleRecord = namedtuple('BeagleRecord', 'Index, Time, Dur ,Len ,Err ,Dev ,Ep ,Level , Record, Data')


    def beagle_records(filename):
        for beagle_record in map(BeagleRecord._make, csv.reader(open(filename, "rb"))):
            yield beagle_record



Other example
^^^^^^^^^^^^^

.. code-block:: python

    EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

    import csv
    for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
        print emp.name, emp.title

    import sqlite3
    conn = sqlite3.connect('/companydata')
    cursor = conn.cursor()
    cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
    for emp in map(EmployeeRecord._make, cursor.fetchall()):
        print emp.name, emp.title


.. seealso::

    collections documentation:  http://docs.python.org/library/collections.html
    namedtuple:  http://docs.python.org/library/collections.html#collections.namedtuple





.. _pyBGL2SIM_gen:

pyBGL2SIM_gen.py
================


::

    from __future__ import print_function

    # Import standard modules
    import string
    import csv
    import binascii
    import time

    # Import addons modules
    import serial

    ## COM port number
    # Please defines here the correct COM port number.
    COMPortNumber = 5

    from collections import namedtuple

    BeagleRecord = namedtuple('BeagleRecord', 'Index, Time, Dur ,Len ,Err ,Dev ,Ep ,Level , Record, Data')


    def beagle_records(filename):
        print('opening the ' ,  filename , 'beagle file')
        try:
            for beagle_record in map(BeagleRecord._make, csv.reader(open(filename, "rb"))):
                yield beagle_record
        except Exception as e:
           print('can t open file', filename)

    #beagle_file = "essai_touche_gen.csv"
    # beagle_file = "bug2_gen.csv"
    # beagle_file = "CR_t2009_11_09_small_gen.csv"
    nb_max_records = 100000000000
    beagle_file = "CR_beagle_2009_11_09_all_gen.csv"

    if __name__ == '__main__':
        try:
            print("Opening serial port ...")
            ser = serial.Serial(COMPortNumber-1, 115200)

            try :
                Table                   = string.maketrans('','')
                RemoveNonHexCharsTable  = string.translate(Table, Table, string.hexdigits)
                CheckBadCharTable       = string.translate(Table, Table, string.punctuation)
                UniformSepTable         = string.maketrans(string.punctuation,' '.ljust(len(string.punctuation)))

                LastTime = time.clock()
                PreviousTimeStamp = None

                nb_records=0;
                for beagle_record in beagle_records(beagle_file):
                    nb_records=nb_records+1
                    print("." , end = "")
                    if ((nb_records % 200) == 0):
                        print("\n", nb_records, " beagle records")
                    if (nb_records > nb_max_records):
                        break;
                    SplittedTime = string.translate(beagle_record.Time, UniformSepTable).split()
                    Minutes, Secondes, Millisecondes = int(SplittedTime[0]), int(SplittedTime[1]), int(SplittedTime[2])
                    Microsecondes , Nanosecondes = int(SplittedTime[3]), int(SplittedTime[4])
                    CurrentTimeStamp = (Minutes * 60) + Secondes + (Millisecondes / 1000.0) + (Microsecondes / 1000000.0) + (Nanosecondes / 1000000000.0)

                    # to comment if no delay between frames.
                    if PreviousTimeStamp is not None :
                       if CurrentTimeStamp > PreviousTimeStamp :
                           time.sleep(CurrentTimeStamp-PreviousTimeStamp)
                       else:
                           PreviousTimeStamp = CurrentTimeStamp
                    else:
                        PreviousTimeStamp = CurrentTimeStamp

                    if len(string.translate(beagle_record.Data, Table, CheckBadCharTable)) == 0 :
                        try :
                            RawData = binascii.a2b_hex(string.translate(beagle_record.Data, Table, RemoveNonHexCharsTable))
                            ser.write(RawData)
                        except TypeError :
                            pass
                    PreviousTimeStamp = CurrentTimeStamp
            finally :
                print("\n" , nb_records, "records processed")
                print("Closing serial port ...")
                ser.close()
        except serial.SerialException, e :
            print("Unable to open COM port %d, please check port number" % COMPortNumber)


.. index::
   pyBGL2SIM_gen.py

Code source de pyBGL2SIM_gen.py
===============================

:download:`Download pyBGL2SIM_gen.py <pyBGL2SIM_gen.py>`


.. literalinclude::  pyBGL2SIM_gen.py



Twisted serial service
======================


You should be able to implement your own Service class and create your
SerialPort instances in the startService method. e.g. (untested)

.. code-block:: python

    from twisted.application import service
    from twisted.internet import reactor
    from twisted.internet.serialport import SerialPort
    from twisted.protocols.basic import LineReceiver

    class SerialService(service.Service):
       def startService(self):
           self.serial = SerialPort(LineReceiver, '/dev/tty/serialport',reactor)

    multiService = service.MultiService()
    serialService = SerialService()
    serialService.setServiceParent(multiService)

    # Add some other services...

    application = service.Application("Serial MultiService Example")
    multiService.setServiceParent(application)


.. seealso::

   - http://twistedmatrix.com/documents/9.0.0/api/twisted.application.service.Service.html
   - http://twistedmatrix.com/documents/current/core/howto/producers.html


.. code-block:: python

    Hi,I try to use twisted for asynchronous serial port read().

    Here is my simple twisted code:
    ==========================
    from twisted.internet import reactor
    from twisted.internet.serialport import SerialPort
    from twisted.internet.protocol import Protocol

    class Client(Protocol):
        def connectionMade(self):
            print 'connected'

        def dataReceived(self, data):
            print data

    SerialPort(Client(), 'COM4', reactor)
    reactor.callLater(20, reactor.stop())
    reactor.run()

    ==========================

    It runs on my Mac with this line changed to SerialPort(Client,
    'dev/tty.usbserial-A4001mLL', reactor) which is my Arduino board device.

    But on Windows XP, it gave the error message:
    "AttributeError: 'module' object has no attribute 'addEvent' "

    I tried to used different reactor, such as selectreactor, win32eventreactor,
    but the error message became "AssertionError: reactor already installed"

.. code-block:: python

    > Can twisted be used to access a serial port on OS X, MS Windows, linux,
    > etc ???

    Yes, via the twisted.internet.serial module.

    > Is there any support for serial protocols (eg. BISYNC, PPP, etc) ???

    You'd have to write them yourself, except for a couple, e.g. Logitech
    Serial Mouse
    (http://twistedmatrix.com/trac/browser/tags/releases/twisted-8.2.0/twisted/protocols/mice/mouseman.py) and a couple of GPS protocols.

    > Can twisted be used to create custom serial protocols ???

    Yes. For example,
    http://twistedmatrix.com/projects/core/documentation/examples/mouse.py
    shows how to use the mouse protocol.


.. code-block:: python

    > > I've been able to create an application in Linux that reads/writes
    > > multiple serial ports asyncronously. The setup code that does this looks
    > > like this:
    > >
    > > ...
    > > from twisted.internet.qtreactor import install
    > > a = QApplication(argv)
    > > install(a)
    > > from twisted.internet import reactor
    > > from twisted.internet.serialport import SerialPort
    > > ...
    > >   ports, badPorts = getGoodPorts()
    > >   if not ports:
    > >     exit(1)
    > >   data = ConfigData(join(sep, 'etc', 'qa.conf'))
    > >   dbInfo = copy(data['qadata'])
    > >   getLogin(dbInfo)
    > >   w = MainWindow(data, dbInfo, ports)
    > >   w.show()
    > >   reactor.addSystemEventTrigger('after', 'shutdown', a.quit)
    > >   a.connect(a, SIGNAL('lastWindowClosed()'), reactor.stop)
    > >   for portObj in w.portObjs:
    > >     SerialPort(portObj.scanner, portObj.port, reactor, baudrate=38400)
    > >     portObj.sendLine()
    > >   reactor.run()
    > >
    > > Where the portObj.scanner is an instance of a descendent of Protocol.
    > > Like I said, the above code works under Linux. Then I tried porting this
    > > to Windows. The first problem I came across is that the qtreactor.py
    > > would not work. I had to subclass QTReactor from Win32Reactor. It runs
    > > without errors. However, I am not reading anything off of the serial
    > > port. I can see the lights blink on the port when the portObj.sendLine()
    > > is called, so I believe I am writing to it ok and data is coming back.
    > > The data is just not read by the application. I think it must have
    > > something to do with the SerialPort instance not getting an even that
    > > data is ready. I suspect this is a Windows issue in that Windows is not
    > > signaling an event when data is ready to read on the serial port.
    > >
    > > Does anybody have any experience with this? Is there a work around? Am I
    > > doing something wrong?
    >
    > Well, I found out that it has something to do with the qtreactor. If I
    > use just a Win32Reactor, it will read/write the serial port just fine. I
    > played around with writing to the serial port using
    > scanner.transport.write('\n') and found that
    > Win32Reactor.doWaitForMultipleEvents() is called when a Win32Reactor is
    > used. It is not called when a QTReactor(Win32Reactor) is used. The
    > question is why is this the case?

    Ok, I was able to find a solution to my problem. I had to make some
    changes to the original qt4reactor.py (which I renamed to qtreactor.py
    and copied over the original twisted qtreactor.py). The changes I made
    are:

    1) Subclassed QTReactor from Win32Reactor.
    2) Commented out the following methods so the base class methods are
    used:
      addReader()
      addWriter()
      removeReader()
      removeWriter()
      removeAll()
    3) Modified the QTReactor.simulate() method so it calls doIteration()
    after calling runUntilCurrent().

    I've tested this with two devices and it works great. After I test this
    in a production environment with six devices, I can create a patch
    against the original qt4reactor.py. I'd like to make this available to
    others who might need it. Where is the best place to post the patch?
    This mailing list?


.. code-block:: python


    How can I access the reactor if I want to use the win32eventreactor?
    It seems I have to win32eventreactor.install() before importing
    the reactor from twisted.internet, otherwise I get a traceback
    saying AssertionError: reactor already installed.

    Is this the recommended way to do it:

    -----
    from twisted.internet import win32eventreactor
    win32eventreactor.install()
    from twisted.internet import reactor










