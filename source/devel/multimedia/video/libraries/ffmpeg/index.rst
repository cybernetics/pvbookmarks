

.. index::
   Video (ffmpeg library)


.. _ffmpeg_video_library:

=====================
ffmpeg video library
=====================

.. seealso::

   - :ref:`ffmpeg_audio_library`
   - http://ffmpeg.org/index.html
   - http://ffmpeg.org/about.html
   - http://www.commandlinefu.com/commands/tagged/76/ffmpeg
   - http://pypi.python.org/pypi/wffmpeg/0.1.1
   - :ref:`libav`
   - :ref:`video_ffmpeg_scripts`

.. image:: ffmpeg-logo.png


.. contents::
   :depth: 3


Project Description
===================

``FFmpeg`` is a complete, cross-platform solution to record, convert and stream
audio and video.

It includes:

- libavcodec_, the leading open source codec library
- libavformat (implementing muxers and demuxers),
- libswscale (for very fast video scaling),
- libavfilter (an advanced video filter system supporting arbitrary filter graphs),
- libavutil (a utility library intended to supplement libc).

A simple multimedia player is included too. An experimental streaming server
for live broadcasts is also included.

FFmpeg is free software licensed under the LGPL or GPL depending on your choice
of configuration options. If you use FFmpeg or its constituent libraries,
you must adhere to the terms of the license in question. You can find basic
compliance information and get licensing help on our license and legal
considerations page.

The project is made of several components:

- ffmpeg is a command line tool to convert multimedia files between formats.
- ffserver is a multimedia streaming server for live broadcasts.
- ffplay is a simple media player based on SDL and the FFmpeg libraries.
- ffprobe is a is a simple multimedia stream analyzer.
- libavutil is a library containing functions for simplifying programming,
  including random number generators, data structures, mathematics routines,
  core multimedia utilities, and much more.
- libavcodec is a library containing decoders and encoders for audio/video codecs.
- libavformat is a library containing demuxers and muxers for multimedia
  container formats.
- libavdevice is a library containing input and output devices for grabbing
  from and rendering to many common multimedia input/output software frameworks,
  including Video4Linux, Video4Linux2, VfW, and ALSA.
- libavfilter is a library containing media filters.
- libswscale is a library performing highly optimized image scaling and color
  space/pixel format conversion operations.



.. _libavcodec: https://fr.wikipedia.org/wiki/Libavcodec

.. _documentation: http://ffmpeg.org/ffmpeg.html


Commandlinefu
=============

.. seealso:: http://www.commandlinefu.com/commands/tagged/76/ffmpeg


FFmpeg source code
==================

.. seealso::

   - http://git.videolan.org/?p=ffmpeg.git;a=tree

FFmpeg is developed with Git.

Given the decentralized nature of Git, multiple repositories from developers and
groups of developers are available.

::

    git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg




FFmpeg download
===============

.. seealso::

   - http://ffmpeg.org/download.html


FFmpeg windows download
-----------------------

.. seealso::

   - http://ffmpeg.zeranoe.com/builds/



ffmpeg history
==============

.. toctree::
   :maxdepth: 3

   history


Versions
========

.. toctree::
   :maxdepth: 4

   versions/index

Wrappers
========

.. toctree::
   :maxdepth: 4

   wrappers/index







