
.. index::
   pair: Android; NDK




.. _android_ndk:

==================================
Android Ndk
==================================


.. seealso::

   - https://developer.android.com/tools/sdk/ndk/index.html
   - https://en.wikipedia.org/wiki/Android_NDK#Native_development_kit


.. contents::
   :depth: 3


Introduction
============

The NDK is a toolset that allows you to implement parts of your app using native-code
languages such as C and C++. For certain types of apps, this can be helpful so you
can reuse existing code libraries written in these languages, but most apps do
not need the Android NDK.

Before downloading the NDK, you should understand that the NDK will not benefit
most apps. As a developer, you need to balance its benefits against its drawbacks.

Notably, using native code on Android generally does not result in a noticable
performance improvement, but it always increases your app complexity.

In general, you should only use the NDK if it is essential to your app—never
because you simply prefer to program in C/C++.



Android Ndk versions
====================

.. toctree::
   :maxdepth: 3

   versions/index

