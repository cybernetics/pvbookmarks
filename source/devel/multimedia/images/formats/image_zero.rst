


.. index::
   pair: Format ; Image Zero


.. _image_zero_format:

============================================
Images zero format (iz, pronounced “easy”)
============================================

.. seealso:: http://imagezero.maxiom.de/

.. contents::
   :depth: 3



History (January 30, 2012 at 3:11 am)
=====================================

.. seealso::

   - http://kdepepo.wordpress.com/2012/01/30/fast-lossless-color-image-compression/


What does a programmer do, when he is not satisfied with what is available?
Right, he re-invents the world, only to make it better:

Last week, I released the initial version of ImageZero (iz, pronounced “easy”),
a high-performance lossless RGB photo codec.

Being twice as fast as PNG when decompressing (and more than 20 times faster
when compressing) it achieves compression ratios that are near or better than
PNG for natural photos, sometimes even better than JPEG-LS for very high quality
photos.

ImageZero is not intended for grayscale or artificial images, but I may improve
the algorithms for those image types.

Introduction
============


ImageZero ("IZ") is a low-level, high-performance, in-memory, lossless color
image compression C++ template library, available under BSD 2-clause license.

It is intended to be used by image database applications, photo manipulation
software, or other applications where simple RLE or no compression had been
used because of performance or complexity considerations.

IZ is designed with photographic images in mind, where other fast compression
algorithms (e.g. QuickLZ) fail to obtain any significant compression rate.

With IZ, the compressed size for natural 24-bit photographic images is usually
around 30% ... 50% of uncompressed size.

Depending on the image, IZ often compresses better than PNG or JPEG-LS.

For very compressible images, however, the compression rate can be much worse
than the rate obtained with any other compression algorithm.

IZ is a symmetric coder, meaning both compression as well as decompression need
about the same amount of time. On modern processors, the single-core performance
is up to 180 megabytes per second of 24-bit RGB pixel data.

IZ is optimized for modern processors, featuring small cache-friendly Huffman
coding tables and branchless implementations of nearly all operations.

IZ takes advantage of 64-bit architecture improvements (e.g. MMX registers), but
scales well to smaller or larger architectures.


Source code : https://gitorious.org/imagezero
=============================================

- https://gitorious.org/imagezero


Benchmarks
==========

.. seealso::

   - http://kdepepo.wordpress.com/2012/10/11/imagezero-5x-faster-than-webp/
   - http://www.imagecompression.info/gralic/LPCB.html

