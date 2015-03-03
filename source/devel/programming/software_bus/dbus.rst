

.. index::
   dbus

.. _dbus:

====
dbus
====

.. seealso:: 

   - :ref:`dbus_interprocess_communication` 
   - http://www.freedesktop.org/wiki/IntroductionToDBus
   - http://fr.wikipedia.org/wiki/Dbus
   - http://en.wikipedia.org/wiki/D-Bus
   

En informatique, D-Bus est un système de communication inter-processus simple 
permettant aux logiciels de communiquer entre eux.

Hautement influencé par le système DCOP implémenté dans KDE 2 et KDE 3, il l'a 
remplacé dans KDE 4.

Red Hat est le développeur principal de D-Bus, en tant qu'élément du projet 
freedesktop.org. 
`Freedesktop.org`_ diffuse D-Bus sous les termes de la licence publique générale 
GNU et la Licence Académique Libre en tant que logiciel libre.


.. _`Freedesktop.org`: http://fr.wikipedia.org/wiki/Freedesktop.org

.. index::
   DBUS bindings
   GLib 
   main loop (GLIB)
   
   
DBUS bindings
=============

D-Bus bindings are available for an increasing number of languages. 
There is a low-level C binding, but that is probably too detailed and 
cumbersome for anything but writing other bindings. A more practical C binding 
is based on `GLib`_. There are also `Java`_, Perl and Python bindings (about we also 
have notes and examples), and so on. 

.. _`Java`: http://dbus.freedesktop.org/doc/dbus-java/
.. _`GLib`: http://dbus.freedesktop.org/doc/dbus-glib/index.html


API for using D-BUS with GLib
-----------------------------

.. seealso:: http://dbus.freedesktop.org/doc/dbus-glib/index.html


libdbus proper is a low-level API, these GLib bindings wrap libdbus with a 
much higher-level approach. The higher level approach is possible because 
GLib defines a main loop, an object/type system, and an out-of-memory 
handling policy (it exits the program). 
See http://www.gtk.org for GLib information.
