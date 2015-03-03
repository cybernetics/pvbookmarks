

.. index::
   pair: bootloader; UEFI
   pair: bootloader; GPT (GUID partition table)


.. _UEFI:

=====================================
Unified Extensible Firmware Interface
=====================================

.. seealso::

   - https://secure.wikimedia.org/wikipedia/en/wiki/Unified_Extensible_Firmware_Interface
   - https://secure.wikimedia.org/wikipedia/fr/wiki/Extensible_Firmware_Interface


.. image:: 150px-Uefi_logo.svg.png


.. image:: 300px-Efi-simple.svg.png


Micrologiciel EFI à la place du BIOS
====================================

Sur certains PC actuels, c'est le micrologiciel EFI (et non pas le BIOS) qui est
utilisé pour lancer le chargeur d'amorçage : l'EFI lit la GPT du disque
(GUID Partition Table, voir (en) GPT) pour déterminer l'emplacement de la
routine d'amorçage.



The Unified Extensible Firmware Interface (UEFI) is a specification that defines
a software interface between an operating system and platform firmware. UEFI is
a more secure replacement for the older BIOS firmware interface, present in all
IBM PC-compatible personal computers, which is vulnerable to bootkit malware.[1][2]

The original EFI (Extensible Firmware Interface) specification was developed by
Intel. In 2005, development of the EFI specification ceased in favour of UEFI,
which had evolved from EFI 1.10. The UEFI specification is being developed by
the industry-wide organization Unified EFI Forum.

UEFI is not restricted to any specific processor architecture and can run on
top of, or instead of, older BIOS implementations


Grandes lignes
==============

Une des fonctions principales d'UEFI est l'amorçage d'un système d'exploitation.
Celui-ci se fait par l'intermédiaire d'un programme d'amorçage, qui est un cas
particulier d'application UEFI. Le secteur de démarrage du BIOS n'est plus utilisé.

UEFI gère pour les disques, outre le partitionnement classique par MBR
(limité à 2,2 To), un nouveau système de partitionnement nommé GPT (globally
unique identifier partition table). Le GPT permet 128 partitions principales sur
un support de capacité allant jusqu'à 9.4 Zo (milliards de téraoctets).

UEFI permet ainsi le démarrage sur des disques de 2,2 To et plus.

L'UEFI permet également :

- grâce à une pile de protocoles réseau, les mises à jour automatique du
  micrologiciel depuis le site du constructeur, à la manière des mises à jour d'OS ;
- grâce à la gestion bas niveau des disques, le clonage de disques sans passer
  par l'OS, ce qui facilite les copies de disques hébergeant plusieurs
  systèmes d'exploitation.
