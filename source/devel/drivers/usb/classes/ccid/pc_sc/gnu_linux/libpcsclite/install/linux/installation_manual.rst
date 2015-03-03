
.. index::
   pair: libpcsclite ; installation

.. _libpcsclite_installation:

========================
libpcsclite installation
========================

.. seealso::

   - :term:`PCSC Lite`


.. _libpcsclite_installation_on_gnu_linux:

Prerequisite
============


.. seealso::

   - :ref:`pcscd_uses_libudev_instead_of_libhal`


- libudev

::

    sudo aptitude install libudev-dev
    Les NOUVEAUX paquets suivants vont être installés :
      libudev-dev
    0 paquets mis à jour, 1 nouvellement installés, 0 à enlever et 20 non mis à jour.
    Il est nécessaire de télécharger 153ko d'archives. Après dépaquetage, 504ko seront utilisés.
    Prendre :1 http://fr.archive.ubuntu.com/ubuntu/ maverick-updates/main libudev-dev i386 162-2.2 [153kB]
    153ko téléchargés en 1s (153ko/s)
    Sélection du paquet libudev-dev précédemment désélectionné.
    (Lecture de la base de données... 251274 fichiers et répertoires déjà installés.)
    Dépaquetage de libudev-dev (à partir de .../libudev-dev_162-2.2_i386.deb) ...
    Paramétrage de libudev-dev (162-2.2) ...


Package installation
====================

on fedora
---------

::

    yum install libpcsclite-dev


Manual installation
===================

.. warning:: libusb must be installed before libpcsclite.


::

    bunzip2 pcsc-lite-x.y.z.tar.bz2
    tar xvf pcsc-lite-x.y.z.tar
    cd pcsc-lite-x.y.z
    chmod +x configure
    ./configure --disable-libhal LIBUSB_LIBS="-L/opt/libusb/current/lib -lusb-1.0" --prefix=/opt/pcsclite/x.y.z
    make



Exemple for the last version 1.x.y
------------------------------------

The last version of libpcsclite is 1.7.4 (june 23, 2011)

::

    cd pcsc-lite-1.x.y
    chmod +x configure
    ./configure --disable-libhal LIBUSB_LIBS="-L/opt/libusb/current -lusb-1.0" --prefix=/opt/pcsclite/1.x.y
    make


::

    PC/SC lite has been configured with following options:
    Version:             1.x.y
    System binaries:     /opt/pcsclite/1.x.y /sbin
    Configuration dir:   /opt/pcsclite/1.x.y /etc/reader.conf.d
    Host:                i686-pc-linux-gnu
    Compiler:            gcc
    Preprocessor flags:  -I${top_srcdir}/src
    Compiler flags:      -Wall -fno-common -g -O2
    Preprocessor flags:  -I${top_srcdir}/src
    Linker flags:
    Libraries:

    PTHREAD_CFLAGS:      -pthread
    PTHREAD_LIBS:
    PCSC_ARCH:           Linux

    pcscd binary          /opt/pcsclite/1.x.y /sbin/pcscd
    libudev support:      yes
    libusb support:       no
    USB drop directory:   /opt/pcsclite/1.x.y /lib/pcsc/drivers
    ATR parsing messages: false
    ipcdir:               /var/run/pcscd
    use serial:           yes
    use usb:              yes




make
----



make install
-------------

::

    Libraries have been installed in:  /opt/pcsclite/1.x.y /lib
    If you ever happen to want to link against installed libraries
    in a given directory, LIBDIR, you must either use libtool, and
    specify the full pathname of the library, or use the `-LLIBDIR'
    flag during linking and do at least one of the following:
       - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
         during execution
       - add LIBDIR to the `LD_RUN_PATH' environment variable
         during linking
       - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
       - have your system administrator add LIBDIR to `/etc/ld.so.conf'



After make install
------------------


In /opt/pcsclite/1.x.y ::

    ├── include
    │   └── PCSC
    │       ├── debuglog.h
    │       ├── ifdhandler.h
    │       ├── pcsclite.h
    │       ├── reader.h
    │       ├── winscard.h
    │       └── wintypes.h
    ├── lib
    │   ├── libpcsclite.la
    │   ├── libpcsclite.so -> libpcsclite.so.1.0.0
    │   ├── libpcsclite.so.1 -> libpcsclite.so.1.0.0
    │   ├── libpcsclite.so.1.0.0
    │   └── pkgconfig
    │       └── libpcsclite.pc
    ├── sbin
    │   └── pcscd
    └── share
        ├── doc
        │   └── pcsc-lite
        │       └── README.DAEMON
        └── man
            ├── man5
            │   └── reader.conf.5
            └── man8
                └── pcscd.8



Link to the the current libusb version
======================================

::

    cd /opt/pcsclite/1.x.y
    ln -s 1.x.y  current
    ls -als


::

    drwxr-xr-x 3 root root 4096 2011-04-07 13:56 ./
    drwxr-xr-x 5 root root 4096 2011-04-07 13:54 ../
    drwxr-xr-x 6 root root 4096 2011-04-07 13:54 1.x.y /
    lrwxrwxrwx 1 root root    5 2011-04-07 13:56 current -> 1.x.y /


.. index::
   pcsc
   pcscd daemon
   pcscd help

The pcscd daemon
================

pcscd help
----------

::

    cd /opt/pcsclite/current/sbin
    sudo pcscd -h

::

    Usage: ./pcscd options
    Options:
      -a, --apdu        log APDU commands and results
      -c, --config        path to reader.conf
      -f, --foreground    run in foreground (no daemon),
                        send logs to stderr instead of syslog
      -h, --help        display usage information
      -H, --hotplug        ask the daemon to rescan the available readers
      -v, --version        display the program version number
      -d, --debug         display lower level debug messages
          --info         display info level debug messages (default level)
      -e  --error         display error level debug messages
      -C  --critical     display critical only level debug messages
      --force-reader-polling ignore the IFD_GENERATE_HOTPLUG reader capability
      -t, --max-thread    maximum number of threads (default 200)
      -s, --max-card-handle-per-thread    maximum number of card handle per thread
            (default: 200)
      -r, --max-card-handle-per-reader    maximum number of card handle per reader
            (default: 200)






