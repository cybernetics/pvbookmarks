



.. index::
   pair: Kivy ; Python for android
   pair: Python ; Android


.. _kivy_python_for_android:

=======================
Kivy python for android
=======================

.. seealso:: 

   - https://github.com/kivy/python-for-android
   - http://python-for-android.readthedocs.org/en/latest/
   - http://txzone.net/2012/01/introducing-python-for-android/
   - Website: http://python-for-android.rtfd.org/
   - Forum: https://groups.google.com/forum/?hl=fr#!forum/python-android
   - Mailing list: python-android@googlegroups.com
   

Introduction
============

Python for android is a project to create your own Python distribution
including the modules you want, and create an apk including python, 
libs, and your application.

Global overview
---------------

#. Download Android NDK, SDK
 
 * NDK: http://dl.google.com/android/ndk/android-ndk-r8c-linux-x86.tar.bz2
 
 * More details at: http://developer.android.com/tools/sdk/ndk/index.html
 
 * SDK: http://dl.google.com/android/android-sdk_r21.0.1-linux.tgz
 
 * More details at:http://developer.android.com/sdk/index.html

#. Launch "android", and download latest Android platform, here API 14, 
   which would be Android 4.0

#. Export some environment variables::

    export ANDROIDSDK="/path/to/android/android-sdk-linux_86"
    export ANDROIDNDK="/path/to/android/android-ndk-r8c"
    export ANDROIDNDKVER=r8c
    export ANDROIDAPI=14

 (Of course correct the paths mentioned in ANDROIDSDK and ANDROIDNDK)

#. Clone python-for-android::

    git clone git://github.com/kivy/python-for-android

#. Build a distribution with OpenSSL module, PIL and Kivy::

    cd python-for-android
    ./distribute.sh -m "openssl pil kivy"

#. Go to your fresh distribution, build the APK of your application::

    cd dist/default
    ./build.py --package org.test.touchtracer --name touchtracer \
    --version 1.0 --dir ~/code/kivy/examples/demo/touchtracer debug

#. Install the debug apk to your device::

    adb install bin/touchtracer-1.0-debug.apk

#. Enjoy.


Articles
========

.. seealso:: http://archlinux.me/dusty/2012/10/16/python-on-android-first-impressions-of-kivy/


