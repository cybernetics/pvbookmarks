

.. index::
   pair: libccid; 1.4.7

.. _libccid_1.4.7:

=========================================================
Changes for libccid 1.4.7  22 June 2012, Ludovic Rousseau
=========================================================

.. seealso::

   - http://ludovicrousseau.blogspot.fr/2012/06/new-version-of-libccid-147.html
   - https://alioth.debian.org/frs/shownotes.php?release_id=1808



- Add support of:

   * ACS ACR101 ICC Reader
   * ACS CryptoMate64
   * Alcor Micro AU9522
   * Bit4id CKey4
   * Bit4id cryptokey
   * Bit4id iAM
   * Bit4id miniLector
   * Bit4id miniLector-s
   * CCB eSafeLD
   * Gemalto Ezio Shield Branch
   * KOBIL Systems IDToken
   * NXP PR533

- KOBIL Systems IDToken special cases:
   * Give more time (3 seconds instead of 2) to the reader to answer
   * Hack for the Kobil IDToken and Geman eID card* The German eID
     card is bogus and need to be powered off before a power on
   * Add Reader-Info-Commands special APDU/command:

     - Manufacturer command
     - Product name command
     - Firmware version command
     - Driver version command

- Use auto suspend for CCID devices only (Closes Alioth bug
  [#313445] "Do not activate USB suspend for composite devices:
  keyboard")
- Fix some error management in the T=1 TPDU state machine
- some minor bugs removed
- some minor improvements added
