


.. index::
   pair: Raster; Image
   pair: PIL ; frombuffer

.. _pil_raster_images:

============================
PIL raster images
============================


.. seealso::

   - http://www.pythonware.com/library/pil/handbook/concepts.htm
   - http://stackoverflow.com/questions/3397157/how-to-read-a-raw-image-using-pil

.. contents::
   :depth: 3


Introduction
============

The Python Imaging Library handles raster images; that is, rectangles of pixel
data.


Mode
====

The mode of an image defines the type and depth of a pixel in the image.

The current release supports the following standard modes:

- 1 (1-bit pixels, black and white, stored with one pixel per byte)
- L (8-bit pixels, black and white)
- P (8-bit pixels, mapped to any other mode using a colour palette)
- RGB (3x8-bit pixels, true colour)
- RGBA (4x8-bit pixels, true colour with transparency mask)
- CMYK (4x8-bit pixels, colour separation)
- YCbCr (3x8-bit pixels, colour video format)
- I (32-bit signed integer pixels)
- F (32-bit floating point pixels)

PIL also provides limited support for a few special modes, including

- LA (L with alpha),
- RGBX (true colour with padding)
- and RGBa (true colour with premultiplied alpha).

You can read the mode of an image through the mode attribute.

This is a string containing one of the above values.


PIL.Image.frombuffer(mode, size, data, decoder, parameters) ) => image
======================================================================

.. versionadded:: 1.1.4

**Creates an image memory from pixel data in a string or buffer object, using the
standard "raw" decoder**.

For some modes, the image memory will share memory with the original buffer
(this means that changes to the original buffer object are reflected in the image).

Not all modes can share memory; supported modes include:

- "L",
- "RGBX",
- "RGBA",
- and "CMYK".

For other modes, this function behaves like a corresponding call to the
fromstring function.

Note: In versions up to 1.1.6, the default orientation differs from that of
fromstring.

This may be changed in future versions, so for maximum portability, it's
recommended that you spell out all arguments when using the "raw" decoder:

::

    im = Image.frombuffer(mode, size, data, "raw", mode, 0, 1)



PIL.Image.frombuffer example1
=============================

::


    import sys
    import time
    import datetime
    import string
    import os
    import os.path
    import glob
    import getopt
    import ConfigParser
    import Tkinter
    import ImageTk

    # third-parties modules
    import serial
    import PIL
    from PIL import Image


    if Filename != None :
        ImageSize=(ImageWidth, ImageLength)
        ComputedSizeImage = ImageWidth * ImageLength;
        RealImageSize = len(ImageData) - ImageWidth*2
        RawData=ImageData[ImageWidth*2:]

        if len(RawData) != ImageWidth * ImageLength :
            raise RuntimeError("Unexpected image data size : expected %d, received %d" % (ImageWidth * ImageLength, len(RawData)))

        AcqTimeString = TimeStamp.strftime("%Y_%m_%d__%H_%M_%S_%f")[:-3]
        if Sensor != None :
            ImageName = "%s_%s_%s.%s" % (Filename, Sensor, AcqTimeString, Format)
        else :
            ImageName = "%s_%s.%s" % (Filename, AcqTimeString, Format)

        if(Format.lower() == "jpg"):
            Image = PIL.Image.frombuffer("L", ImageSize, RawData, "raw", "L", 0, 1)
            Image.save(ImageName, "JPEG")
        elif(Format.lower() == "bmp"):
            Image = PIL.Image.frombuffer("L", ImageSize, RawData, "raw", "L", 0, 1)
            Image.save(ImageName, "BMP")
        else:
            ImageFile = file(ImageName, "wb")
            ImageFile.write(RawData)
            ImageFile.close()
