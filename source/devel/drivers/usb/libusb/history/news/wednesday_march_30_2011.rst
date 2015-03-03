

.. index::
   libpcsc Ludovic Rousseau


.. _libusb_ludovic_rousseau:

===============================================
Wednesday, March 30, 2011 from Ludovic Rousseau
===============================================

.. seealso::

   - http://ludovicrousseau.blogspot.com/2011/03/new-version-of-libusb.html
   - http://ludovic.rousseau.free.fr/softwares/pcsc-lite/





My CCID driver uses libusb-1.0 to talk to USB readers.

libusb evolution stalled
========================

The latest version 1.0.8 of libusb-1.0 was released in `May 2010 <http://sourceforge.net/projects/libusb/files/libusb-1.0/>`_ (nearly a year
ago). Since then many bugs have been reported and most have been fixed in the
git repository.

The problem is that now new stable or 1.0.9 version has been released since
May 2010. So if you suffer from a bug in libusb it is not easy to update it.

libusb git snapshot
===================

To ease the use of a more up-to-date version of libusb-1.0 I made a snapshot of
the version in the git repository and provide it on my web page of beta versions
or http://ludovic.rousseau.free.fr/softwares/pcsc-lite/

The files in the libusb git repository have not evolved in the last 6 months so
I do not expect to have to make a new snapshot within the next 6 months.

I sent a mail on the `libusb mailing list`_.


.. _`libusb mailing list`: http://sourceforge.net/mailarchive/forum.php?thread_name=AANLkTinp3vS0bemKC4Us6-23g4QyaE%2BgRjS5MyuT1HNr%40mail.gmail.com&forum_name=libusb-devel

Conclusion
==========

So before reporting a bug in libccid first try a newer version of libusb. If the
bug is at the communication level it may already be solved in the `libusb snapshot version`_.

.. _`libusb snapshot version`:  http://ludovic.rousseau.free.fr/softwares/pcsc-lite/



[Libusb-devel] GIT snapshot available
=====================================

::

    From: Ludovic Rousseau <ludovic.rousseau@gm...> - 2011-03-30 07:10

Hello,

Some users report problems with my application but the problems are in
fact in libusb. Often/always the problems have already been fixed but
the code is not yet released in a stable libusb (1.0.9) version.

So I decided to distribute a .tar.bz2 `[1]`_ from GIT so that my users
can rebuild libusb themself without using git and autotools.

The last commit in the libusb.git repo dates back to October 2010 (6
months ago). And I do not expect any change in the next 6 months. So a
nigthly, weekly, monthly or yearly snapshot is the same. Updating my
snapshot to a newer version should not take more than 5 minutes each
year.

The libusb project is making me lose my time, energy and motivation.
Not releasing a stable version has external costs on many people (me
and my users at least).

Bye

.. _`[1]`:  http://ludovic.rousseau.free.fr/softwares/pcsc-lite/


