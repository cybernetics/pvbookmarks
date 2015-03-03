
.. index::
   pair: NDK ; 8 (Android)


.. _android_ndk_8:

==================================
Android Ndk 8 (Maay 2012)
==================================


.. seealso::

   - https://developer.android.com/tools/sdk/ndk/index.html



Important changes
=================

This release of the NDK includes support for MIPS ABI and a few additional fixes.

New features
============

Added support for the MIPS ABI, which allows you to generate machine code that
runs on compatible MIPS-based Android devices. Major features for MIPS include
MIPS-specific toolchains, system headers, libraries and debugging support.

For more details regarding MIPS support, see docs/CPU-MIPS.html in the NDK package.

By default, code is generated for ARM-based devices. You can add mips to your
APP_ABI definition in your Application.mk file to build for MIPS platforms.

For example, the following line instructs ndk-build to build your code for three
distinct ABIs::

    APP_ABI := armeabi armeabi-v7a mips

Unless you rely on architecture-specific assembly sources, such as ARM assembly
code, you should not need to touch your Android.mk files to build MIPS machine code.

You can build a standalone MIPS toolchain using the --arch=mips option when calling
make-standalone-toolchain.sh. See docs/STANDALONE-TOOLCHAIN.html for more details.

