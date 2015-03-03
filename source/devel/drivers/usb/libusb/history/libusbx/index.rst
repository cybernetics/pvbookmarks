

.. index::
   pair: USB ; Libusbx
   pair: fork; Libusbx
   ! Libusbx


.. _libusbx:

===========
libusbx
===========

.. seealso::

   - http://www.libusbx.org/
   - :ref:`ludovic_rousseau`


.. figure:: libusbx.png
   :align: center

   Libusbx logo


.. contents::
   :depth: 3


Warning
========


.. warning:: libusbx was a fork of libusb, a library that provides generic 
   access to USB devices.

   As of 2014.01.26, this project has been fully merged back into libusb and is 
   being discontinued.

   Since there will be no further releases of libusbx, you are strongly 
   encouraged to switch to using libusb. 


Migrating to libusb
=====================

If you are an existing libusbx user:

As far as the library binary and header are concerned, since libusb and libusbx 
use the same names and have the same API, you just need to replace your deployed 
libusbx files with the libusb ones. That's all!

::

    The SourceForge project changes from
    https://sourceforge.net/projects/libusbx/ to
    https://sourceforge.net/projects/libusb/
    The mailing list changes from
    libusbx-devel@lists.sourceforge.net to
    libusb-devel@lists.sourceforge.net
    The API documentation changes from
    http://libusbx.sourceforge.net/api-1.0/ to
    http://libusb.sourceforge.net/api-1.0/
    The git repository changes from
    git://github.com/libusbx/libusbx.git to
    git://github.com/libusb/libusb.git
    The Homepage changes from
    http://libusbx.org to
    http://libusb.info
    The github project (Wiki, issue tracker, etc.) changes from
    https://github.com/libusbx/libusbx to
    https://github.com/libusb/libusb


Overview
=========

``libusbx`` is a library for USB device access from Linux, Mac OS X,
Windows and OpenBSD/NetBSD userspace, with OpenBSD/NetBSD, and to a
lesser extent some of the newest features of Windows (such as libusbK
and libusb-win32 driver support) being EXPERIMENTAL.

It is written in C and licensed under the GNU Lesser General Public
License version 2.1 or, at your option, any later version (see COPYING).

libusbx is abstracted internally in such a way that it can hopefully
be ported to other operating systems. Please see the PORTING file
for more information.

libusbx homepage: http://libusbx.org/

Developers will wish to consult the API documentation: http://api.libusbx.org

Use the mailing list for questions, comments, etc:  http://mailing-list.libusbx.org

- Pete Batard <pete@akeo.ie>
- Hans de Goede <hdegoede@redhat.com>
- Xiaofan Chen <xiaofanc@gmail.com>
- Ludovic Rousseau <ludovic.rousseau@gmail.com>


Is libusbx a fork of libusb?
============================


Yes it is.

The reason for the fork is that, despite having dedicated members, libusb has
still not been able to produce a new release for the past 2 years.

When a project fails to produce regular releases, we consider that you, its
user, are paying the ultimate price. This is because it means that patches and
new feature are being witheld and you end up wasting your time.

We are the same dedicated team who tirelessy tried to improve libusb but saw
our efforts being wasted there.

After using libusbx for a while and after dealing with our great community, we
hope that you will be as convinced as we are that there exists a better way!


What are the advantages of libusbx over libusb ?
================================================

Apart from frequent releases, which include regular bugfixes as well as exciting
new features (please check our roadmap), you should find that we are a lot more
responsive and that, rather than focus our efforts on elements that are of little
interest to you, or an ever delayed promise of "better" features that fail to
materialize, we strive to bring you the best possible user and developer experience
today.

Also, unlike libusb, we fully subscribe to the Release Early, Release Often (RERO)
philosophy, upon which the success of the Linux kernel and countless other
Open Source projects is based.

Finally, if there's anything the failure of libusb has taught us, it's that a
project should never fail to listen to you, its user...

As such, libusbx is as much your library as it is ours, and we hope that you
will engage with us to help make it even greater!


libusbx milestones
==================

.. seealso::

   - https://github.com/libusbx/libusbx/issues/milestones
   - https://github.com/libusbx/libusbx/issues/milestones?direction=asc&sort=due_date


libusbx source code
===================

.. seealso::

   - https://github.com/libusbx
   - https://github.com/libusbx/libusbx


The latest development tree is always available from git.

For those not familiar with git, here are the commands one can use to retrieve libusbx:

# retrieve development branch (this only needs to be done once)::

    git clone git://github.com/libusbx/libusbx.git
    cd libusbx

# for further updates, once the clone has been done::

    git pull

You can also browse the git development tree from https://github.com/libusbx/libusbx.

Also note that, when compiling from git, you may have to run ./autogen.sh, ./bootstrap.sh
or run the autotools creation utilities, in order to have configure and Makefile
created for you.

The difference between autogen.sh and bootstrap.sh is that the former will invoke
configure with a set of default options, whereas the latter will not.

To create projects relying on libusbx, please refer to the samples in the
examples/ subdirectory.


libusbx people
==============

.. toctree::
   :maxdepth: 3

   people/index



libusbx logs
============

.. seealso::

   - http://log.libusbx.org
   - https://github.com/libusbx/libusbx/commits/master.atom


Libusbx versions
================

.. toctree::
   :maxdepth: 3

   versions/index

Libusbx wrappers
================

.. toctree::
   :maxdepth: 3

   libusbx_cplusplus_wrapper


