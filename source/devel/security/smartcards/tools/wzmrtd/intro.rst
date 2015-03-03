


.. _wzmrtd_info:

============
wzmrtd intro
============

.. contents::
   :depth: 3
   

Description
===========

wzMRTD is a software library that reads electronic passports (also well known
as E-Passports or biometric passports).

Electronic passports embedd a contactless smart card, which stores the data 
to be read by border-clearance software or by wzMRTD. 

The mapping of the chip (file system, data layout) has been defined by ICAO, 
an international organization, in Machine Readable Travel Document (MRTD) standard.

Communication between wzMRTD and the chip is performed through a contactless 
reader compliant with ISO/IEC 14443 standard. 

PC/SC and Pro-Active readers are supported. Accessing the data is possible 
only in a secure session, where the authentication key is computed from 
information printed on the passport (number, date of delivery and date 
of expiracy). 

The digits -printed on the Machine Readable Zone (MRZ)- can be read by an OCR scanner.

wzMRTD is an open-source project, and aims to be modified, enhanced, 
re-used... by anybody interested in this subject. 

Why ?
=====

I decided to develop wzMRTD and to publish its source code in a reaction of 
mood vis-a-vis many articles publied in late 2006, dealing with the "vulnerability" 
of electronic passports. The most significant one is this article (title : "Cracked it !")
published by the Guardian in UK. Here's an extract :

(...) we have just sucked out all the supposedly secure data and biometric information
from three new passports and displayed it all on a laptop computer.

To make a long story short, wzMRTD is an answer to this misinformation.

In my opinion, nobody shall be surprised to be able to read a passport with a 
proximity card reader and a small piece of software, this is precisely the 
intended goal (remember what "MRTD" stands for...). Relax, guys, you've 
not "cracked" anything, you've just read a document, and implemented 
what was described in it. No surprise at all, unless you forgot to 
read the more interesting pages...

This article in question caused a small thread on french Usenet group 
fr.misc.cryptologie, where interesting contributions (especially signed 
by Sylvain) may be read (in french).

Due to my position at Pro-Active, I had a few contactless readers, and
a few contactless passports, so I decided to "crack" them as well, 
and to publish the project for people interested in the subject.

And afterwards ?
================

Obviously wzMRTD is not really interesting for end-user, one needs a small 
graphical interface to display the data and the picture, that's why 
wzPASS has been written too.

Todo list/Roadmap
=================

* Handling of DG11 and DG12,
* Linux version using pcsc-lite,
* Publish documentation.

Credits / Thanks
================

* Sylvain Ferey for his repeated support,
* Stanislas Dourdin, author of an early yet functionnal pre-version,
* Damien Croisot, who provided his own passport for test,
* Oberthur Card System, provider of the Utopians passports,
* Pro-active, my official provider for readers, computers, and coffee.
    
    
Links
=====

- http://www.waazaa.org/wzmrtd/

