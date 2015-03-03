
.. index::
   DBUS and smartcard
   smartcard and DBUS

.. _smartcard_and_dbus:

====================
DBUS and smartcard
====================


http://lists.drizzle.com/pipermail/muscle/2011-September/009131.html
====================================================================

::

    Florian Echtler floe at butterbrot.org
    Fri Sep 2 02:46:29 PDT 2011


Hello everyone,

a while ago, there was a discussion in xdg [1] about DBus support for
smartcard activity. I've hacked together a bash script for that purpose::

    #!/bin/bash
    pcsc_scan -n | { while read RESULT; do

        ATR=$(echo $RESULT | perlgrep "ATR: ..35m(.*)\e")
        [ "$ATR" ] && dbus-send --session
    --type=signal /org/debian/alioth/pcsclite/reader0/slot0
    org.debian.alioth.pcsclite.CardPresence string:"$ATR"

        RMV=$(echo $RESULT | grep "removed")
        [ "$RMV" ] && dbus-send --session
    --type=signal /org/debian/alioth/pcsclite/reader0/slot0
    org.debian.alioth.pcsclite.CardPresence boolean:false

    done }

However, I think it would be a bit smoother to directly integrate this
into pcsc-lite. The best to add support would be in eventhandler.c,
correct?

Florian

[1] http://lists.freedesktop.org/archives/xdg/2009-August/011008.html
