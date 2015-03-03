
.. index::
   DBUS
   dbus interprocess communication


.. _dbus_interprocess_communication:

=================================
D-BUS Interprocess communication
=================================

.. image:: diagram_dbus.png


.. seealso::

   - http://www.freedesktop.org/wiki/Software/dbus
   - http://blog.fpmurphy.com/2011/08/introduction-to-udisks.html



D-Bus is a message bus system, a simple way for applications to talk to one
another.

In addition to ``interprocess`` communication, D-Bus helps coordinate process
lifecycle; it makes it simple and reliable to code a "single instance"
application or daemon, and to launch applications and daemons on demand when
their services are needed.

D-Bus supplies both a system daemon (for events such as **"new hardware device added"**
or "printer queue changed") and a per-user-login-session daemon (for general IPC
needs among user applications). Also, the message bus is built on top of a general
one-to-one message passing framework, which can be used by any two apps to
communicate directly (without going through the message bus daemon).

Currently the communicating applications are on one computer, or through
unencrypted TCP/IP suitable for use behind a firewall with shared NFS home
directories. (Help wanted with better remote transports -
the transport mechanism is well-abstracted and extensible.)


.. toctree::
   :maxdepth: 4

   examples/index
   tools/index
   smartcard/index


