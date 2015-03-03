.. module:: 14443
    :synopsis: 14443 annexes


.. index::
   pair: smartcard protocol; 14443


.. _iso_iec_14443_protocol:

======================
ISO/IEC 14443 protocol
======================

.. seealso::

   - http://www.waazaa.org/14443/
   - http://en.wikipedia.org/wiki/ISO_14443


.. contents::
   :depth: 3


Introduction
============

ISO 14443 is an international standard for « Proximty Cards », i.e. contactless
cards operating at the 13.56 MHz frequency, with a maximum operating distance
of 10 centimetres.

The International Organization for Standardization, or ISO, issued its ISO 14443
standards in 2008 to harmonize the use of proximity or contactless smart cards
and their communication protocol. Contactless cards can retrieve the identity of
a person from a distance.

The speed and convenience of using contactless smart cards has opened the doors
to a large amount of applications, such as transactions with banks, mass transit
or gas stations.

The 14443 guidelines promote good design and business practices to ensure that
the smart card performs as expected, is highly reliable and works with many
different technology platforms.

Scope
=====

ISO 14443 specifically addresses the physical and programming aspects of contactless
cards.

**These new devices do not make contact with a card reader**.

They contain a wireless communications system that transmits identification
information in proximity to a reader. These smart devices store 64 kilobytes of
information and contain strong security features.

Most contact cards, such as credit cards, will eventually migrate to the contactless
technology to gain access to greater data storage, better encryption and less
wear and tear.


First Application
=================

ISO 14443 has been tested and applied to passenger identification in transportation
systems in Asia and Europe. For instance, South Korea implemented it in its T-money
system that facilitates payment in buses, on the subway or with taxis.

Similarly, Hong Kong leveraged the guidance of the standards when it launched
its Octopus card for transportation payments.

Requirements
============

ISO 14443 represents four sets of standards that cover the physical card requirements,
the radio frequency power and signal spectrum interferences, initialization aspects
and anticollision and finally communications protocols.

In addition, ISO 14443 comes in two flavors:

- Type A represents most contactless card applications.
- Type B is reserved for banking systems that carry larger amount of data.

Specifications
==============

ISO 14443 specifies the thickness---0.03 inches, or 0.84 mm---and the size of
the card, which is about the size of a credit card.
The radio frequency required is 13.56 megahertz and must provide a read range
of 4 inches, or 10 centimeters.

The speed of communications must operate at 106 kilobits per second.
Anticollision methods must be implemented to manage the read of multiple cards passing an area all at the same time, such as in mass transit transportation. ISO 1443 describes the various options for the language of communication and the protocol instructions that must be implemented.

Exclusions
==========

The standards do not cover the reading system and operating system embedded in
the cards.
These belong to each vendor who has proprietary rights to them.
However, ISO 1443 paints the characteristics of an "envelope protocol" to guarantee
an error-free communication.




Openpcd, 14443
==============

.. seealso:: http://www.openpcd.org/ISO14443


Other parts
=============

.. toctree::
   :maxdepth: 2

   anticollision
   faq






