
.. index::
   pcsc (systemd)


.. _systemd_and_pcscd:

=================
systemd and pcscd
=================


.. seealso::

   - http://ludovicrousseau.blogspot.com/2011/11/pcscd-auto-start-using-systemd.html


.. image:: by_nc_sa.png

License: by-nc-sa
Creative Commons Licence
This blog by Ludovic Rousseau is licensed under a Creative
Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

Tuesday, November 15, 2011 pcscd auto start using systemd
=========================================================


In pcsc-lite version 1.6.0 (5 May 2010) I introduced a mechanism to start the
pcscd daemon only when an application called ``SCardstablishContext()`` to get a
PC/SC context.

Read `Configuring your system for pcscd auto-start`_ for more information.


.. _`Configuring your system for pcscd auto-start`: http://ludovicrousseau.blogspot.com/2010/12/configuring-your-system-for-pcscd-auto.html

Old way: start by the libpcsclite library
=========================================

One of the problem is that pcscd is then started as the user running the
application. The pcscd process has to be setgid to get special privileges to
get access to the USB devices (the smart card readers). Some people (and I understand)
do not like files with special access right (like setgid).

New way: systemd
================

Around the same time (23 Aug 2010) the `first article`_ about systemd was posted
by systemd author: Lennart Poettering

.. _`first article`:  http://0pointer.de/blog/projects/systemd-for-admins-1.html

Socket activation
-----------------

I will not describe systemd in details. But one of the services of systemd is to
start a process when an application tries to communicate to a socket. The good
news is that libpcsclite and pcscd are communicating through a UNIX (local)
socket. So systemd provides a way to start pcscd when libpcsclite starts the
communication.

The good news is that the changes are really minimal. libpcsclite has not changed
and only the initialisation of pcscd has been updated a bit to use systemd services.

systemd configuration
=====================

pcsc-lite now use 2 systemd configuration files: :file:`pcscd.service` and :file:`pcscd.socket`

File pcscd.service
------------------

::

    [Unit]
    Description=PC/SC Smart Card Daemon
    Requires=pcscd.socket

    [Service]
    ExecStart=/usr/sbin/pcscd --foreground --auto-exit
    ExecReload=/usr/sbin/pcscd --hotplug
    StandardOutput=syslog

    [Install]
    Also=pcscd.socket


File pcscd.socket
-----------------

::

    [Unit]
    Description=PC/SC Smart Card Daemon Activation Socket

    [Socket]
    ListenStream=/var/run/pcscd/pcscd.comm

    [Install]
    WantedBy=sockets.target


These two files are installed in /lib/systemd/system/ on my Debian (testing)
system.

Status
======

::

    $ systemctl status pcscd.service
    pcscd.service - PC/SC Smart Card Daemon
       Loaded: loaded (/lib/systemd/system/pcscd.service)
       Active: inactive (dead) since Mon, 14 Nov 2011 16:33:40 +0100; 17h ago
      Process: 15489 ExecStart=/usr/sbin/pcscd --foreground --auto-exit (code=exited, status=0/SUCCESS)
       CGroup: name=systemd:/system/pcscd.service


::

    $ systemctl status pcscd.socket
    pcscd.socket - PC/SC Smart Card Daemon Activation Socket
       Loaded: loaded (/lib/systemd/system/pcscd.socket)
       Active: active (listening) since Mon, 14 Nov 2011 14:49:45 +0100; 19h ago
       CGroup: name=systemd:/system/pcscd.socket


The pcscd socket is configured and active but the pcscd process is not running.
After starting a PC/SC application we get:

::

    $ systemctl status pcscd.service
    pcscd.service - PC/SC Smart Card Daemon
       Loaded: loaded (/lib/systemd/system/pcscd.service)
       Active: active (running) since Tue, 15 Nov 2011 10:27:39 +0100; 9s ago
     Main PID: 26929 (pcscd)
       CGroup: name=systemd:/system/pcscd.service
        └ 26929 /usr/sbin/pcscd --foreground --auto-exit

Stop
====

It is possible to stop the running pcscd process.

::

    $ sudo systemctl stop pcscd.service
    $ systemctl status pcscd.service
    pcscd.service - PC/SC Smart Card Daemon
       Loaded: loaded (/lib/systemd/system/pcscd.service)
       Active: failed since Tue, 15 Nov 2011 10:30:13 +0100; 1s ago
      Process: 26965 ExecStart=/usr/sbin/pcscd --foreground --auto-exit (code=exited, status=1/FAILURE)
       CGroup: name=systemd:/system/pcscd.service


But in general I just kill(1) the pcscd process.

Start
=====

If you start pcscd by hand, for example in debug and foreground mode, the daemon
will remove the socket /var/run/pcscd/pcscd.comm on exit. This socket is not
recreated automatically by systemd. You need to stop and start the pcscd.socket,
using just start is not enough.

::

    $ ls /var/run/pcscd/pcscd.comm
    ls: cannot access /var/run/pcscd/pcscd.comm: No such file or directory
    $ sudo systemctl stop pcscd.socket
    $ sudo systemctl start pcscd.socket
    $ ls /var/run/pcscd/pcscd.comm
    /var/run/pcscd/pcscd.comm


The pcscd process is not started but the socket is now listening.

Migration
=========

I removed the old autostart code in revision 6105. If you have systemd installed
on your system I recommend using it to start pcscd. If you do not have systemd
installed (maybe you do not use a Linux kernel) then you have to start pcscd
at boot (as before version 1.6.0).

systemd availability
====================

``systemd`` is only available with a Linux kernel. systemd is now installed by
default in Fedora 14. systemd is provided by Debian but Debian is not just
limited to a Linux kernel. Debian also provides Hurd and FreeBSD kernel based
Debian systems and systemd is not (yet) available for these kernels.

Major GNU/Linux distributions should provide ``systemd`` now. If your distribution
do not have systemd you can still use the old way of starting pcscd at boot.

For non-Linux systems I have no auto-start solution. Just start ``pcscd`` at boot.

Conclusion
==========

``systemd`` is a nice new system to replace init and a lot more. It is a good piece
of code to implement auto start for pcsc-lite.

Thanks to Kalev Lember for pushing the systemd patches.

