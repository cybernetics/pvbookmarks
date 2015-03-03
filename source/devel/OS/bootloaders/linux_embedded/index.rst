
.. index::
   pair: bootloaders; embedded linux


.. _linux_embedded_bootloaders:

==========================
Linux embedded bootloaders
==========================



The role of the bootloader is to initialize some basic hardware peripherals,
load the Linux kernel image and run it.

The boot process of most recent embedded processors is the following:

1. The processor **executes code in ROM**, to load a first-stage bootloader from
   NAND, SPI flash, serial port or SD card
2. The **first stage bootloader** initializes the memory controller and a few other
   peripherals, and loads a second stage bootloader. No interaction is possible
   with this first stage bootloader, and it is typically provided by the CPU vendor.
3. The **second stage bootloader** offers more features: usually a shell, with
   commands. It allows to manipulate the storage devices, the network, configure
   the boot process, etc. This bootloader is typically generic and open-source.



Open-source bootloaders
========================


.. toctree::
   :maxdepth: 4

   u_boot/index
   barebox/index
