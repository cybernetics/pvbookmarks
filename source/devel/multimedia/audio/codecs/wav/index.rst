

.. index::
   pair: Audio ; WAV
   ! WAV


.. _wav_codec:

==================================
WAV codec
==================================


.. seealso::

   - http://en.wikipedia.org/wiki/WAV

.. contents::
   :depth: 4


Introduction
============

Waveform Audio File Format (WAVE, or more commonly known as WAV due to its
filename extension), (also, but rarely, named, Audio for Windows) is a Microsoft
and IBM audio file format standard for storing an audio bitstream on PCs.

It is an application of the Resource Interchange File Format (RIFF) bitstream
format method for storing data in "chunks", and thus is also close to the 8SVX
and the AIFF format used on Amiga and Macintosh computers, respectively.

It is the main format used on Windows systems for raw and typically **uncompressed
audio**.

The usual bitstream encoding is the linear pulse-code modulation format.

Description
============

Both WAVs and AIFFs are compatible with Windows, Macintosh, and Linux operating
systems. The format takes into account some differences of the Intel CPU such as
little-endian byte order.

The RIFF format acts as a "wrapper" for various audio compression codecs.

Though a WAV file can hold compressed audio, the most common WAV format contains
uncompressed audio in the linear pulse code modulation (LPCM) format.

The standard audio file format for CDs, for example, is LPCM-encoded, containing
two channels of 44,100 samples per second, 16 bits per sample.

Since LPCM uses an uncompressed storage method which keeps all the samples of an
audio track, **professional users or audio experts may use the WAV format for
maximum audio quality**.

**WAV audio can also be edited and manipulated with relative ease using software**.

Popularity
==========

Uncompressed WAV files are large, so file sharing of WAV files over the Internet
is uncommon. However, it is a commonly used file type, suitable for retaining
first generation archived files of high quality, for use on a system where disk
space is not a constraint, or in applications such as audio editing, where the
time involved in compressing and uncompressing data is a concern.



