
.. index::
   pair: U-boot; versions

==========================
U-Boot  versions
==========================

.. seealso::

   - http://www.denx.de/wiki/U-Boot/ReleaseCycle




Like with many other things, U-Boot development follows the Linux model of a
release cycle. That means:

- We will have U-Boot releases at a fixed interval.
- The release interval shall be (approximately) 3 months.
- Immediately following each release, there will be a "merge window" of normally
  2 weeks. While this merge window is open, new features can be added to the
  U-Boot source tree. Linus Torvalds explains here and there what the term
  "merge window" is supposed to mean.
- After the merge window closes, no new features may be added to allow for a
  release candidate phase which is intended to fix bugs and regressions.

.. warning:: even though we follow Linux ways in may respects, there are
  differences in the actual procedures, which are documented in section `Development Process`_.



.. _`Development Process`:  http://www.denx.de/wiki/U-Boot/DevelopmentProcess



Version Numbers
===============

Starting with the release in October 2008, the names of the releases were
changed from numerical release numbers without deeper meaning into a time
stamp based numbering.

Regular releases are now identified by names consisting of the calender year
and month of the release date.

Additional fields (if present) indicate release candidates or bug fix releases
in "stable" maintenance trees.

Examples::

    U-Boot v2009.11     - Release November 2009
    U-Boot v2009.11.1   - Release 1 in version November 2009 stable tree
    U-Boot v2010.09-rc1 - Release candiate 1 for September 2010 release



U-boot versions
===============


.. toctree::
   :maxdepth: 4

   v2011.09/index
