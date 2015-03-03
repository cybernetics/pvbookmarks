

.. index::
   pair: Android; Debugging


.. _android_developer_tools_debugging:

==================================
Android Developer Tools Debugging
==================================

.. seealso::

   - https://developer.android.com/tools/debugging/index.html


.. figure:: debugging.png
   :align: center


.. contents::
   :depth: 3

Introduction
============

The Android SDK provides most of the tools that you need to debug your
applications. You need a JDWP-compliant debugger if you want to be able to do
things such as step through code, view variable values, and pause execution of
an application.

If you are using Eclipse, a JDWP-compliant debugger is already included and there
is no setup required. If you are using another IDE, you can use the debugger
that comes with it and attach the debugger to a special port so it can communicate
with the application VMs on your devices.

The main components that comprise a typical Android debugging environment are:

- adb
  acts as a middleman between a device and your development system. It provides
  various device management capabilities, including moving and syncing files to
  the emulator, running a UNIX shell on the device or emulator, and providing a
  general means to communicate with connected emulators and devices.
- Dalvik Debug Monitor Server
  DDMS is a graphical program that communicates with your devices through adb.
  DDMS can capture screenshots, gather thread and stack information, spoof incoming
  calls and SMS messages, and has many other features.
- Device or Android Virtual Device
  Your application must run in a device or in an AVD so that it can be debugged.
  An adb device daemon runs on the device or emulator and provides a means for
  the adb host daemon to communicate with the device or emulator.
- JDWP debugger
  The Dalvik VM (Virtual Machine) supports the JDWP protocol to allow debuggers
  to attach to a VM.
  Each application runs in a VM and exposes a unique port that you can attach a
  debugger to via DDMS. If you want to debug multiple applications, attaching to
  each port might become tedious, so DDMS provides a port forwarding feature that
  can forward a specific VM's debugging port to port 8700. You can switch freely
  from application to application by highlighting it in the Devices tab of DDMS.
  DDMS forwards the appropriate port to port 8700. Most modern Java IDEs include
  a JDWP debugger, or you can use a command line debugger such as jdb.


DDMS (Dalvik Debug Monitor Server)
==================================

.. toctree::
   :maxdepth: 3

   ddms/index



