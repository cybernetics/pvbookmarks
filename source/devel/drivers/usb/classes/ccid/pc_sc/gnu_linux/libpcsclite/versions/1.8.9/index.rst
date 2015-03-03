
.. index::
   pair: libpcsclite ; version 1.8.9


.. _libpcsclite_1_8_9:

========================================
libpcsclite 1.8.9 (16 October 2013)
========================================

.. seealso::

   - http://ludovicrousseau.blogspot.fr/2013/10/new-version-of-pcsc-lite-189.html
   - https://alioth.debian.org/frs/?group_id=30105&release_id=1906#pcsclite-_1.8.9-title-content


.. contents::
   :depth: 3

Changelog (16/10/2013)
==========================


SCardEndTransaction()
---------------------

Return an error if is called with no corresponding  SCardBeginTransaction()


SCardGetAttrib()
-----------------

- Add support of SCARD_ATTR_DEVICE_SYSTEM_NAME
- Fix bug in SCARD_ATTR_DEVICE_FRIENDLY_NAME

SCardBeginTransaction() 
-----------------------

was not correctly releasing a mutex when the hCard handle was invalidated
The problem was that SCardGetStatusChange() was blocked because SCardBeginTransaction() 
had not released the context mutex.

PCSC/reader.h
---------------

Use C99 flexible array member
The structures PIN_MODIFY_STRUCTURE and PIN_VERIFY_STRUCTURE now use a C99 
flexible array member when available for abData field.
uint8_t abData[];

Add support of --reader-name-no-serial and --reader-name-no-interface
----------------------------------------------------------------------

It is now possible to NOT add the USB serial number of the reader using --reader-name-no-serial
It is now possible to NOT add the CCID interface name of the reader using --reader-name-no-interface


Add support of serialconfdir pkg-config variable
------------------------------------------------

It is now possible to use pkg-config to get the directory used by pcscd to fetch 
serial drivers configurations::

    $ pkg-config libpcsclite --variable=serialconfdir 
    /etc/reader.conf.d
    
    
pcsc-spy
---------

- Try to display the thread in the order they appear in the log
- Add SCARD_ATTR_DEVICE_SYSTEM_NAME


Check the Info.plist file is (a minimum) correct
-------------------------------------------------

Update PROTOCOL_VERSION_MINOR from 2 to 3


MAX_READERNAME
---------------

We broke the API between version 1.8.3 and 1.8.4 by changing the value of MAX_READERNAME. 

This change should have been made before releasing version 1.8.4 to make mix of 
versions clearly non working instead of failing with strange errors.


hotplug_libudev.c
==================

Fix a memory leak in case of error
Fix OpenBSD 5.2 compilation regarding dlopen

correctly manage thread safe multi-slot readers
Do not use pthread_atfork() any more (fix problem on FreeBSD)
fix memory leaks.

This was not really a problem unless you embedd pcscd in another process and 
do init/deinit pcscd without exiting the process (as maybe used on Android or iOS).

pcscd.8 manpage
===============

add documentation for 
--max-thread, --max-card-handle-per-thread, --max-card-handle-per-reader, 
--force-reader-polling, --error, --critical and --color


Some other minor improvements and bug correction
================================================








