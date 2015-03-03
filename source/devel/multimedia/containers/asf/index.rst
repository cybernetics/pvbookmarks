

.. index::
   pair: Container ; AFS
   pair: Container ; Advanced Systems Format
   ! Advanced Systems Format


.. _asf_container:

==============================
ASF (Advanced Systems Format)
==============================


.. seealso::

   - http://en.wikipedia.org/wiki/Advanced_Systems_Format
   - http://en.wikipedia.org/wiki/Comparison_of_container_formats
   - :ref:`vorbis_codec`

.. contents::
   :depth: 4


Introduction
============

Advanced Systems Format (formerly Advanced Streaming Format, Active Streaming
Format) is Microsoft's proprietary digital audio/digital video container format,
especially meant for streaming media. ASF is part of the Windows Media framework.

ASF is based on serialized objects which are essentially byte sequences identified
by a GUID marker.

The format does not specify how (i.e. with which codec) the video or audio
should be encoded; it just specifies the structure of the video/audio stream.

This is similar to the function performed by the QuickTime, AVI, or Ogg container
formats.

One of the objectives of ASF was to support playback from digital media
servers, HTTP servers, and local storage devices such as hard disk drives.

The most common file types contained within an ASF file are:

- Windows Media Audio (WMA)
- and Windows Media Video (WMV).

Note that the file extension abbreviations are different from the codecs which
have the same name. The current version of Windows Media Encoder produces files
with the extension .WMA (and MIME-type 'audio/x-ms-wma') and
.WMV (MIME-type 'video/x-ms-asf').

These files are identical to the old .ASF files but for their extension and MIME-type.
According to Microsoft, the change in extensions was made to make it easier for
an application to identify the content of a media file (see Q284094).

Although this differentiation was introduced in 2003, to this date most webbrowsers
(including the latest versions of Internet Explorer and Firefox) do not function
as might be expected with the 'new' extensions: even when a .wma or .wmv file is
specifically encoded for progressive download, browsers still proceed to completely
download the file before playing it.

This can, however, be easily remedied by simply renaming the .wma or .wmv file
to the old extension .asf.

ASF files can also contain objects representing metadata, such as the artist,
title, album and genre for an audio track, or the director of a video track,
much like the ID3 tags of MP3 files. It supports scalable media types and stream
prioritization; as such, it is a format optimized for streaming.

The ASF container provides the framework for digital rights management in
Windows Media Audio and Windows Media Video. An analysis of an older scheme used
in WMA reveals that it is using a combination of elliptic curve cryptography key
exchange, DES block cipher, a custom block cipher, RC4 stream cipher and the
SHA-1 hashing function.

ASF container-based media are sometimes still streamed on the internet either
through the MMS protocol or the RTSP protocol.

Mostly, however, they contain material encoded for 'progressive download', which
can be distributed by any webserver and then offers the same advantages as
streaming: **the file starts playing as soon as a minimum number of bytes is
received** and the rest of the download continues in the background while one
is watching or listening.



