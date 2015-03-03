

.. index::
   pair: CCID ; compliant reader
   pair: CCID ; sudo apt-cache search "PC/SC"


.. _ccid_compliant_reader:


===============================
GNU/Linux CCID compliant reader
===============================

.. seealso::

   - http://pcsclite.alioth.debian.org/ccid.html#CCID_compliant


.. contents::
   :depth: 3



How to become CCID compliant
============================

::

    Just get the source code of this driver and do:

     tar xzvf ccid-x.y.z.tar.gz
     cd ccid-x.y.z
     ./configure
     make
     sudo ./src/parse > output.txt

     and send me (ludovic.rousseau@free.fr) the generated output.txt file.

     If your reader is CCID compliant and you would like to add it to the list
     of readers I would also need:

     - The URL of a web page describing the reader. Typically the web page of
       the reader description on the manufacturer web site.
     - A picture of the reader. In general a picture is already available on
       the manufacturer web page described above.



sudo apt-cache search "PC/SC"
=============================


::

       patrick@vercors:~$ sudo apt-cache search "PC/SC"
       libpcsclite-dev - Middleware to access a smart card using PC/SC (development files)
       libpcsclite1 - Middleware to access a smart card using PC/SC(library)
       libacr38u - PC/SC driver for the ACR38U smart card reader
       libasedrive-serial - PC/SC driver for the Athena ASEDrive IIIe serial smart card reader
       libasedrive-usb - PC/SC driver for the Athena ASEDrive IIIe USB smart card reader
       libccid - PC/SC driver for USB CCID smart card readers
       libgcr410 - PC/SC driver for GemPlus GCR410 serial SmartCard interface
       libgempc410 - PC/SC driver for the GemPC 410, 412, 413 and 415 smart card readers
       libgempc430 - PC/SC driver for the GemPC 430, 432, 435 smart card readers
       libopenct1 - middleware framework for smart card terminals (libraries)
       libopenct1-dbg - middleware framework for smart card terminals (libraries)
       libopenct1-dev - headers and development libraries for libopenct1
       libpcsc-perl - Perl interface to the PC/SC smart card library
       libpcscada-dev - Ada bindings to PC/SC middleware (development)
       libpcscada0 - Ada bindings to PC/SC middleware
       openct - middleware framework for smart card terminals
       pcsc-tools - Some tools to use with smart cards and PC/SC
       pcscada-dbg - Ada bindings to PC/SC middleware (debug)
       pcscd - Middleware to access a smart card using PC/SC (daemon side)
       python-pyscard - Python wrapper above PC/SC API
       pcsc-omnikey - PC/SC driver for Omnikey Cardman Smartcard readers (binary-only)



sudo aptitude install libusb-dev
================================

.. seealso::

   - :ref:`libccid_installation_on_gnu_linux`
   - :ref:`libpcsclite_installation`


::

    patrick@vercors:~$ sudo aptitude install libusb-dev
    Lecture des listes de paquets... Fait
    Construction de l'arbre des dépendances
    Lecture des informations d'état... Fait
    Lecture de l'information d'état étendu
    Initialisation de l'état des paquets... Fait
    Les NOUVEAUX paquets suivants vont être installés : libusb-dev
    0 paquets mis à jour, 1 nouvellement installés, 0 à enlever et 0 non mis à jour.
    Il est nécessaire de télécharger 38,8ko d'archives. Après dépaquetage, 344ko
    seront utilisés.
    Écriture de l'information d'état étendu... Fait
    Prendre :1 http://fr.archive.ubuntu.com karmic/main libusb-dev 2:0.1.12-13
    [38,8kB]
    38,8ko téléchargés en 0s (102ko/s)
    Sélection du paquet libusb-dev précédemment désélectionné.
    (Lecture de la base de données... 464692 fichiers et répertoires déjà
    installés.)
    Dépaquetage de libusb-dev (à partir de
    .../libusb-dev_2%3a0.1.12-13_i386.deb) ...
    Traitement des actions différées (« triggers ») pour « doc-base »...
    Processing 1 added doc-base file(s)...
    Registering documents with scrollkeeper...
    Traitement des actions différées (« triggers ») pour « man-db »...
    Paramétrage de libusb-dev (2:0.1.12-13) ...


sudo aptitude install libpcsclite-dev
=====================================

::


    patrick@vercors:~$ sudo aptitude install libpcsclite-dev
    [sudo] password for patrick:
    Lecture des listes de paquets... Fait
    Construction de l'arbre des dépendances
    Lecture des informations d'état... Fait
    Lecture de l'information d'état étendu
    Initialisation de l'état des paquets... Fait
    Les NOUVEAUX paquets suivants vont être installés :
     libpcsclite-dev
    0 paquets mis à jour, 1 nouvellement installés, 0 à enlever et 0 non mis à
    jour.
    Il est nécessaire de télécharger 62,1ko d'archives. Après dépaquetage, 205ko
    seront utilisés.
    Écriture de l'information d'état étendu... Fait
    Prendre :1 http://fr.archive.ubuntu.com karmic/main libpcsclite-dev
    1.5.3-1ubuntu1 [62,1kB]
    62,1ko téléchargés en 0s (151ko/s)
    Sélection du paquet libpcsclite-dev précédemment désélectionné.
    (Lecture de la base de données... 464675 fichiers et répertoires déjà
    installés.)
    Dépaquetage de libpcsclite-dev (à partir de
    .../libpcsclite-dev_1.5.3-1ubuntu1_i386.deb) ...
    Paramétrage de libpcsclite-dev (1.5.3-1ubuntu1) ...
    Lecture des listes de paquets... Fait
    Construction de l'arbre des dépendances
    Lecture des informations d'état... Fait
    Lecture de l'information d'état étendu
    Initialisation de l'état des paquets... Fait
    Écriture de l'information d'état étendu... Fait

./configure
-----------

::

    libccid has been configured with following options:

    Version:             1.3.11
    User binaries:       NONE/bin
    Configuration files: NONE/etc


    Host:                i686-pc-linux-gnu
    Compiler:            gcc
    Preprocessor flags:
    Compiler flags:      -g -O2
    Preprocessor flags:
    Linker flags:
    Libraries:

    PCSC_CFLAGS:         -I/usr/include/PCSC
    PCSC_LIBS:           -lpcsclite
    PTHREAD_CFLAGS:      -pthread
    PTHREAD_LIBS:
    BUNDLE_HOST:         Linux
    DYN_LIB_EXT:         so
    LIBUSB_CFLAGS:
    LIBUSB_LIBS:         -lusb
    SYMBOL_VISIBILITY:   -fvisibility=hidden
    NOCLASS:

make
----



/etc/init.d/pcscd stop
======================

::

    /etc/init.d/pcscd stop


sudo ./src/parse > output.txt
=============================

::

    patrick@vercors:~/projects/id3/libccid/ccid-1.3.11$ sudo ./src/parse > output.txt
    Parsing USB bus/device: 001/002
    idVendor:  0x0BDA  iManufacturer: Generic
    idProduct: 0x0151  iProduct: USB2.0-CRW
    NOT a CCID/ICCD device
    Parsing USB bus/device: 001/001
    idVendor:  0x1D6B  iManufacturer: Linux 2.6.31-19-generic ehci_hcd
    idProduct: 0x0002  iProduct: EHCI Host Controller
    NOT a CCID/ICCD device
    Parsing USB bus/device: 002/004
    idVendor:  0x0B81  iManufacturer: id3 Semiconductors
    idProduct: 0x0200  iProduct: Contactless Reader
    Found a CCID/ICCD device at interface 0
    Parsing USB bus/device: 002/001
    idVendor:  0x1D6B  iManufacturer: Linux 2.6.31-19-generic ohci_hcd
    idProduct: 0x0001  iProduct: OHCI Host Controller
    NOT a CCID/ICCD device


.. index::
   pair: CCID; CL1356T5
   pair: CCID; output.txt

CL1356T5 output.txt
===================

.. seealso::

   - http://pcsclite.alioth.debian.org/shouldwork.html#0x0B810x0200
   - http://pcsclite.alioth.debian.org/readers/id3_CL1356T5.txt


CL1356A+ output.txt
===================

.. seealso:: :ref:`usbids`

::

    idVendor: 0x0B81
    iManufacturer: id3 Semiconductors
    idProduct: 0x0200
    iProduct: CL1356A+
    bcdDevice: 11.06 (firmware release?)
    bLength: 9
    bDescriptorType: 4
    bInterfaceNumber: 0
    bAlternateSetting: 0
    bNumEndpoints: 3
    bulk-IN, bulk-OUT and Interrupt-IN
    bInterfaceClass: 0x0B [Chip Card Interface Device Class (CCID)]
    bInterfaceSubClass: 0
    bInterfaceProtocol: 0
    bulk transfer, optional interrupt-IN (CCID)
    Can't get iInterface string
    CCID Class Descriptor
    bLength: 0x36
    bDescriptorType: 0x21
    bcdCCID: 1.10
    bMaxSlotIndex: 0x00
    bVoltageSupport: 0x07
    5.0V
    3.0V
    1.8V
    dwProtocols: 0x0000 0x0003
    T=0
    T=1
    dwDefaultClock: 3.390 MHz
    dwMaximumClock: 13.560 MHz
    bNumClockSupported: 0 (will use whatever is returned)
    IFD does not support GET CLOCK FREQUENCIES request: Success
    dwDataRate: 106000 bps
    dwMaxDataRate: 848000 bps
    bNumDataRatesSupported: 4
    Support 106000 bps
    Support 212000 bps
    Support 424000 bps
    Support 848000 bps
    dwMaxIFSD: 254
    dwSynchProtocols: 0x00000000
    dwMechanical: 0x00000000
    No special characteristics
    dwFeatures: 0x000406FE
    ....02 Automatic parameter configuration based on ATR data
    ....04 Automatic activation of ICC on inserting
    ....08 Automatic ICC voltage selection
    ....10 Automatic ICC clock frequency change according to parameters
    ....20 Automatic baud rate change according to frequency and Fi, Di params
    ....40 Automatic parameters negotiation made by the CCID
    ....80 Automatic PPS made by the CCID
    ..02.. NAD value other than 00 accepted (T=1)
    ..04.. Automatic IFSD exchange as first exchange (T=1)
    04.... Short and Extended APDU level exchange
    dwMaxCCIDMessageLength: 65535 bytes
    bClassGetResponse: 0xFF
    echoes the APDU class
    bClassEnveloppe: 0xFF
    echoes the APDU class
    wLcdLayout: 0x0000
    bPINSupport: 0x00
    bMaxCCIDBusySlots: 1




