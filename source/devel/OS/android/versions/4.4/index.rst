

.. index::
   pair: Android ; 4.4
   pair: Android ; KITKAT
   pair: Android ; NFC (KITKAT)
   pair: Android ; API Level 19
   pair: Card ; Emulation (Host Card Emulation)

.. _android_os_4_4:
.. _android_kitkat:

========================================================
Android 4.4 KITKAT (API Level 19 31 october 2013)
========================================================

.. seealso::

   - http://developer.android.com/about/versions/kitkat.html
   - http://developer.android.com/about/versions/android-4.4.html
   - :ref:`android_platforms`



.. figure:: kk-hero.png
   :align: center

.. contents::
   :depth: 3



Introduction
=============

.. seealso::

   - http://android-developers.blogspot.fr/2013_10_01_archive.html

Android 4.4 (KITKAT) is a new release for the Android platform that offers new 
features for users and app developers. 

This document provides an introduction to the most notable new APIs.

As an app developer, you should download the Android 4.4 system image and SDK 
platform from the SDK Manager as soon as possible. 

If you don't have a device running Android 4.4 on which to test your app, use 
the Android 4.4 system image to test your app on the Android emulator. 

Then build your apps against the Android 4.4 platform to begin using the latest APIs.



Key Developer Features
=======================

- Host Card Emulation
- Printing framework
- Storage access framework
- Low-power sensors
- SMS provider
- Full-screen Immersive mode
- Transitions framework
- Chromium WebView
- Screen recording
- RenderScript NDK
- Bluetooth HOGP and MAP
- IR Blasters
- Closed captioning settings
- RTL features
- Security enhancements
- Tools for analyzing memory use


API differences 
===============

.. seealso::  http://developer.android.com/sdk/api_diff/19/changes.html



.. _android_kitkat_nfc:

Wireless and Connectivity
==========================

Host Card Emulation (HCE)
-------------------------

.. seealso:: 

   - http://developer.android.com/guide/topics/connectivity/nfc/hce.html
   - http://developer.android.com/about/versions/kitkat.html#44-hce

Android apps can now emulate ISO14443-4 (ISO-DEP) NFC cards that use APDUs for 
data exchange (as specified in ISO7816-4). 

This allows an NFC-enabled device running Android 4.4 to emulate multiple 
NFC cards at the same time, and allows an NFC payment terminal or other NFC reader 
to initiate a transaction with the appropriate NFC card based on the application 
identifier (AID).

If you want to emulate an NFC card that is using these protocols in your app, 
create a service component based on the HostApduService class. 

Whereas if your app instead uses a secure element for card emulation, you need 
to create a service based on the OffHostApduService class, which will not 
directly be involved in the transactions but is necessary to register the AIDs 
that should be handled by the secure element.

For more information, read the `NFC Card Emulation guide`_.


.. _`NFC Card Emulation guide`:  http://developer.android.com/guide/topics/connectivity/nfc/hce.html


New NFC capabilities through Host Card Emulation
=================================================

.. seealso:: http://developer.android.com/about/versions/kitkat.html#44-hce

Android 4.4 introduces new platform support for secure NFC-based transactions 
through Host Card Emulation (HCE), for payments, loyalty programs, card access, 
transit passes, and other custom services. 

With HCE, any app on an Android device can emulate an NFC smart card, letting 
users tap to initiate transactions with an app of their choice, no provisioned 
secure element (SE) in the device is needed. 

Apps can also use a new Reader Mode to act as readers for HCE cards and other 
NFC-based transactions.

Android HCE emulates ISO/IEC 7816 based smart cards that use the contactless 
ISO/IEC 14443-4 (ISO-DEP) protocol for transmission. 
These cards are used by many systems today, including the existing EMVCO NFC 
payment infrastructure. 

Android uses Application Identifiers (AIDs) as defined in ISO/IEC 7816-4 as the 
basis for routing transactions to the correct Android applications.

Apps declare the AIDs they support in their manifest files, along with a 
category identifier that indicates the type of support available 
(for example, "payments"). 

In cases where multiple apps support the same AID in the same category, Android 
displays a dialog that lets the user choose which app to use.

When the user taps to pay at a point-of-sale terminal, the system extracts the 
preferred AID and routes the transaction to the correct application. 

The app reads the transaction data and can use any local or network-based 
services to verify and then complete the transaction.

Android HCE requires an NFC controller to be present in the device. 

Support for HCE is already widely available on most NFC controllers, which offer 
dynamic support for both HCE and SE transactions. 

Android 4.4 devices that support NFC will include Tap & Pay for easy payments using HCE. 



NFC reader mode
================


A new NFC reader mode allows an activity to restrict all NFC activity to only 
reading the types of tags the activity is interested in while in the foreground. 

You can enable reader mode for your activity with enableReaderMode(), providing 
an implementation of NfcAdapter.ReaderCallback that receives a callback when 
new tags are detected.

This new capability, in conjunction with host card emulation, allows Android 
to operate on both ends of a mobile payment interface: One devices operates as 
the payment terminal (a device running a reader mode activity) and another 
device operates as the payment client (a device emulating an NFC card).



