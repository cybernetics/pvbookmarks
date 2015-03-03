
.. index::
   pair: Linux ; Systemd
   ! Systemd


.. _systemd:

=======
systemd
=======


.. seealso::

   - http://fr.wikipedia.org/wiki/Systemd
   - http://cgit.freedesktop.org/systemd/systemd/
   - http://www.freedesktop.org/wiki/Software/systemd
   - http://fedoraproject.org/wiki/Features/systemd
   - http://0pointer.de/blog/projects/socket-activation.html


Introduction
============

systemd is a system and service manager for Linux, compatible with SysV and
LSB init scripts. systemd provides aggressive parallelization capabilities,
uses socket and D-Bus activation for starting services, offers on-demand
starting of daemons, keeps track of processes using Linux cgroups, supports
snapshotting and restoring of the system state, maintains mount and automount
points and implements an elaborate transactional dependency-based service
control logic. It can work as a drop-in replacement for sysvinit.

See `Lennart's blog story`_ for a longer introduction, and the `two status` `updates`_
since then. Also see the `Wikipedia article`_.

In April 2012, the official udev source tree was merged into systemd.

.. _`Lennart's blog story`: http://0pointer.de/blog/projects/systemd.html
.. _`two status`: http://0pointer.de/blog/projects/systemd-update.html
.. _`updates`: http://0pointer.de/blog/projects/systemd-update-2.html
.. _`Wikipedia article`:  http://en.wikipedia.org/wiki/Systemd


.. _systemd_source_code:

Systemd Source code
===================

.. seealso::

   - http://cgit.freedesktop.org/systemd/systemd/
   - :ref:`udev_source_code`




Socket activation
=================

.. seealso:: http://0pointer.de/blog/projects/socket-activation.html

In the `original blog story`_ about systemd I tried to explain why socket
activation is a wonderful technology to spawn services. Let's reiterate the
background here a bit.

.. _`original blog story`: http://0pointer.de/blog/projects/systemd.html


systemd use cases
=================

.. toctree::
   :maxdepth: 4

   pcscd/index
