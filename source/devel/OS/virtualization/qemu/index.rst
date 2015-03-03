


.. index::
   pair: Virtualization ; QEMU
   pair: Fabrice ; Bellard
   ! QEMU


.. _qemu:

=================================
QEMU (short for "Quick EMUlator")
=================================

.. seealso::

   - http://fr.wikipedia.org/wiki/Qemu
   - http://wiki.qemu.org/Main_Page
   - http://git.qemu.org/qemu.git
   - http://en.wikipedia.org/wiki/Fabrice_Bellard


.. contents::
   :depth: 3

Introduction
=============

QEMU est un logiciel libre d'émulation de processeur et de machine 
virtuelle permettant d'exécuter un ou plusieurs systèmes d'exploitation 
via les hyperviseurs KVM et Xen, ou seulement des binaires, dans 
l'environnement d'un système d'exploitation déjà installé sur la machine.

Main Page
==========

.. seealso:: see http://wiki.qemu.org/Main_Page

QEMU is a generic and open source machine emulator and virtualizer.

When used as a machine emulator, QEMU can run OSes and programs made for 
one machine (e.g. an ARM board) on a different machine (e.g. your own PC). 
By using dynamic translation, it achieves very good performance.

When used as a virtualizer, QEMU achieves near native performances by 
executing the guest code directly on the host CPU. 
QEMU supports virtualization when executing under the Xen hypervisor or 
using the KVM kernel module in Linux. 
When using KVM, QEMU can virtualize x86, server and embedded PowerPC, 
and S390 guests


Qemu source code
================


QEMU is developed using git. The main tree is located at http://git.qemu.org/qemu.git. 

The latest development happens on the master branch. The stable tree is 
located in a stable-0.XX' branch where '0.XX' is the minor release version.

To download the latest development tree, use the following command::

    git clone git://git.qemu-project.org/qemu.git
    
    


