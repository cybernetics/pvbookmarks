



.. _linux_kernel_3_8_0:

======================================================
linux  kernel 3.8.0  (Mon, 18 Feb 2013 16:28:03 -0800)
======================================================

.. seealso::

   - https://lkml.org/lkml/2013/2/18/476
   - http://kernelnewbies.org/Linux_3.8
   - http://linuxfr.org/news/sortie-du-noyau-linux-3-8


.. contents::
   :depth: 3


Summary
========

This Linux release includes support in Ext4 for embedding very small files in
the inode, which greatly improves the performance for these files and saves some
disk space.

There is also a new Btrfs feature that allows to replace quickly a disk, a new
filesystem F2FS optimized for SSDs, support of filesystem mounts, UTS, IPC, PIDs,
and network stack namespaces for unprivileged users, accounting of kernel memory
in the memory resource controller, journal checksums in XFS, an improved NUMA
policy redesign and, of course, the removal of support for 386 processors.

Many small features and new drivers and fixes are also available.



Linux fr
========

.. seealso:: https://plus.google.com/u/0/111104121194250082892/posts/KW3TdRYwjr9

À noter, une nouvelle survenue pendant le développement de cette version, dont
l'incidence sur les développements futurs reste inconnue : Alan Cox, qui a été
employé successivement par Red Hat et Intel, a décidé de quitter Intel et le
développement du noyau (dont il est un des piliers) pour raisons familiales.
