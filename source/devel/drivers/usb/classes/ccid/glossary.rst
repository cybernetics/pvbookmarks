

.. index::
   pair: CCID; Glossary

.. _ccid_glossary:

=================================================
CCID Chip/Smart Card Interface Devices Glossary
=================================================


.. seealso::

   - :ref:`glossary_smartcard`

.. glossary::

   APDU Command Header
       The four byte sequence that begins an APDU; CLA INS P1 P2 (ISO/IEC 7816-4 § 5.3.1)

   CCID
       Chip/Smart Card Interface Devices.The USB CCID specification from the USB
       working group aims to normalize USB smartcard readers, in order to have
       a single driver (supplied once for all with the operating system) for
       virtually any reader from any manufacturer.


   Smart Card
       Any of a number of similar devices conforming to ISO/IEC 7816-3.


   T=0 Command Header
       The sequence of five bytes; CLA INS P1 P2 P3 [ISO/IEC 7816-3 § 8.3.2].

   WI
       Waiting time Integer for protocol T = 0

