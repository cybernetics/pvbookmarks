

.. index::
   pair: Android; Adb (Android Debug Bridge)
   ! Adb


.. _adb:

============================
Adb
============================

.. seealso::

   - https://developer.android.com/tools/help/adb.html
   - :ref:`ddms`
   - :ref:`adb_installation`


.. contents::
   :depth: 3

Introduction
=============

``Android Debug Bridge`` (adb) is a versatile command line tool that lets you
communicate with an emulator instance or connected Android-powered device.

It is a client-server program that includes three components:

- A client, which runs on your development machine. You can invoke a client from
  a shell by issuing an adb command. Other Android tools such as the ADT plugin
  and DDMS also create adb clients.
- A server, which runs as a background process on your development machine.
  The server manages communication between the client and the adb daemon running
  on an emulator or device.
- A daemon, which runs as a background process on each emulator or device instance.

You can find the adb tool in <sdk>/platform-tools/.
