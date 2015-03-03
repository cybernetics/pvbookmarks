


.. index::
   pair: Virtualization ; Boxes


==============
boxes
==============

.. toctree::
   :maxdepth: 4

.. seealso::

   - http://git.gnome.org/browse/gnome-boxes

.. image:: boxes-icon.png


How to help ?
=============

Seems many people are already very excited about this little project of ours and
I'm hoping this blog entry will attract more contributors so I wanted to point
out some things we need help with. If you are interested in UI work, Marc-Andre
has written down a TODO for Boxes that you can pick some tasks from. Other than
that, we still need a lot of help with two of our main dependencies:

- libosinfo: This library is our store for information on operating systems and
  means to detect operating systems from installation media.
- libvirt-glib: libvirt-glib wraps libvirt to provide a high-level object-oriented
  API better suited for glib-based applications.

While Boxes is written in Vala, these libraries are completely written in C so
if you are a C hacker and want to contribute, these would be good places to
start with. While most of the work needed on libosinfo is that of populating
its database with information on all kinds of operating systems out there,
libvirt-glib still lacks a lot of needed API. One particular part of libvirt-glib
that needs the most work and is of highest priority to us is its API to deal
with libvirt's configuration XML.






