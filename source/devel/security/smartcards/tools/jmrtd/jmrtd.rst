
.. index::
   pair: Smartcards ; JMRTD

.. _jmrtd:

==============================================================================
JMRTD An Open Source Java Implementation of Machine Readable Travel Documents
==============================================================================

.. seealso::

   - http://jmrtd.org/


.. figure:: jmrtd.png
   :align: center

.. contents::
   :depth: 3


Description
============

JMRTD is an open source Java implementation of the Machine Readable Travel 
Document (MRTD) standards as specified by the International Civil Aviation 
Organization (ICAO). 

The electronic passport (or "ePassport"), which by now has been introduced in 
many countries, is an implementation of these standards.

JMRTD provides both a card side application (the "passport applet") and a host 
side API for accessing ePassports. 

The passport applet makes it possible to create your own passports (in case 
you're starting your own country). 
The applet is written in Java Card.

The host side Java API can be used in different scenarios
=========================================================

Inspection system
------------------

The API makes it possible to read, decode, and validate 
the information on the chip (for some of these tasks JMRTD will need access 
to the issuing country's trust infrastructure).

Enrollment / personalization system
------------------------------------

The API also allows to encode information by complying to the relevant 
standards.

Testing framework
------------------

JMRTD was developed initially to test conformance and security of ePassport 
implementations.



The main features of JMRTD
===========================

- A (100% pure) Java API for accessing ICAO compliant eMRTDs and ePassports
- A Java Card eMRTD/ePassport emulator
- Java and Android supported
- PKD certificates and PKD CSCA master lists (from LDAP) supported
- Extended access control (EAC) and supplemental access control (SAC/PACE) supported
- LDS 1.7 decoding and encoding
- CBEFF datagroups fully supported
- JPEG2000 and WSQ encoded biometric images supported


  


   
   

     
   

   

   
