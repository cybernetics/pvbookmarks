.. module:: GUI
   :synopsis: GUI


.. index::
   gnome


.. _gnome_gui:

=====
gnome
=====

.. seealso::

   - http://en.wikipedia.org/wiki/GNOME
   - :ref:`gnome_desktop`

GNOME (abbreviation of GNU Network Object Model Environment) is a desktop
environment—a graphical user interface that runs on top of a computer
operating system—composed entirely of free and open source software.
It was created by two Mexican programmers, Miguel de Icaza and Federico Mena.
It is an international project that includes creating software development
frameworks, selecting application software for the desktop, and working on
the programs that manage application launching, file handling, and window
and task management.

GNOME is part of the GNU Project and can be used with various Unix-like
operating systems, most notably GNU/Linux, and as part of the
Java Desktop System in Solaris.

Major subprojects
=================

GNOME is built from a large number of different projects. A few of the major
ones are listed below:

* Bonobo – a (obsolete in current releases) compound document technology.
* GConf – for storing application settings.
* GVFS – a virtual file system.
* GNOME Keyring – for storing encryption keys and security information.
* GNOME Translation Project – translate documentation and applications into
  different languages.
* GTK+ – a widget toolkit used for constructing graphical applications. The
  use of GTK+ as the base widget toolkit allows GNOME to benefit from certain
  features such as theming (the ability to change the look of an application)
  and smooth anti-aliased graphics. Sub-projects of GTK+ provide object-oriented
  programming support (GObject), extensive support of international character
  sets and text layout (Pango) and accessibility (ATK).
  GTK+ reduces the amount of work required to port GNOME applications to
  other platforms such as Windows and Mac OS X.
* Human interface guidelines (HIG) – research and documentation on building
  easy-to-use GNOME applications.
* LibXML – an XML library.

A number of language bindings are available allowing applications to be written
in a variety of programming languages, such as C++ (gtkmm), Java (java-gnome),
Ruby (ruby-gnome2), C# (Gtk#), Python (PyGTK), Perl (gtk2-perl) and many others.
The only languages currently used in applications that are part of an official
GNOME desktop release are C, C#, Python and Vala.


.. toctree::
   :maxdepth: 5

   fontconfig/index
   pixman/index
   cairo/index
   glib/index
   atk/index
   pango/index
   gtk+/index
   pygobject/index
   pygtk/index
   pycairo/index
   gnome-python/index
   gobject/index










