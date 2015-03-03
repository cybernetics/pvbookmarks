

.. index::
   pair: libpcsclite ; version 1.7.3

.. _libpcsclite_1.7.3:

=================
libpcsclite 1.7.3
=================

.. seealso:: http://ludovicrousseau.blogspot.com/2011/06/new-version-of-pcsc-lite-173.html

Changelog
=========

I just released new version of `pcsc-lite 1.7.3`_.


- COPYING: Add my name as copyright holder
- hotplug libudev: support libudev >= 171
- hotplug libusb: Fix a memory leak
- pcscd: exit immediately in case of SIGTERM
  Closes Debian bug #620305 "pcscd slows down shutdown/restart"
- Send logs to stdout instead of stderr
  It is now possible to use tee(1) to redirect logs in a file without first
  redirecting stderr to stdout
- Add command line option -T, --color: force use of colored logs
  The idea is to have colored logs even if they are redirected to a file or a pipe.
- Define g_rgSCardT?Pci as const structures to be more Windows like
  I do not expect a regression or compilation problem in WinSCard API users but how knows...
- log at level PCSC_LOG_DEBUG instead of PCSC_LOG_ERROR to avoid filling the system log file
- Remove the deprecated define FEATURE_MCT_READERDIRECT (replaced by
  FEATURE_MCT_READER_DIRECT)
- better Hurd support


some other minor improvements and bug corrections


.. _`pcsc-lite 1.7.3`:  https://alioth.debian.org/frs/?group_id=30105&release_id=1693#pcsclite-pcsc-lite-1.7.3-title-content



















