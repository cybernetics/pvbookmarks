
.. index::
   pair: gdb ; 7.4.0


.. _gdb_7_4_0:

=============================
GDB 7.4.0
=============================


::

    Joel Brobecker brobecker@adacore.com via sourceware.org
    heure de l'expéditeur:   Envoyé à 14:32 (GMT-05:00). Heure locale : 09:26. ✆
    à:   gdb-announce@sourceware.org
    date:    13 décembre 2011 14:32
    objet:   GDB 7.4 release process created!
    liste de diffusion:  <gdb-announce.sourceware.org> Filtrer les messages de cette liste de diffusion
    envoyé par:  sourceware.org


Hello,

A quick message to announce that the GDB 7.4 branch has just been created.

If all goes well, we should publish the GDB 7.4 release at the start of
next year.



Announce
========

.. seealso:: http://www.gnu.org/software/gdb/download/ANNOUNCEMENT


Release 7.4 of GDB, the GNU Debugger, is now available via anonymous
FTP.  GDB is a source-level debugger for Ada, C, C++, Objective-C,
Pascal and many other languages.  GDB can target (i.e., debug programs
running on) more than a dozen different processor architectures, and GDB
itself can run on most popular GNU/Linux, Unix and Microsoft Windows
variants.

You can download GDB from the GNU FTP server in the directory::

    ftp://ftp.gnu.org/gnu/gdb

The vital stats::

    Size  md5sum                            Name
    20MB  95a9a8305fed4d30a30a6dc28ff9d060  gdb-7.4.tar.bz2
    27MB  7877875c8af7c7ef7d06d329ac961d3f  gdb-7.4.tar.gz

There is a web page for GDB at::

    http://www.gnu.org/software/gdb/

That page includes information about GDB mailing lists (an announcement
mailing list, developers discussion lists, etc.), details on how to
access GDB's CVS repository, locations for development snapshots,
preformatted documentation, and links to related information around
the net.  We will put errata notes and host-specific tips for this release
on-line as any problems come up.  All mailing lists archives are also
browsable via the web.

GDB 7.4 brings new targets, features and improvements, including
================================================================

New target: Texas Instruments TMS320C6x (tic6x-)
---------------------------------------------------

New simulator: Renesas RL78 (rl78--elf)
----------------------------------------

New configure option --with-iconv-bin
-------------------------------------

Python scripting improvements
------------------------------

- The Python commands and convenience functions located in
  the data directory are now automatically loaded on GDB start-up.
- New command "set python print-stack none|full|message",
  replacing "maint set python print-stack on|off", which has
  been deprecated in GDB 7.5.
- The "gdb.breakpoint" function has been deprecated in favor of
  "gdb.breakpoints".
- Type objects for struct and union types now allow access to
  the fields using standard Python dictionary (mapping) methods.
- Four new attributes in class Block.
- Class Symbols now provides a "type" attribute.
- A prompt substitution hook, and a new gdb.prompt module.
- A new class "gdb.FinishBreakpoint".
- A new event "gdb.new_objfile".
- A new function, "deep_items" has been added to module gdb.types.

Changes to existing commands
----------------------------

- libthread-db-search-path now supports two special values:
    $sdir and $pdir

New commands
------------

- "skip file", "skip function": To skip uninteresting functions
  during debugging.
- watch EXPRESSION mask MASK_VALUE
- info auto-load-scripts [REGEXP]
- info macro [-all] [--] MACRO
- collect[/s] EXPRESSIONS
- tstart [NOTES]
- tstop [NOTES]
- "!" (alias of the "shell" command)

New options
-----------

- set extended-prompt
  show extended-prompt
- set print entry-values (both|compact|default|if-needed|no|only| preferred)
  show print entry-values
- set debug entry-values
  show debug entry-values
- set basenames-may-differ
  show basenames-may-differ
- set trace-user
  show trace-user
- set trace-notes
  show trace-notes
- set trace-stop-notes
  show trace-stop-notes

- GDB now handles ambiguous linespecs more consistently, and set
  a breakpoint on all matching locations.  Locations will be added
  or removed according to inferior changes.

- Masked Watchpoint support on PowerPC BookE running a Linux kernel (version 2.6.34 or later).

- Ability to display function parameter values at the time the function
  gets called (only available with code compiled with GCC 4.7 or later).
  See new option "set print entry-values".

Tracepoint improvements
-----------------------

- Ability to enable and disable tracepoints at any time after
  a trace experiment has been started.
- Fast tracepoints on 32-bit x86-architectures can now be placed
  at locations with 4-byte instructions (the minimum was previously 5 bytes).

Remote protocol changes
-----------------------

- New packets: QTEnable, QTDisable, QTNotes, qTP, qTMinFTPILen,
- New commands: "set dcache line" and "set dcache line-size".
- New command "set remote hardware-watchpoint-length-limit".

GDB/MI changes
--------------

- "stopped" events can report several new "reason"s.
- Breakpoint changes are now notified using new async records.
- New command: -ada-task-info.

New GDBserver operation: --once
-------------------------------

The gdbtui binary will be deprecated deprecated starting with GDB 7.5.

Use "gdb -tui" instead.


For a complete list and more details on each item, please see the
gdb/NEWS file.
