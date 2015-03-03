
.. index::
   pair: Windows explorer; hash

.. _hashtab_windows:

=========================
Hashtab windows
=========================

.. seealso:: http://implbits.com/HashTab/HashTabWindows.aspx


Introduction
============

.. seealso:: http://ohax.fr/verifier-facilement-sous-windows-un-checksum-md5-crc32-sha-1

Contrôler un checksum MD5 est souvent utile pour vérifier qu’un transfert de
fichier ou un téléchargement n’a pas été altéré ou modifié.

Pour calculer ces hachages, il existe des logiciels plus ou moins pratiques à
utiliser, le plus simple d’entre eux est certainement Hashtab Windows Shell Extension !

Ce qui est vraiment pratique avec ce freeware, c’est qu’il vous ajoute un nouvel
onglet dans la page « Propriétés », accessible via un simple clic droit sur un fichier.


Once you have installed HashTab, just right click on any file.

On Windows, select  Properties and you will see a new "File Hashes" tab.
"File Hashes" displays all the configured hashes for the file.

You can customize which hashes are calculated and displayed. You can hash other
files for comparison. You can also paste in hash text so you don't go cross-eyed
trying to compare hashes.

HashTab supports the following hash functions: Adler32, CRC32, MD2, MD4, MD5,
RIPEMD(128,256,320), SHA-1,256,384,512, Tiger, and Whirlpool.

NOTE: If you do not see any hashes in the File Hashes dialog, click Settings and
make sure that at least one hash algorithm is selected to display
