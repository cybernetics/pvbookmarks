


.. _pcsclite_octobre_2014:

=======================
pcsclite octobre 2014
=======================

::

    Author: rousseau
    Date: 2014-10-02 09:26:36 +0000 (Thu, 02 Oct 2014)
    New Revision: 7004

    Modified:
       trunk/PCSC/COPYING
       trunk/PCSC/UnitaryTests/SCardBlockingBehaviourTest.py
       trunk/PCSC/UnitaryTests/SCardExclusiveBehaviour.py
       trunk/PCSC/src/PCSC/debuglog.h
       trunk/PCSC/src/PCSC/ifdhandler.h
       trunk/PCSC/src/PCSC/pcsclite.h.in
       trunk/PCSC/src/PCSC/reader.h
       trunk/PCSC/src/PCSC/winscard.h
       trunk/PCSC/src/PCSC/wintypes.h
       trunk/PCSC/src/atrhandler.c
       trunk/PCSC/src/atrhandler.h
       trunk/PCSC/src/configfile.h
       trunk/PCSC/src/configfile.l
       trunk/PCSC/src/debug.c
       trunk/PCSC/src/debuglog.c
       trunk/PCSC/src/dyn_generic.h
       trunk/PCSC/src/dyn_hpux.c
       trunk/PCSC/src/dyn_macosx.c
       trunk/PCSC/src/dyn_unix.c
       trunk/PCSC/src/error.c
       trunk/PCSC/src/eventhandler.c
       trunk/PCSC/src/eventhandler.h
       trunk/PCSC/src/hotplug.h
       trunk/PCSC/src/hotplug_generic.c
       trunk/PCSC/src/hotplug_libudev.c
       trunk/PCSC/src/hotplug_libusb.c
       trunk/PCSC/src/hotplug_linux.c
       trunk/PCSC/src/hotplug_macosx.c
       trunk/PCSC/src/ifdwrapper.c
       trunk/PCSC/src/ifdwrapper.h
       trunk/PCSC/src/lassert.h
       trunk/PCSC/src/misc.h
       trunk/PCSC/src/parser.h
       trunk/PCSC/src/pcsc-wirecheck-gen.c
       trunk/PCSC/src/pcscdaemon.c
       trunk/PCSC/src/powermgt_generic.c
       trunk/PCSC/src/powermgt_generic.h
       trunk/PCSC/src/prothandler.c
       trunk/PCSC/src/prothandler.h
       trunk/PCSC/src/readerfactory.c
       trunk/PCSC/src/readerfactory.h
       trunk/PCSC/src/strlcpycat.h
       trunk/PCSC/src/sys_generic.h
       trunk/PCSC/src/sys_unix.c
       trunk/PCSC/src/testpcsc.c
       trunk/PCSC/src/tokenparser.l
       trunk/PCSC/src/utils.c
       trunk/PCSC/src/utils.h
       trunk/PCSC/src/utils/formaticc.c
       trunk/PCSC/src/utils/installifd.c
       trunk/PCSC/src/winscard.c
       trunk/PCSC/src/winscard_clnt.c
       trunk/PCSC/src/winscard_msg.c
       trunk/PCSC/src/winscard_msg.h
       trunk/PCSC/src/winscard_msg_srv.c
       trunk/PCSC/src/winscard_svc.c
       trunk/PCSC/src/winscard_svc.h
    Log:
    Make the license more 3-clause BSD like

    The line "Changes to this license can be made only by the copyright
    author with explicit written consent." was present in the pcsc-lite
    license from the origin of the project (at least since the initial
    version of COPYING in the VCS in March 2002).

    This line is not present in the 3-clause BSD license
    http://en.wikipedia.org/wiki/BSD_licenses

    The change has been approved by David Corcoran, initial author of
    pcsc-lite.

    The change was requested by Oracle about the headers files winscard.h
    and pcsclite.h " To include in OpenJDK, Oracle needs the right to
    relicense under other terms."
