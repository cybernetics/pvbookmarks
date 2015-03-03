
.. index::
   pair: Smartcard; ATR
   pair: Smartcard; Raw mode
   pair: Smartcard; Mode transparent
   pair: Smartcard; PCSC
   pair: Smartcard; CCID
   pair: Smartcard; glossary

.. _glossary_smartcard:

==================
Smartcard Glossary
==================

.. seealso::

   - :ref:`glossary_devel`
   - :ref:`ccid_glossary`


.. seealso::  http://www.smartcardalliance.org/pages/smart-cards-intro-glossary


.. glossary::


    AFI
        Application Family Identifier (see Parameters description: Type B AFI).


    APDU
        Application Protocol Data Unit.

    APDU Command Header
        The four byte sequence that begins an APDU; CLA INS P1 P2 (ISO/IEC 7816-4 § 5.3.1)

    ATR
        Answer To Reset. The first response of a card inserted in a smartcard reader is called the ATR (Answer To Reset).
        The main goal for the ATR is to describe the communication parameters supported to establish a dialogue with the
        smartcard reader. The ATR is a series of bytes standardized by the ISO7816-3 standard.
        The first bytes describe the conventions of communication with the card, the available interfaces and their parameters.
        These bytes are followed by a series of bytes called "historical bytes", for which no standard exists and which are
        used to transmit information such as the type of card, the embedded software or the status of the card.
        Finally, these historical bytes may be followed by a byte verification, cheksum of the previous bytes.

    ATTRIB
        :term:`PICC` selection command


    Carier
        Carrier: Base signal (e.g. 13.56Mhz).
        Reader modifies this signal to send data.

        .. seealso::  :term:`Subcarrier`


    CCID
        Chip/Smart Card Interface Devices. The USB CCID specification from
        the USB working group aims to normalize USB smartcard readers, in
        order to have a single driver (supplied once for all with the
        operating system) for virtually any reader from any manufacturer.

        .. seealso::

           - http://www.usb.org/developers/defined_class/
           - http://www.usb.org/developers/defined_class/#BaseClass0Bh


    CID
        (smart)card identifier.

    CRC
        Cyclic Redundancy check

    CSC
        A Country Signing Certificate (CSC) is needed to verify the authenticity of the Document Signing Certificate (DSC).
        Some countries have made their CSC publicly available. The list below contains those CSCs that we could find
        with Google. The list has links to government Web and LDAP servers where we found the certificates.
        (But please, don't trust us, go to your government's server and download the certificate yourself!)
        see http://jmrtd.org/csca.shtml

    DFU
        Device Firmware Upgrade. A standard protocol for downloading (and optionally uploading)
        firmware images to/from USB devices.
        The specification is available from the USB Forum at http://www.usb.org/developers/devclass_docs/usbdfu10.pdf

        .. seealso::

           - http://www.openpcd.org/DFU
           - http://www.openpcd.org/Sam7dfu

    DSFID
        Data Storage Format IDentifier

    EOF
        End of frame

    ePassport
        A travel document that contains an integrated circuit chip based on international standard ISO/IEC 14443 and
        that can securely store and communicate the ePassport holder’s personal information to authorized reading
        devices.

    GNU/Linux
        .. seealso:: http://en.wikipedia.org/wiki/Linux

        GNU/Linux is a generic term referring to Unix-like  computer operating
        systems based on the Linux kernel. Their development is one of the most
        prominent examples of free and open source software collaboration;
        typically all the underlying source code can be used, freely modified,
        and redistributed, both commercially and non-commercially, by anyone
        under licenses such as the GNU General Public License.
        The name "Linux" comes from the Linux kernel, originally written in 1991
        by Linus Torvalds.

        .. note:: The contribution of a supporting Userland in the form
           of system tools and libraries from the GNU Project (announced in 1983 by
           Richard Stallman) is the **basis for the Free Software Foundation's preferred
           name GNU/Linux**)


        Supported platforms: IA-32, MIPS, x86-64, SPARC, DEC Alpha, Itanium,
        PowerPC, ARM, m68k, PA-RISC, s390, SuperH, M32R and more
        Latest stable release Kernel 2.6.32.8


    High frequency (HF)
        Radio frequencies (RF) in the range of 3 MHz to 30 MHz. When used in an RF-based
        identification system, the high frequency used is typically 13.56 MHz.
        International Civil Aviation Organization (ICAO) MRTD


    International Civil Aviation Organization (ICAO) MRTD
        International Civil Aviation Organization Machine Readable Travel Documents. ICAO establishes international
        standards for travel documents. An MRTD is an international travel document (e.g., a passport or visa)
        containing eye- and machine-readable data. ICAO Document 9303 is the international standard for MRTDs.


    ICC
        Integrated circuit card. ICC typically refers to a plastic (or other material)
        card containing an integrated circuit which is compatible to ISO/IEC 7816.

    Identity document
        A piece of documentation designed to verify aspects of a person’s identity. (See also breeder document.)

    ISO/IEC 14443
        ISO14443 is a series of international, vendor-independent standards for
        proximity RFID.
        It operates on 13.56MHz and uses magnetic coupling between the reader
        (:term:`PCD`) and transponder (:term:`PICC`).

        .. seealso::

           - http://www.iso.ch/
           - http://www.waazaa.org/14443/
           - http://www.openpcd.org/ISO14443
           - https://secure.wikimedia.org/wikipedia/en/wiki/ISO/IEC_14443
           - :ref:`iso_iec_14443_protocol`

        ISO/IEC 14443 consists of four parts and describes two types
        of cards: Type A and Type B, both of which communicate via radio at 13.56 MHz.
        The main differences between these types concern modulation methods,
        coding schemes (Part 2) and protocol initialization procedures (Part 3).
        Both Type A and Type B cards use the same transmission protocol described
        in Part 4. The transmission protocol specifies data block exchange and
        related mechanisms:

            1. data block chaining
            2. waiting time extension
            3. multi-activation

        An attempt was made to include additional legacy systems as appendixes
        – Type C (Sony/Japan), Type D (OTI/Israel), Type E (Cubic/USA), and
        Type F (Legic/Switzerland) and Type G (China) – but they were not finally
        accepted as ISO-standard.

        ISO 14443 is supported by most contactless smart card providers to one
        level or another and is usually specified in the different RFP’s who are
        looking for contactless smart cards. VISA and MasterCard have both announced
        that they are supporting ISO14443 in their relevant contactless specifications.

    ISO/IEC 14443 Type B
        The standard of contactless Smart card developed by Motorola. It is used
        in the Basic Resident Register Card.
        Type-B cards are mainly used in France and francophone countries.

    ISO/IEC 14443 Type A
        Mifare versus ISO 14443
        MIFARE and ISO 14443 Type A are not the same. While MIFARE is often viewed
        as equivalent to or subset of ISO 14443 Type A, it is a proprietary
        encryption/conditional access protocol owned and licensed by Philips
        Semiconductors to multiple vendors of card ICs and reader ICs.
        All MIFARE readers must make use of a Philips special chip that handles
        these special security features.
        Because MIFARE has been so predominantly used with products employing
        ISO 14443 Type A technology, it has mistakenly become synonymous with the
        standard. However ISO 14443 Type A is an open standard and does not require
        the use of this MIFARE encryption/conditional access scheme.


    ISO 14443-4
        This part describes an optional transport layer protocol.
        This protocol is often also referred-to as "T=CL".
        This is a name derived from the commonly-used contact based smart card
        protocols T=0 and T=1. "CL" means "contact less".

    ISO/IEC 15693
        ISO15693 is a series of international, vendor-independent standards for
        vicinity RFID.

        It operates on 13.56MHz and uses magnetic coupling between the reader
        (VCD) and transponder (VICC).

        .. seealso::

           - http://www.openpcd.org/ISO15693
           - http://www.waazaa.org/15693/
           - https://secure.wikimedia.org/wikipedia/en/wiki/ISO/IEC_15693


    KibiByte
        see http://en.wikipedia.org/wiki/Binary_prefix#Specific_units_of_IEC_60027-2_A.2
        http://en.wikipedia.org/wiki/Timeline_of_binary_prefixes


    Mifare classic
        This is a proprietary Philips protocol which runs on top of 14443-1,2,3
        (Type A). It does not implement 14443-4. Since Mifare Classic includes
        some proprietary CRYPTO1 algorithm, you can only do Mifare if you have
        a Philips reader ASIC (such as the RC632).

    NAD
        node address (NAD) used in :term:`ISO/IEC 14443`


    OpenPCD
        OpenPCD is a free hardware design for Proximity Coupling Devices (PCD)
        based on 13,56MHz communication. This device is able to screen
        informations from Proximity Integrated Circuit Cards (PICC) conforming
        to vendor-independent standards such as ISO 14443, ISO 15693 as well as
        proprietary protocols such as Mifare Classic. Contactless cards like
        these are for example used in the new electronic passports.

        .. seealso:: http://www.openpcd.org/


    PCSC
    PC/SC
        Personal Computer/Smart Card. The PC/SC specification defines how to
        integrate smart card readers and smart cards with the computing environment
        and how to allow multiple applications to share smart card devices

    PCSC Lite
        Personal Computer/Smart Card Lite. PCSC Lite is open source software that
        implements the PC/SC specification for Linux.

        .. seealso:: :ref:`libpcsclite`

    PCD
        Proximity Coupling Device: it refers to the smartcard reader (reader).

        .. seealso::

           - :term:`VCD`
           - http://www.openpcd.org/


    PICC
        Proximity Integrated Circuit Card (:term:`ICC`): it refers to the card
        (smartcard, memory card, ...)
        Also known as ``tag``.

    PPS
        Protocol Parameter Selection

        .. seealso::

           - :term:`ISO/IEC 14443`

    PKCS#11
        XXX

    Proximity cards:
        A generic name for contactless integrated circuit devices typically used for security access or payment systems.
        It can refer to 125 kHz RFID devices or 13.56 MHz contactless smart cards. (See ISO/IEC 14443.).


    Raw mode
        En français: mode transparent.


    Reader
        Any device that communicates information or assists in communications from a card, token or other identity
        document and transmits the information to a host system, such as a control panel/processor or database for
        further action.


    RC632
        The RC632 is a multi-protocol 13.56MHz RFID reader ASIC produced by
        Philips_/NXP.

        .. seealso::

           - http://www.openpcd.org/RC632
           - http://www.nxp.com/documents/data_sheet/CLRC632.pdf

        .. _Philips: http://semiconductor.philips.com/

    RFU
        Reserved for Future Use

    Smart card
        A device that includes an embedded integrated circuit that can be either a secure microcontroller or equivalent
        intelligence with internal memory or a memory chip alone. The card connects to a reader with direct physical
        contact or with a remote contactless radio frequency interface. With an embedded microcontroller, smart cards
        have the unique ability to store large amounts of data, carry out their own on-card functions (e.g., encryption
        and mutual authentication) and interact intelligently with a smart card reader. Smart card technology conforms
        to international standards (ISO/IEC 7816 and ISO/IEC 14443) and is available in a variety of form factors,
        including plastic cards, subscriber identification modules used in GSM mobile phones, and USB-based tokens.

    SOF
        Start of Frame

    Subcarrier
        Signal on top of the base signal.
        Tag generates this signal to send data.

        .. seealso:: :term:`carier`


    Type A card
        Type A smartcard = ISO1443A.

    UID
        Unique Identifier (UID): All ISO-compliant smart cards are provided with a UID number. For interoperability
        purposes, a card’s UID is open and available to be read by all compliant readers. Since this unique number is
        not secured by keys, reading the UID of a smart card is comparable to reading a proximity card, mag stripe card
        or other technology that utilizes open, unsecured numbers.

    USB
        Universal Serial Bus. A serial bus standard to interface devices.

    VCD
        Vicinity Coupling Device

        .. seealso:: :term:`PCD`

    VICC
        Vicinity Integrated Circuit Card

        .. seealso::  :term:`PICC`

