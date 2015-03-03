
.. index::
   pair: Desktop toolkit; GTK+

.. _GTK_plus:

===================
GTK+
===================

.. seealso::

   - http://en.wikipedia.org/wiki/GTK%2B

::

    git clone git://git.gnome.org/gtk+



.. figure:: logoGtk+.svg.png

   *Logo GTK+*

GTK+ (GIMP Toolkit) is a cross-platform widget toolkit for creating graphical
user interfaces. It is licensed under the terms of the GNU LGPL, allowing both
free and proprietary software to use it.

It is one of the most popular toolkits for the X Window System, along with Qt.


The name GTK+ originates from GTK; the plus was added to distinguish an enhanced
version.

It was originally created for the GNU Image Manipulation Program (GIMP), a free
software raster graphics editor, in 1997 by Spencer Kimball and Peter Mattis,
members of eXperimental Computing Facility (XCF) at the University of California,
Berkeley. It is now maintained by members of the GNOME Foundation.


Design
======

GTK+ is an object-oriented widget toolkit written in the C programming language;
object-orientation is achieved by using the GLib object system.

On the X11  display server, GTK+ uses Xlib to draw widgets.

Using Xlib provides flexibility and allows GTK+ to be used on platforms where
the X Window System is unavailable.

While GTK+ is primarily targeted at the X Window System, other platforms are
supported, including Microsoft Windows (interfaced with the Windows API),
and Mac OS X (interfaced with Quartz).

**HTML5 and Wayland backends are in development**

GTK+ can be configured to change the look of the widgets drawn; this is done
using different display engines. Several display engines exist which try to
emulate the look of the native widgets on the platform in use.




Where can I use it ?
====================

Everywhere! GTK+ is cross-platform and boasts an easy to use API, speeding up
your development time. Take a look at the screenshots to see a number of
platforms GTK+ will run.

What languages are supported ?
==============================

GTK+ is written in C but has been designed from the ground up to support a wide
range of languages, not only C/C++. Using GTK+ from languages such as Perl and
Python (especially in combination with the Glade GUI builder) provides an
effective method of rapid application development.


Are there any licensing restrictions ?
======================================

.. seealso:: http://www.gtk.org/commerce.php

GTK+ is free software and part of the GNU Project. However, the licensing
terms for GTK+, the GNU LGPL, allow it to be used by all developers, including
those developing proprietary software, without any license fees or royalties.

Get an overview of GTK+. Understand who started it, the basic architecture and
why we use the license we do.

GTK+ has been involved in many projects and some big platforms.

To get a glimpse of what people think of GTK+ and how it has been used in
commercial projects, read the `success stories`_...

.. _`success stories`:  http://www.gtk.org/commerce.php


.. toctree::
   :maxdepth: 4

   versions/index





