

.. index::
   pair: Drawing ; GIMP
   ! GIMP


.. _drawing_raster_gimp:

=====================================
GIMP (GNU Image Manipulation Program)
=====================================

.. seealso::

   - https://fr.wikipedia.org/wiki/Gimp
   - http://www.gimp.org/

.. image:: 80px-GIMP_Icon.svg.png


.. contents::
   :depth: 3

Introduction
==============

GIMP (GNU Image Manipulation Program) is a free software raster graphics editor.

It is primarily employed as an image retouching and editing tool and is
freely available in versions tailored for most popular operating systems
including Microsoft Windows, Apple Mac OS X, and Linux.

In addition to detailed image retouching and free-form drawing, GIMP can
accomplish essential image editing tasks such as resizing, editing, and
cropping photos, photomontages combining multiple images, and converting
between different image formats.

GIMP can also be used to create animated images in many formats such as GIF
and MPEG through the Animation Plugin.


Windows GIMP
============

.. seealso:: http://gimp-win.sourceforge.net/index.html


Install with chocolatey
------------------------

.. seealso::

   - :ref:`choco`
   - http://chocolatey.org/packages/gimp

::

    cinst gimp 


Automation, scripts and plug-ins
================================

GIMP has approximately 150 standard effects and filters, including Drop Shadow,
Blur, Motion Blur and Noise.

GIMP operations can be automated with scripting languages. The Script-Fu is a
Scheme based extension language implemented using TinyScheme.

GIMP can also be scripted in Perl, :ref:`Python <python_language>` (Python-fu), or Tcl. New features
can be added to GIMP not only by changing program code (GIMP core), but also
by creating plug-ins.

These are external programs that are executed and controlled by the main
GIMP program. MathMap is an example of a plug-in written in C.


.. toctree::
   :maxdepth: 4


   plugins/index


