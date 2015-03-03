

.. index::
   pair: Patch; Management
   ! Patch


.. _patch_management:


====================
Git, mercurial, DVCS
====================


.. contents::
   :depth: 3

patch management
================

**Patchutils** is a small collection of programs that operate on patch files.
  Interdiff generates an incremental patch from two patches against a common source.
  For example, if you have applied a pre-patch to a source tree, and wish to apply
  another pre-patch (which is against the same original source tree), you can use
  interdiff to generate the patch that you need to apply. You can also use this to
  review changes between two pre-patches.

**combinediff** generates a single patch from two incremental patches, allowing
  you to merge patches together. The resulting patch file only alters each file once.

**filterdiff** will select the portions of a patch file that apply to files
  matching (or, alternatively, not matching) a shell wildcard.

**Fixcvsdiff** is for correcting the output of ‘cvs diff’.

**rediff** corrects hand-edited patches, by comparing the original patch with
  the modified one and adjusting the offsets and counts.

**lsdiff** displays a short listing of affected files in a patch file, along
  with (optionally) the line numbers of the start of each patch.

**splitdiff** separates out patches from a patch file so that each new patch file
  only alters any given file once. In this way, a file containing several incremental
  patches can be split into individual incremental patches.


**Recountdiff** fixes up counts and offsets in a unified diff.

**Unwrapdiff** fixes word-wrapped unified diffs.

::

     /usr/bin/install -c -m 644 './doc/interdiff.1' '/opt/patchutils/0.3.1/share/man/man1/interdiff.1'
     /usr/bin/install -c -m 644 './doc/filterdiff.1' '/opt/patchutils/0.3.1/share/man/man1/filterdiff.1'
     /usr/bin/install -c -m 644 './doc/fixcvsdiff.1' '/opt/patchutils/0.3.1/share/man/man1/fixcvsdiff.1'
     /usr/bin/install -c -m 644 './doc/rediff.1' '/opt/patchutils/0.3.1/share/man/man1/rediff.1'
     /usr/bin/install -c -m 644 './doc/editdiff.1' '/opt/patchutils/0.3.1/share/man/man1/editdiff.1'
     /usr/bin/install -c -m 644 './doc/combinediff.1' '/opt/patchutils/0.3.1/share/man/man1/combinediff.1'
     /usr/bin/install -c -m 644 './doc/lsdiff.1' '/opt/patchutils/0.3.1/share/man/man1/lsdiff.1'
     /usr/bin/install -c -m 644 './doc/splitdiff.1' '/opt/patchutils/0.3.1/share/man/man1/splitdiff.1'
     /usr/bin/install -c -m 644 './doc/grepdiff.1' '/opt/patchutils/0.3.1/share/man/man1/grepdiff.1'
     /usr/bin/install -c -m 644 './doc/recountdiff.1' '/opt/patchutils/0.3.1/share/man/man1/recountdiff.1'
     /usr/bin/install -c -m 644 './doc/unwrapdiff.1' '/opt/patchutils/0.3.1/share/man/man1/unwrapdiff.1'
     /usr/bin/install -c -m 644 './doc/dehtmldiff.1' '/opt/patchutils/0.3.1/share/man/man1/dehtmldiff.1'
     /usr/bin/install -c -m 644 './doc/flipdiff.1' '/opt/patchutils/0.3.1/share/man/man1/flipdiff.1'
     /usr/bin/install -c -m 644 './doc/espdiff.1' '/opt/patchutils/0.3.1/share/man/man1/espdiff.1'

    [root@houx bin]# ll
    total 348
    lrwxrwxrwx 1 root root      9 jan  6 16:23 combinediff -> interdiff
    -rwxr-xr-x 1 root root   1351 jan  6 16:23 dehtmldiff
    -rwxr-xr-x 1 root root   1952 jan  6 16:23 editdiff
    -rwxr-xr-x 1 root root   1563 jan  6 16:23 espdiff
    -rwxr-xr-x 1 root root  97741 jan  6 16:23 filterdiff
    -rwxr-xr-x 1 root root   1870 jan  6 16:23 fixcvsdiff
    lrwxrwxrwx 1 root root      9 jan  6 16:23 flipdiff -> interdiff
    lrwxrwxrwx 1 root root     10 jan  6 16:23 grepdiff -> filterdiff
    -rwxr-xr-x 1 root root 111375 jan  6 16:23 interdiff
    lrwxrwxrwx 1 root root     10 jan  6 16:23 lsdiff -> filterdiff
    -rwxr-xr-x 1 root root   3436 jan  6 16:23 recountdiff
    -rwxr-xr-x 1 root root  95762 jan  6 16:23 rediff
    -rwxr-xr-x 1 root root   3032 jan  6 16:23 splitdiff
    -rwxr-xr-x 1 root root   5940 jan  6 16:23 unwrapdiff


Where is it ?
-------------

Released tarballs (as well as pre-test releases) are here_.
For discussion about patchutils, try the patchutils mailing list.
To subscribe to this list, which is very low traffic, send a message
to: <patchutils-list-subscribe@sources.redhat.com>.

The git repository is available to view at fedorahosted.org:

::

    git clone git://git.fedorahosted.org/git/patchutils.git


.. _here: http://cyberelk.net/tim/data/patchutils/stable


.. seealso::

   - http://cyberelk.net/tim/software/patchutils
   - http://savannah.nongnu.org/projects/quilt
   - http://mercurial.selenic.com/wiki/MqExtension#Using_Mercurial_Queues

PATH update
===========

::

    export PATH=/opt/patchutils/current/bin:$PATH









