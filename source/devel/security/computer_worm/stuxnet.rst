

.. index::
   ! stuxnet

.. _stuxnet_worm:

==============
stuxnet worm
==============

.. seealso::

   - https://secure.wikimedia.org/wikipedia/en/wiki/Stuxnet
   - https://secure.wikimedia.org/wikipedia/fr/wiki/Stuxnet
   - http://owni.fr/2011/06/20/video-stuxnet-en-trois-minutes-chrono/

.. contents::
   :depth: 3

Introduction
============

Stuxnet is a Windows computer worm discovered in July 2010 that targets industrial
software and equipment. While it is not the first time that hackers have
targeted industrial systems, it is the first discovered `malware`_ that spies on
and subverts industrial systems,and the first to include a programmable
logic controller (PLC) `rootkit`_.

The worm initially spreads indiscriminately, but includes a highly specialized
malware payload that is designed to target only Siemens `Supervisory Control And Data Acquisition (SCADA)`_
systems that are configured to control and monitor specific industrial processes.

Stuxnet infects PLCs by subverting the `Step-7`_ software application that is used
to reprogram these devices

.. _`malware`: https://secure.wikimedia.org/wikipedia/en/wiki/Malware
.. _`rootkit`: https://secure.wikimedia.org/wikipedia/en/wiki/Rootkit
.. _`Supervisory Control And Data Acquisition (SCADA)`: https://secure.wikimedia.org/wikipedia/en/wiki/SCADA
.. _`Step-7`:  https://secure.wikimedia.org/wikipedia/en/wiki/WinCC



