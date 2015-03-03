

.. index::
   pair: Android; Apk
   pair: Android; classes.dex



.. _android_fundamentals:

================================
Android components fundamentals
================================

.. seealso::

   - https://developer.android.com/guide/components/fundamentals.html


.. contents::
   :depth: 3

Introduction
============


Android applications are written in the Java programming language. The Android
SDK tools compile the code—along with any data and resource files—into an
Android package, an archive file with an ``.apk`` suffix.

All the code in a single ``.apk`` file is considered to be one application and
is the file that Android-powered devices use to install the application.

Once installed on a device, each Android application lives in its own security
sandbox:

The Android operating system is a multi-user Linux system in which each application
is a different user.

By default, the system assigns each application a unique Linux user ID (the ID
is used only by the system and is unknown to the application). The system sets
permissions for all the files in an application so that only the user ID assigned
to that application can access them.

Each process has its own virtual machine (VM), so an application's code runs in
isolation from other applications.

By default, every application runs in its own Linux process. Android starts the
process when any of the application's components need to be executed, then shuts
down the process when it's no longer needed or when the system must recover memory
for other applications.


In this way, the Android system implements the **principle of least privilege**.

That is, each application, by default, has access only to the components that it
requires to do its work and no more. This creates a very secure environment in
which an application cannot access parts of the system for which it is not given
permission.

However, there are ways for an application to share data with other applications
and for an application to access system services:

It's possible to arrange for two applications to share the same Linux user ID,
in which case they are able to access each other's files. To conserve system
resources, applications with the same user ID can also arrange to run in the
same Linux process and share the same VM (the applications must also be signed
with the **same certificate**).

An application can request permission to access device data such as the user's
contacts, SMS messages, the mountable storage (SD card), camera, Bluetooth, and
more. All application permissions must be granted by the user at install time.


Définition
==========

.. seealso::

   - https://en.wikipedia.org/wiki/.apk


Une application Android est un fichier zip ayant pour extension ``.apk``.

Le code exécutable de l'application compilé sous la forme de bytecode Dalvik
est situé dans le fichier ``classes.dex``.


