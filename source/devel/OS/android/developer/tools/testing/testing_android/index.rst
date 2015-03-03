

.. index::
   pair: Android; Monkeyrunner


.. _testing_android:


=====================
Testing android.html
=====================

.. seealso::

   - https://developer.android.com/tools/testing/testing_android.html


.. figure:: test_framework.png
   :align: center


monkey and monkeyrunner
=======================

The SDK provides two tools for functional-level application testing:

- The UI/Application Exerciser Monkey, usually called "monkey", is a
  command-line tool that sends pseudo-random streams of keystrokes, touches, and
  gestures to a device.
  You run it with the Android Debug Bridge (adb) tool. You use it to stress-test
  your application and report back errors that are encountered. You can repeat a
  stream of events by running the tool each time with the same random number seed.
- The monkeyrunner tool is an API and execution environment for test programs
  written in Python. The API includes functions for connecting to a device,
  installing and uninstalling packages, taking screenshots, comparing two images,
  and running a test package against an application.
  Using the API, you can write a wide range of large, powerful, and complex tests.
  You run programs that use the API with the monkeyrunner command-line tool.


What to Test
============

.. seealso::

   - https://developer.android.com/tools/testing/what_to_test.html

The topic What To Test describes the key functionality you should test in an
Android application, and the key situations that might affect that functionality.

Most unit testing is specific to the Android component you are testing.

The topics:

- `Activity Testing <https://developer.android.com/tools/testing/activity_testing.html>`_,
- `Content Provider Testing <https://developer.android.com/tools/testing/contentprovider_testing.html>`_,
- and `Service Testing <https://developer.android.com/tools/testing/service_testing.html>`_

each have a section entitled "What To Test" that lists possible testing areas.

**When possible, you should run these tests on an actual device.**

If this is not possible, you can use the `Android Emulator`_ with Android Virtual
Devices configured  for the hardware, screens, and versions you want to test.

.. _`Android Emulator`:  https://developer.android.com/tools/devices/emulator.html


Next Steps
===========

Testing with eclipse.html
-------------------------

.. seealso:: https://developer.android.com/tools/testing/testing_eclipse.html

To learn how to set up and run tests in Eclipse, please refer to `Testing from Eclipse
with ADT <https://developer.android.com/tools/testing/testing_eclipse.html>`.

If you're not working in Eclipse, refer to Testing from Other IDEs.

Step by step introduction
-------------------------

.. seealso:: https://developer.android.com/tools/testing/activity_test.html

If you want a step-by-step introduction to Android testing, try the `Activity
Testing Tutorial <https://developer.android.com/tools/testing/activity_test.html>`_.
