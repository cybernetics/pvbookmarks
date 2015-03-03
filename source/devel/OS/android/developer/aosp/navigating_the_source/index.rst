


======================
Navigating the Source
======================


.. contents::
   :depth: 3



Platform Overview
=================


.. toctree::
   :maxdepth: 3

   platform_overview/index



Branches & Releases
===================

.. seealso::

   - http://source.android.com/source/code-lines.html

The Android Open Source Project maintains a complete software stack intended to
be ported by OEMs and other device implementors to run on actual hardware.

Accordingly, we maintain a number of "code lines" to clearly separate the current
stable version of Android from unstable experimental work.

The chart below depicts at a conceptual level how AOSP manages code and releases.

We're referring to these as "code lines" instead of "branches" simply because at
any given moment there may be more than one branch extant for a given "code line".

For instance, when a release is cut, sometimes that will become a new branch in
git, and sometimes not, based on the needs of the moment.



.. _android_build_numbers:

Android Build Numbers
=====================


.. seealso::

   - http://source.android.com/source/build-numbers.html
   - :ref:`android_platforms`
   - :ref:`android_os_versions`

The code names match the following version numbers, along with API levels and NDK
releases provided for convenience:

================== ================== =================
Code name          Version            API level
================== ================== =================
(no code name)     1.0                API level 1
(no code name)     1.1                API level 2
Cupcake            1.5                API level 3, NDK 1
Donut              1.6                API level 4, NDK 2
Eclair             2.0                API level 5
Eclair             2.0.1              API level 6
Eclair             2.1                API level 7, NDK 3
Froyo              2.2.x              API level 8, NDK 4
Gingerbread        2.3 - 2.3.2        API level 9, NDK 5
Gingerbread        2.3.3 - 2.3.7      API level 10
Honeycomb          3.0                API level 11
Honeycomb          3.1                API level 12, NDK 6
Honeycomb          3.2.x              API level 13
Ice Cream Sandwich 4.0.1 - 4.0.2      API level 14, NDK 7
Ice Cream Sandwich 4.0.3 - 4.0.4      API level 15, NDK 8
Jelly Bean         4.1.x              API level 16
Jelly Bean         4.2.x              API level 17
================== ================== =================

