
.. index::
   pair: bootloader; GRUB


.. _grub:

==========================
GRUB
==========================


.. seealso::

   - http://www.gnu.org/software/grub/
   - http://fr.wikipedia.org/wiki/GRUB


.. figure:: grub.png

   *Logo GRUB*


GNU GRUB (acronyme signifiant en anglais « GRand Unified Bootloader ») est un
programme de multiboot, libre, au même titre que LILO (Linux loader), qui permet
de choisir au démarrage de son ordinateur entre plusieurs systèmes d'exploitation.

Ses avantages sont notamment la gestion d'autres systèmes que Linux et Windows
(utile pour Hurd, Solaris, FreeBSD et OpenBSD), la lecture de la configuration
au démarrage (pas besoin de réinstaller GRUB dans le secteur d'amorçage après
un changement de configuration, contrairement à LILO), une ligne de commande
permettant de changer la configuration au démarrage et surtout la reconnaissance
en natif de divers systèmes de fichiers existants. Il possède également une
sorte de langage de commande simple permettant de « rattraper » un amorçage qui
se serait mal passé, suite au mauvais adressage d'une partition, par exemple.

Grub doit être capable de reconnaître tous les systèmes de fichiers sur lesquels
il pourrait être amené à démarrer. Il est pour cette raison beaucoup plus
volumineux que LILO.



Introduction
============

GNU GRUB is a Multiboot boot loader. It was derived from GRUB, the GRand Unified
Bootloader, which was originally designed and implemented by Erich Stefan Boleyn.

Briefly, a boot loader is the first software program that runs when a computer
starts. It is responsible for loading and transferring control to the operating
system kernel software (such as the Hurd or Linux).

The kernel, in turn, initializes the rest of the operating system (e.g. GNU).


GRUB Development
================


GRUB 2 has replaced what was formerly known as GRUB (i.e. version 0.9x), which
has, in turn, become GRUB Legacy. Enhancements to GRUB are still being made,
but the current released versions are quite usable for normal operation.

GRUB Legacy is no longer being developed. For the differences between
GRUB Legacy and GRUB, see the Grub Legacy Documentation.



