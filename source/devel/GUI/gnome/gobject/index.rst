
.. index::
   gobject

=======
gobject
=======

- http://en.wikipedia.org/wiki/GObject

The GLib  Object System, or GObject, is a free  software library 
(covered by the LGPL) providing a portable object system and transparent 
cross-language interoperability. GObject is designed for use both directly 
in C programs to provide object-oriented C-based APIs ;and through bindings 
to other languages to provide transparent cross-language interoperability.

History
=======

Depending only on GLib and libc, GObject is a cornerstone of GNOME and is 
used throughout GTK+, Pango, Accessibility Toolkit, and most higher-level 
GNOME libraries and applications. Prior to GTK+ 2.0, the GObject code was 
part of the GTK+ codebase. (The name “GObject” was not yet in use — the common 
baseclass was called GtkObject.)

The release of GTK+ 2.0 had the object system extracted into a separate 
library due to its general utility. In the process, most non-GUI-specific 
parts of the GtkObject class were moved up into GObject, the new common 
baseclass. 
Having existed as a separate library since March 11, 2002 (the release 
date of GTK+ 2.0), the GObject library is now used by many non-GUI programs 
such as command-line and server applications.

Relation to GLib
================

Though GObject has its own separate set of documentation and is usually 
compiled into its own shared library file, the source code for GObject 
resides in the GLib source tree and is distributed along with GLib. 
For this reason, GObject uses the GLib version numbers and is typically 
packaged together with GLib (for example, Debian puts GObject in its 
libglib2.0 package family).


.. _gobject_introspection:

gobject introspection
=====================

- http://live.gnome.org/GObjectIntrospection

Versions
========

0.9.3
-----

- 


0.6.14
-------

- http://ftp.gnome.org/pub/GNOME/sources/gobject-introspection/0.6/

