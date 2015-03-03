

.. index::
   pcsclite debug

.. _pcsclite_debug:

==============
pcsclite debug
==============

PCSC API spy for GNU systems
============================

http://ludovicrousseau.blogspot.com/2010/08/pcsc-api-spy-for-gnu-systems.html


Executive summary
-----------------

   1. Copy the file ltrace.conf to ~/.ltrace.conf
   2. Use with: ltrace -l/usr/lib/libpcsclite.so your_application

    * Call to other libraries (lib C in particular) are no more displayed
    * PCSC functions arguments are displayed in a human form


If I reuse the same SCardConnect example we now have::

    SCardConnect(0x103d6cb, "Lenovo Integrated Smart Card Rea"..., SCARD_SHARE_SHARED, SCARD_PROTOCOL_T0_SCARD_PROTOCOL_T1, 126261, SCARD_PROTOCOL_T1) = SCARD_S_SUCCESS
    

We get:

    * Connection context to the PC/SC Resource Manager. It is just a random numeric value: 0x103d6cb
    * Reader name to connect to: "Lenovo Integrated Smart Card Rea"...
    * Mode of connection type: exclusive or shared. SCARD_SHARE_SHARED
    * Desired protocol use: SCARD_PROTOCOL_T0_SCARD_PROTOCOL_T1
    * Handle to this connection: 126261
    * Established protocol to this connection: SCARD_PROTOCOL_T1
    * Return code: SCARD_S_SUCCESS

   
   
It is easy to use ltrace to trace a program. I will use the testpcsc 
program included in pcsc-lite as a PC/SC sample code::

    $ ltrace .libs/testpcsc
    
    
Limitations
-----------


By default ltrace lists all the calls from all the libraries. You can restrict 
the tracing to one specific library using::

    -l/usr/lib/libpcsclite.so

The PC/SC API calls are not really useful. You have to parse the argument 
by hand. 

It is not easy to know what SCardConnect(0x103a3a0, 0x96ea118, 2, 3, 0xbfdfacdc) = 0 
is really doing.

ltrace PCSC configuration file
------------------------------

ltrace can use a configuration file to parse the arguments of the functions 
and display a (more) human readable version.

The configuration file uses a very simple format. 
For example for SCardConnect I used::

    scarderror SCardConnect(scardcontext, string, share_mode, protocol, +scardhandle*, +protocol*);

A ltrace configuration file is now included in the pcsc-lite project in 
the new contrib/ directory. Just copy the :download:`ltrace.conf` to ~/.ltrace.conf.

./pcscd -a 
==========



DO_PROFILE define in src/winscard_clnt.c
========================================

To have more logs on the client side you have to edit src/winscard_clnt.c and 
``#define DO_PROFILE``. Then rebuild and reinstall pcsc-lite.
 
