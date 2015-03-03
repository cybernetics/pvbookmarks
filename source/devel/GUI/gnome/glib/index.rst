
.. _glib:

====
glib
====

- http://en.wikipedia.org/wiki/GLib
- ftp://ftp.gtk.org/pub/glib/


GLib is a cross-platform software utility library that began as part 
of the GTK+  project, however, before releasing version 2 of GTK+, 
the project's developers decided to separate non-GUI-specific code 
from the GTK+ platform, thus creating GLib as a separate product. 
GLib was released as a separate library so other developers, those 
that did not make use of the GUI-related portions of GTK+, could make 
use of the non-GUI portions of the library without the overhead of 
depending on a full-blown GUI library.

Since GLib is a cross-platform library, applications using it to interface 
with the operating system are usually portable across different operating 
systems without major changes.


Similar projects
================

For many applications, C with GLib is an alternative to C++ with STL 
(see GObject for a detailed comparison).

The Apache Portable Runtime has a large functional overlap with GLib, 
and provides many similar OS-portable threading, network and data 
structure implementations in C.

Other widget toolkits usually also provide low-level functions and 
implementations of data structures. For instance, in the wxWidgets 
library the non-GUI functions are in the wxBase library, and in Qt 
the non-GUI parts are in the QtCore module, which is written in C++.

