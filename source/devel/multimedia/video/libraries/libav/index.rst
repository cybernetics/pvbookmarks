

.. index::
   libav (see ffmpeg)


.. _libav:

=======
libav
=======


.. seealso::

   - http://libav.org/


.. contents::
   :depth: 3

Introduction
============

Libav is a complete, cross-platform solution to record, convert and stream audio
and video. It includes libavcodec - the leading audio/video codec library.

See the documentation_ for a complete feature list and the Changelog for recent changes.

.. _documentation : http://libav.org/ffmpeg.html


Features
========

We strive to implement and provide useful and innovative features in a timely
fashion, provide stable release and interact to the best of our abilities
with our downstream such as distributors and end users. For instance, most of
the ffmpeg-mt work has been merged into Libav for quite some time.

This work is still ongoing, we are still working hard to fix the remaining
issues such as with multi-threaded h264 decoding.

We are not afraid to overhaul radically our code in order to provide a better
foundation for future works and we prefer to spend effort to get clean code
right instead of piling up special cases and heuristics.

We are patient enough to track bugs and corner cases until they are
completely solved

With the help of our users we try to improve the experience of using both the
libraries and the tools

We try to focus both on real world issues as well on experiments that might
lead to new interesting outcomes.

**We are happy to learn that the now arisen competition has finally lead FFmpeg
to merge important and long requested features such as frame based
multi-threaded decoding based on ffmpeg-mt, something the project leader
strongly refused to merge during our attempts to reconcile with him**.



.. index::
   libav history


.. _libav_history:

libav History
=============

March 13, 2011
--------------

We, as a group of FFmpeg developers, have decided to continue developing FFmpeg
under the name Libav. All existing infrastructure will be transferred to the
libav.org domain.

============ ================================================================
Website:     http://www.libav.org/
Git:         git://git.libav.org/libav.git (see http://libav.org/download.html)
FATE:        http://fate.libav.org/
Roundup:     https://roundup.libav.org/
Patchwork:   http://patches.libav.org/
Mailinglists http://lists.libav.org/ (developer list: libav-devel@libav.org)
============ ================================================================

You can update your git repository using the following command::

    git remote set-url origin 'git://git.libav.org/libav'

For now we are still reachable over FFmpeg's mailing lists and IRC channels but
we will migrate to libav.org counterparts. For a transition period both the
website and source might still contain references to FFmpeg.

These will disappear over time, except where historically relevant.



Visual studio compilation
=========================

.. seealso:: http://blogs.gnome.org/rbultje/2012/09/27/microsoft-visual-studio-support-in-ffmpeg-and-libav/



An often-requested feature for FFmpeg is to compile it using Microsoft Visual
Studio’s C compiler (MSVC). The default (quite arrogant) answer used to be that
this is not possible, because the godly FFmpeg code is too good for MSVC.

Usually this will be followed by some list of C language features/extensions
that GCC supports, but MSVC doesn’t (e.g. compound literals, designated
initializers, GCC-style inline assembly).

There are complete patches and forks related to this one single feature.

Reality is, many of these C language features are cosmetic extensions introduced
in C99 that are trivially emulated using classic C89 syntax. Consider designated
initializers::

    struct {
        int a, b;
    } var = { .b = 1, };

This can be trivially emulated in C89 by using the following syntax::

    struct {
        int a, b;
    } var = { 0, 1 };

For unions, you can change the initialization (as long as the size of the first
field is large enough to hold the contents of any other field in the union) to
do a binary translation of the initialized field type to the first field type::

    union {
        unsigned int a;
        float b;
    } var = { .b = 1.0, };

becomes:::

    union {
        unsigned int a;
        float b;
    } var = { 0x3f800000, };

Here, 0x3f800000 is the binary representation of the floating point number 1.0.
If the value to be converted is not static, the assignment can simply become a
statement on its own::

    union {
        unsigned int a;
        float b;
    } var;
    var.b = 1.0;

Other C99 language features (e.g. compound literals) can be translated in a
similar manner::

    struct {
        int *list;
    } var = { (int *) { 0, 1 } };

becomes::

    int *list = { 0, 1 };
    struct {
        int *list;
    } var = { list };

Two other Libav developers (Derek Buitenhuis and Martin Storsjo) and I wrote a
conversion tool that automatically translates these C99 language features to
C89-compatible equivalents. With this tool, the FFmpeg and Libav source trees
can be translated and subsequently compiled with MSVC.

A wrapper is provided so that you can tell the FFmpeg build script to use that
as compiler. The wrapper will then (internally) call the conversion utility to
convert the source file from C99 to C89, and then it calls the MSVC build tools
to compile the resulting “C89′ified source file”. In the end, this effectively
means FFmpeg and Libav can be compiled with MSVC, and the resulting binaries
are capable of decoding all media types covered by the test suite (32bit, 64bit)
and can be debugged using the Visual Studio debugger.




