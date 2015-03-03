
.. index::
   pair: Firmware; BSP (Board Support Package)
   pair: Système embarqué; BSP (Board Support Package)


.. _board_support_package:

======================
Board Support Package
======================


.. seealso::
 
   - http://fr.wikipedia.org/wiki/Board_Support_Package
   - http://en.wikipedia.org/wiki/Board_support_package
   - :ref:`thomas_petazzoni`
   - :ref:`linux_embedded_bootloaders`
  
   
.. contents::
   :depth: 3
   

Intro (français)
=================      
   
Un Board Support Package ou BSP est un logiciel bas niveau de support de 
cartes-mères, c'est-à-dire entre l'OS et la carte mère, dans le domaine de 
l'informatique embarquée.

Par exemple, Linaro construit le BSP pour les processeurs ARM. 

SHAI sera l'interface standardisée entre le système d'exploitation symbian, et 
les BSP supportant différents matériels.


Intro (anglais)
=================  

In embedded systems, a board support package (BSP) is implementation specific 
support code for a given (device motherboard) board that conforms to a given 
operating system. 

It is commonly built with a bootloader that contains the minimal device support 
to load the operating system and device drivers for all the devices on the board.

Some suppliers also provide a root file system, a toolchain for making programs 
to run on the embedded system (which would be part of the architecture support 
package), and configurators for the devices (while running).

