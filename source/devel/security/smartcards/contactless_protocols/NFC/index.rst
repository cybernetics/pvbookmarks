
.. index::
   pair: wireless protocol; NFC

.. _nfc_protocol:

==============================
Near Field Communication (NFC)
==============================

.. seealso::

   - https://secure.wikimedia.org/wikipedia/en/wiki/Near_field_communication

Near field communication, or NFC, is a set of short-range wireless technologies,
typically requiring a distance of 4cm or less. NFC operates at 13.56 MHz and at
rates ranging from 106 kbit/s to 848 kbit/s. NFC communication always involves
an initiator and a target: the initiator actively generates an RF field that
can power a passive target. This enables NFC targets to take very simple form
factors such as tags, stickers, key fobs, or cards that do not require batteries.

NFC peer-to-peer communication is also possible, where both devices are powered.


Security aspects
================

Although the communication range of NFC is limited to a few centimeters, NFC
alone does not ensure secure communications.

In 2006, Ernst Haselsteiner and Klemens Breitfuß described different possible
types of attacks, and detail how to leverage NFC's resistance to Man-in-the-middle
attacks to establish a specific key.[11]

Unfortunately, as this technique is not part of the ISO standard, NFC offers no
protection against eavesdropping and can be vulnerable to data modifications.

Applications may use higher-layer cryptographic protocols (e.g., SSL) to establish
a secure channel.



.. toctree::
   :maxdepth: 3

   nfc_and_qt

