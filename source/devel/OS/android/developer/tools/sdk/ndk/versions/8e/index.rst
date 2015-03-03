
.. index::
   pair: NDK ; 8e (Android)


.. _android_ndk_8e:

==================================
Android Ndk 8e (March 2013)
==================================


.. seealso::

   - https://developer.android.com/tools/sdk/ndk/index.html



Important changes
=================

- Added 64-bit host toolchain set (package name suffix *-x86_64.*).
  For more information, see CHANGES.HTML and NDK-BUILD.html.
- Added Clang 3.2 compiler. GCC 4.6 is still the default. For information on using
  the Clang compiler, see CHANGES.HTML.
- Added static code analyzer for Linux/MacOSX hosts. For information on using the
  analyzer, see CHANGES.HTML.
- Added MCLinker for Linux/MacOSX hosts as an experimental feature.
  The ld.gold linker is the default where available, so you must explicitly enable
  it. For more information, see CHANGES.HTML.
- Updated ndk-build to use topological sort for module dependencies, which means
  the build automatically sorts out the order of libraries specified in
  LOCAL_STATIC_LIBRARIES, LOCAL_WHOLE_STATIC_LIBRARIES and LOCAL_SHARED_LIBRARIES.
  For more information, see CHANGES.HTML. (Issue 39378)

