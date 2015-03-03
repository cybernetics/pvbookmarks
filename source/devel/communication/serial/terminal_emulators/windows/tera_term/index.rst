

.. index::
   pair: Tera; Term



.. _tera_term:

===============================
Terminal emulator "Tera Term"
===============================

.. seealso::

   - http://ttssh2.sourceforge.jp/


.. figure:: tera_term.jpg
   :align: center

.. contents::
   :depth: 3


TeraTerm Project
================

TeraTerm Project would have been developed terminal emulator "Tera Term" 
and SSH module "TTSSH". 

This software is open source software under BSD License. This is Tera 
Term Pro 2.3 succession version and is being officially recognized by 
the original author. Development is continuing in Project Page on 
SourceForge.jp.


Specifications
===============

Tera Term is a free software terminal emulator (communication program) 
which supports:

- **Serial port connections**
- TCP/IP (telnet, SSH1, SSH2) connections.
- Log replaying.
- Named pipe connection.
- IPv6 communication.
- VT100 emulation and selected VT200/300 emulation.
- TEK4010 emulation.
- File transfer protocols (Kermit, XMODEM, YMODEM, ZMODEM, B-PLUS and Quick-VAN).
- **Scripts** using the :ref:`"Tera Term Language" <macro_tera_term>`.
- Japanese, English, Russian and Korean character sets.
- UTF-8 character encoding.
- Message catalog(Japanese, English, German, French and Russian).


TeraTerm source code
====================

.. seealso:: 

   - http://en.sourceforge.jp/projects/ttssh2/svn/view/trunk/?root=ttssh2
   - http://en.sourceforge.jp/projects/ttssh2/svn/view/trunk/teraterm/?root=ttssh2



Download
=========

.. seealso::

   - http://en.sourceforge.jp/projects/ttssh2/releases/

Latest version is available from `SourceForge.jp download page`_. 
Current latest release is `4.77`_.

If you can get latest development version, the source code is available from SVN repository. And snapshot is here.
Here is the Old release, however we recommend using the latest release as possible.
Manual

.. _`SourceForge.jp download page`:  http://en.sourceforge.jp/projects/ttssh2/releases/
.. _`4.77`:  http://sourceforge.jp/projects/ttssh2/downloads/58215/teraterm-4.77.exe/


.. _installation_tera_term:

Installation under C:\Program Files (x86)\teraterm
===================================================

::

    C:\Program Files (x86)\teraterm
    | 
    |   cyglaunch.exe
    |   cygterm+.tar.gz
    |   cygterm.cfg
    |   cygterm.exe
    |   delpassw.ttl
    |   dialup.ttl
    |   EDITOR.CNF
    |   FUNCTION.CNF
    |   IBMKEYB.CNF
    |   KEYBOARD.CNF
    |   keycode.exe
    |   license.txt
    |   login.ttl
    |   mpause.ttl
    |   NT98KEYB.CNF
    |   PC98KEYB.CNF
    |   random.ttl
    |   screencapture.ttl
    |   ssh2login.ttl
    |   ssh_known_hosts
    |   teraterm.chm
    |   TERATERM.INI
    |   teratermj.chm
    |   ttermpro.exe
    |   ttmenu_readme-j.txt
    |   ttpcmn.dll
    |   ttpdlg.dll
    |   ttpfile.dll
    |   ttpmacro.exe
    |   ttpmenu.exe
    |   ttpset.dll
    |   ttptek.dll
    |   TTXAlwaysOnTop.dll
    |   TTXProxy.dll
    |   TTXRecurringCommand.dll
    |   TTXResizeMenu.dll
    |   ttxssh.dll
    |   TTXttyplay.dll
    |   TTXttyrec.dll
    |   TTXViewMode.dll
    |   unins000.dat
    |   unins000.exe
    |   wait_regex.ttl
    |   
    +---Collector
    |       Collector.exe
    |       collector.ini
    |       Collector_org.exe
    |       hthook.dll
    |       mfc70.dll
    |       msvcr70.dll
    |       readme.txt
    |       
    +---lang
    |       Default.lng
    |       French.lng
    |       German.lng
    |       Japanese.lng
    |       
    +---plugin
    |       ttAKJpeg.dll
    |       ttAKJpeg.txt
    |       
    \---theme
        |   Advanced.sample
        |   ImageFile.INI
        |   Scale.INI
        |   Tile.INI
        |   
        +---scale
        |       23.jpg
        |       43.jpg
        |       
        \---tile
                03.jpg
                44.jpg
            



Following manuals are available
===============================

.. seealso::

   - http://ttssh2.sourceforge.jp/manual/en/
   - http://ttssh2.sourceforge.jp/manual/en/macro/


- `Tera Term Help Index`_
- `MACRO for TeraTerm`_


.. _`Tera Term Help Index`:  http://ttssh2.sourceforge.jp/manual/en/
.. _`MACRO for TeraTerm`:  http://ttssh2.sourceforge.jp/manual/en/macro/


MACRO for Tera Term ("Tera Term Language (TTL)")
=================================================

.. toctree::
   :maxdepth: 3
   
   macro/index
   
   







