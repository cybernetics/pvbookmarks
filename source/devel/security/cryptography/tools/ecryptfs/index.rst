
.. index::
   pair: Privacy;  Ecryptfs
   ! Ecryptfs


.. _ecryptfs:

===============================
Ecryptfs
===============================

.. seealso::

   - http://ecryptfs.org/
   - https://help.ubuntu.com/community/EncryptedPrivateDirectory
   - https://launchpad.net/ecryptfs
   - http://ecryptfs.org/about.html

.. figure:: ecryptfs_logo_final.png
   :align: center

.. figure:: ecryptfs_64b.png
   :align: center
   
.. contents::
   :depth: 3   
 
Introduction
============

eCryptfs is a POSIX-compliant enterprise cryptographic filesystem for Linux.

eCryptfs is a cryptographic stacked Linux filesystem. 

eCryptfs stores cryptographic metadata in the header of each file 
written, so that encrypted files can be copied between hosts; 
the file will be decrypted with the proper key in the Linux kernel keyring. 

There is no need to keep track of any additional information aside from 
what is already in the encrypted file itself. 
You may think of eCryptfs as a sort of "gnupgfs", or "gnupg as a filesystem".

eCryptfs is widely used, as the basis for Ubuntu's Encrypted Home 
Directory, natively within Google's ChromeOS, and transparently embedded 
in several network attached storage (NAS) devices.

Originally authored by Michael Halcrow and the IBM LInux Technology Center, 
eCryptfs is derived from Erez Zadok's Cryptfs, and the FiST framework 
for stacked filesystems. 

eCryptfs extends Cryptfs to provide advanced key management and policy 
features. 

eCryptfs is currently actively maintained by Dustin Kirkland 
(of Gazzang, , Inc) and Tyler Hicks (of Canonical, Ltd).
 

Annoucements
============

.. seealso::

   - https://slo-tech.com/clanki/10008en/ (Interview with Dustin Kirkland, Ubuntu Core Developer about encryption in Ubuntu, 28. jan 2010)

::

    If the administrator changes the user's password (without entering 
    the user's previous password), they will break the user's automatic 
    mounting of their home directory.

    In this case, the user will need to login, and immediately re-wrap 
    their wrapped-passphrase. They can use the eCryptfs utilities 
    ecryptfs-rewrap-passphrase or ecryptfs-wrap-passphrase to do this. 
    Admittedly this is inconvenient, but hopefully a corner case.


Blog
====

.. seealso::

   - http://blog.dustinkirkland.com/search/label/ecryptfs


Source code
===========

.. seealso::

   - http://ecryptfs.org/source.html

ecryptfs kernel code
--------------------

The ecryptfs kernel code is stored in Git/Kernel.org, and can be 
obtained with::

- https://git.kernel.org/?p=linux/kernel/git/tyhicks/ecryptfs.git;a=summary

or obtain the latest source with::

    git clone git://git.kernel.org/pub/scm/linux/kernel/git/tyhicks/ecryptfs.git


ecryptfs-utils userspace code
------------------------------
 
The ecryptfs-utils userspace code is stored in Launchpad/Bazaar, and can 
be obtained with:

- https://code.launchpad.net/~ecryptfs/ecryptfs/trunk   

or obtain the latest source with::

    bzr branch lp:ecryptfs

Officially released, signed archives and changelogs of the source are 
available at: https://launchpad.net/ecryptfs/+download

The Google+ page is
====================

- https://plus.google.com/103860974668504356550



The mailing list for users and developers is
=============================================


- http://vger.kernel.org/vger-lists.html#ecryptfs
- http://dir.gmane.org/gmane.comp.file-systems.ecryptfs.general


How to decrypt
===============

.. toctree::
   :maxdepth: 3
   
   decrypt/index


Tutorials
=========


.. seealso::

   - http://bodhizazen.net/Tutorials/Ecryptfs/
   
   

