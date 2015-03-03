
.. index::
   pair: ttpmacro; Tera Term



.. _macro_tera_term:

=================================================================
MACRO (ttpmacro.exe)  for Tera Term ("Tera Term Language (TTL)")
=================================================================

.. seealso::

   - http://ttssh2.sourceforge.jp/manual/en/macro/
   - :ref:`tera_term`


Introduction
=============


::

    Copyright (C) 1994-1998 T. Teranishi
    Copyright (C) 2004-2013 TeraTerm Project
    All Rights Reserved.

``MACRO`` (ttpmacro.exe) is an interpreter of the macro language 
"Tera Term Language (TTL)", which controls Tera Term and provides various 
functions like auto dialing, auto login and so on.


How to run a macro file
=======================

.. seealso:: http://ttssh2.sourceforge.jp/manual/en/macro/howtorun.html


The executable file ttpmacro.exe should be placed in the directory in 
which TTERMPRO.EXE exists.

There are two ways to run a macro file.


.. _macro_tera_term_methode1:

1) From Tera Term (Open Macro dialog box)
------------------------------------------

To start MACRO, select the [Control] Macro command and then the macro 
file in the Open Macro dialog box.


.. _macro_tera_term_methode2:

2) From MACRO ( macro file specified as a parameter of the command line) 
------------------------------------------------------------------------

.. seealso::
 
   - :ref:`installation_tera_term`


::

    C:\Program Files (x86)\teraterm
    |   dialup.ttl
    |   ttpmacro.exe



The macro file can be specified as a parameter of the command line 
(shortcut link) of ``ttpmacro.exe``. 

For example, if you want to run the macro file "dialup.ttl", specify the 
command line (shortcut link) like::

   ttpmacro dialup.ttl

You can omit the file name extension ".ttl". 


If you omit the file name, the Open Macro dialog box appears. 
It's convenient to install icons (shortcuts) for the macro files you use 
frequently.

If you choose :ref:`method 2) <macro_tera_term_methode2>`, you can run 
Tera Term, after starting the MACRO, by using the "connect" command in 
the macro file.

While the macro is running, you can pause it, restart it, and stop it 
by pressing the appropriate buttons in the MACRO dialog box.

Note: Running without displaying a window
==========================================

To run without displaying a window, activate TTERMPRO.EXE or ttpmacro.exe 
with a command line option of ``/V``.

When TTERMPRO.EXE is run by using "connect" macro command, "/V" must be 
specified as an argument for it.

This option is required to run without logging in such as using a task.

Note: Loading a macro file
===========================

A macro file is loaded into memory all at once, and the macro is 
interpreted. However, the macro command include always reads a specified 
macro file. When a macro file on the network file server is executed, 
the macro command include may fail if the network is down. 










