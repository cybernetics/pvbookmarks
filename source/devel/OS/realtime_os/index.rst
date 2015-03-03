

.. index::
   pair: Real ; Time 
   ! Real Time
   ! Jitter


.. _real_time_operating_systems:

==============================
Real time Operating systems
==============================

.. seealso::

   - http://fr.wikipedia.org/wiki/Liste_des_syst%C3%A8mes_d%27exploitation_temps_r%C3%A9el

.. contents::
   :depth: 3

Définition française
====================


.. seealso::

   - http://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation_temps_r%C3%A9el

Un système d'exploitation temps réel, en anglais RTOS pour real-time 
operating system (prononcé Are-toss) est un système d'exploitation multitâche 
destiné aux applications temps réel. 

Ces applications comprennent les systèmes embarqués (thermostats programmables, 
contrôleurs électroménagers, téléphones mobiles), des robots industriels, 
les vaisseaux spatiaux, les systèmes de contrôle commande industriel, 
et le matériel de recherche scientifique.

Un RTOS facilite la création d'un système temps réel, mais ne garantit pas 
que le résultat final respecte les contraintes temps réel, ce qui exige le 
développement correct du logiciel. 

Un RTOS n'a pas nécessairement pour but d'être performant et rapide, mais 
un RTOS fournit des services et des primitives qui, si elles sont utilisées 
correctement, peuvent garantir les délais souhaités. 

Un RTOS utilise des ordonnanceurs spécialisées afin de fournir aux développeurs 
des systèmes temps réel les outils et les primitives nécessaires pour 
produire un comportement temps réel souhaité dans le système final.


Définition anglophone
======================

.. seealso::

   - http://en.wikipedia.org/wiki/Real-time_operating_system
   
A real-time operating system (RTOS) is an operating system (OS) intended 
to serve real-time application requests. 

**It must be able to process data as it comes in, typically without buffering 
delays**. 

Processing time requirements (including any OS delay) are measured in 
tenths of seconds or shorter.

A key characteristic of an RTOS is the level of its consistency concerning 
the amount of time it takes to accept and complete an application's task; 

**The variability is jitter**. 

A hard real-time operating system has less jitter than a soft real-time 
operating system. 

The chief design goal is not high throughput, but rather a guarantee of 
a soft or hard performance category. 

An RTOS that can usually or generally meet a deadline is a soft real-time 
OS, but if it can meet a deadline deterministically it is a hard real-time OS.

An RTOS has an advanced algorithm for scheduling. 
Scheduler flexibility enables a wider, computer-system orchestration of 
process priorities, but a real-time OS is more frequently dedicated to a 
narrow set of applications. 

Key factors in a real-time OS are minimal interrupt latency and minimal 
thread switching latency; a real-time OS is valued more for how quickly 
or how predictably it can respond than for the amount of work it can 
perform in a given period of time.


Définitions
===========
 
.. _jitter:
 
Jitter
------


.. seealso:: 

   - http://en.wikipedia.org/wiki/Jitter   
   - http://fr.wikipedia.org/wiki/Gigue_%28%C3%A9lectronique%29


Jitter is the undesired deviation from true periodicity of an assumed 
periodic signal in electronics and telecommunications, often in relation 
to a reference clock source. 

Jitter may be observed in characteristics such as the frequency of 
successive pulses, the signal amplitude, or phase of periodic signals. 

Jitter is a significant, and usually undesired, factor in the design of 
almost all communications links (e.g., USB, PCI-e, SATA, OC-48). 

In clock recovery applications it is called timing jitter


Open RTOS
==========

.. toctree::
   :maxdepth: 3
  
   free_rtos/index
   lepton/index
   linux_rt/index      
   rtems/index   
   xenomai/index

Closed RTOS
================

.. toctree::
   :maxdepth: 3
   
   closed_source/index
   
   



