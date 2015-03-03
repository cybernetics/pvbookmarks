



.. _android_training_basics:

===================================
Android developer training basics
===================================

.. seealso::

   - https://developer.android.com/training/index.html


.. contents::
   :depth: 3

Building your first app
=======================

.. seealso::

   - https://developer.android.com/training/basics/firstapp/index.html


Activity lifecycle
===================

.. seealso::

   - https://developer.android.com/training/basics/activity-lifecycle/index.html



Supporting different devices
============================

.. seealso::

   - https://developer.android.com/training/basics/supporting-devices/index.html



Building a Dynamic UI with Fragments
====================================

.. seealso::

   - https://developer.android.com/training/basics/fragments/index.html


Saving Data
============

.. seealso::

   - https://developer.android.com/training/basics/data-storage/index.html


Most Android apps need to save data, even if only to save information about the
app state during onPause() so the user's progress is not lost. Most non-trivial
apps also need to save user settings, and some apps must manage large amounts of
information in files and databases.

This class introduces you to the principal data storage options in Android, including:

- Saving key-value pairs of simple data types in a shared preferences file
- Saving arbitrary files in Android's file system
- Using databases managed by SQLite



Interacting with Other Apps
===========================

.. seealso::

   - https://developer.android.com/training/basics/intents/index.html

An Android app typically has several activities.

Each activity displays a user interface that allows the user to perform a
specific task (such as view a map or take a photo).

To take the user from one activity to another, your app must use an Intent to
define your app's "intent" to do something. When you pass an Intent to the
system with a method such as startActivity(), the system uses the Intent to
identify and start the appropriate app component. Using intents even allows your
app to start an activity that is contained in a separate app.

An Intent can be explicit in order to start a specific component (a specific
Activity instance) or implicit in order to start any component that can handle
the intended action (such as "capture a photo").

This class shows you how to use an Intent to perform some basic interactions with
other apps, such as start another app, receive a result from that app, and make
your app able to respond to intents from other apps.


Sharing Content
===============

.. seealso::

   - https://developer.android.com/training/sharing/index.html


