

.. index::
   pair: Processors; ARM 

.. _ARM_processors:

==================
ARM Processors
==================


.. seealso::

   - http://fr.wikipedia.org/wiki/Architecture_ARM



Introduction
============

Les architectures ARM, développées par ARM Ltd, sont des architectures 
RISC 32 bits.

Dotés d'une architecture relativement plus simple que d'autres familles 
de processeurs, et bénéficiant d'une faible consommation, les processeurs 
ARM sont devenus dominants dans le domaine de l'informatique embarquée, 
en particulier la téléphonie mobile et les tablettes.

Ces processeurs sont fabriqués sous licence par un grand nombre de 
constructeurs.

ARM is one of the most popular architectures used in embedded Linux systems.

ARM designs CPU cores (instruction sets, caches, MMU, etc.) and sells the design
to licensees

The licensees are founders (Texas Instruments, Freescale, ST Ericsson, 
Atmel, etc.), they integrate an ARM core with many peripherals, into a 
chip called a SoC, for System-on-chip

Each founder provides different models of SoC, with different combination 
of peripherals, power, power consumption, etc.

The concept of SoC allows to reduce the number of peripherals needed on 
the board, and therefore the cost of designing and building the board.

**Linux supports SoCs from most vendors, but not all, and not with the 
same level of functionality.**


Cortex-M
========

.. toctree::
   :maxdepth: 3
   
   cortex_m/index
  
