.. module:: USB_host
    :synopsis: USB host
  

=============
Les hosts USB
=============

En USB 1.0 et 1.1, il existe 2 types de contrôleurs host:

- l'UHCI (Universal Host Controler Interface) développé par Intel 
  Universal Host Controller Interface (UHCI) was created by Intel 
  for USB 1.0 (full and low speeds). Far from being "universal", it is 
  actually proprietary and is incompatible with OHCI. Intel and VIA 
  controllers generally use UHCI, while other vendors use OHCI.
- l'OHCI (Open Host Controler Interface), un standard développé par
  Compaq, Microsoft et National Semiconductor
  Open Host Controller Interface, or OHCI, is an open standard.

Pour l'USB2.0 intervient également le contrôleur EHCI_ 
(Enhanced Host  Controler Interface)  

.. _EHCI: http://en.wikipedia.org/wiki/EHCI

Linux gère les 3 types de contrôleurs: les pilotes sont chargés 
automatiquement selon les besoins.


.. index::
   UHCI (Universal Host Controler Interface)
   OHCI (Open Host Controler Interface)
   EHCI (Enhanced Host  Controler Interface)
   http://en.wikipedia.org/wiki/EHCI

 
A host controller interface (HCI)
=================================

.. seealso::  http://en.wikipedia.org/wiki/EHCI


A host controller interface (HCI) is a register level interface  which 
allows a host controller for USB  or FireWire to communicate with the 
operating system of a personal computer.

On the expansion card or motherboard controller, this involves much 
custom logic, with digital logic engines in FPGAs plus analog circuitry 
managing the high speed differential signals. 
On the software side, it requires a device driver (called a Host Controller 
Driver, or HCD).


.. index::
   usbcore
   
