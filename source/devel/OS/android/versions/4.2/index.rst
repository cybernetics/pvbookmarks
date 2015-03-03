

.. index::
   pair: Android ; 4.2
   pair: Android ; API Level 17
   pair: FORTIFY; SOURCE.

.. _android_os_4_2:

========================================================
Android 4.2 Jelly Bean (API Level 17, 13 November 2012)
========================================================

.. seealso::

   - http://developer.android.com/about/versions/jelly-bean.html#android-42
   - https://developer.android.com/tools/revisions/platforms.html
   - :ref:`android_platforms`


.. contents::
   :depth: 3


Announce
========

.. seealso::

   - http://android-developers.blogspot.fr/2012/11/introducing-android-42-new-and-improved.html



Introducing Android 4.2, A New and Improved Jelly Bean
Posted by Angana Ghosh, Product Manager in Android, and Dirk Dougherty, Android
Developer Relations Team

Today we are making Android 4.2 (Jelly Bean) SDK platform available for download.

Below are some of the highlights of Android 4.2, API level 17.


Nouveautés 4.2
===============

.. seealso::

   - https://fr.wikipedia.org/wiki/Android


- Nouvelle interface de l'appareil photo
- l'introduction de Photosphère permettant une prise des photos à 360°
  type Street View,
- d'un système multi-compte uniquement sur tablette,
- de ``Type Gesture`` permettant d'écrire avec le clavier rien qu'en glissant le
  doigt
- et d'améliorations de :ref:`Google Now <google_now>` ajoutant la possibilité de suivre un colis ou
  d'embarquer à bord d'un avion.


Full native support for RTL
===========================

Android 4.2 introduces full native support for RTL (right-to-left) layouts,
including layout mirroring.

With native RTL support, you can deliver the same great app experience to all
of your users, whether their language uses a script that reads right-to-left
or one that reads left-to-right.


New Bluetooth stack
===================

Android 4.2 introduces a new Bluetooth stack optimized for use with Android
devices.

The new Bluetooth stack developed in collaboration between Google and Broadcom
replaces the stack based on BlueZ and provides improved compatibility and reliability.


FORTIFY_SOURCE
==============

Android now implements ``FORTIFY_SOURCE``.

This is used by system libraries and applications to prevent memory corruption.


Improved Camera with HDR
========================

Android 4.2 introduces a new camera hardware interface and pipeline for improved
performance.

On supported devices, apps can use a new HDR camera scene mode to capture an
image using high dynamic range imaging techniques.

New NFC hardware interface and controller interface
===================================================

Android 4.2 introduces support for controllers based on the NCI standard from
the NFC-Forum.

NCI provides a standard communication protocol between an NFC Controller (NFCC)
and a device Host, and the new NFC stack developed in collaboration between
Google and Broadcom supports it.



