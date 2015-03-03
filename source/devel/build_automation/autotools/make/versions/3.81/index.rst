





.. _gnu_make_3_81:

===============================================
GNU Make 3.81 sam. 01 avril 2006 07:25:13 UTC
===============================================


.. seealso::

   - https://savannah.gnu.org/forum/forum.php?forum_id=4380
   - http://savannah.gnu.org/bugs/index.php?group=make&report_id=111&fix_release_id=103


.. contents::
   :depth: 3

Introduction
=============

Item posté par Paul D. Smith <psmith> le mer. 28 juil. 2010 06:56:40 UTC.

The next stable version of GNU make, version 3.81, has been released and is
available for download from http://ftp.gnu.org/gnu/make/.

This version contains many bug fixes, as well as feature enhancements.

There are also some backward-incompatibilities. Please see the NEWS file that
comes with the GNU make distribution for complete details on user-visible changes.



Changes
=======


* GNU make is ported to OS/2.

* GNU make is ported to MinGW.  The MinGW build is only supported by
  the build_w32.bat batch file; see the file README.W32 for more
  details.

* WARNING: Future backward-incompatibility!
  Up to and including this release, the '$?' variable does not contain
  any prerequisite that does not exist, even though that prerequisite
  might have caused the target to rebuild.  Starting with the _next_
  release of GNU make, '$?' will contain all prerequisites that caused
  the target to be considered out of date.  See this Savannah bug:
  http://savannah.gnu.org/bugs/index.php?func=detailitem&item_id=16051

* WARNING: Backward-incompatibility!
  GNU make now implements a generic "second expansion" feature on the
  prerequisites of both explicit and implicit (pattern) rules.  In order
  to enable this feature, the special target '.SECONDEXPANSION' must be
  defined before the first target which takes advantage of it.  If this
  feature is enabled then after all rules have been parsed the
  prerequisites are expanded again, this time with all the automatic
  variables in scope.  This means that in addition to using standard
  SysV $$@ in prerequisites lists, you can also use complex functions
  such as $$(notdir $$@) etc.  This behavior applies to implicit rules,
  as well, where the second expansion occurs when the rule is matched.
  However, this means that when '.SECONDEXPANSION' is enabled you must
  double-quote any "$" in your filenames; instead of "foo: boo$$bar" you
  now must write "foo: foo$$$$bar".  Note that the SysV $$@ etc. feature,
  which used to be available by default, is now ONLY available when the
  .SECONDEXPANSION target is defined.  If your makefiles take advantage
  of this SysV feature you will need to update them.

* WARNING: Backward-incompatibility!
  In order to comply with POSIX, the way in which GNU make processes
  backslash-newline sequences in command strings has changed.  If your
  makefiles use backslash-newline sequences inside of single-quoted
  strings in command scripts you will be impacted by this change.  See
  the GNU make manual subsection "Splitting Command Lines" (node
  "Splitting Lines"), in section "Command Syntax", chapter "Writing the
  Commands in Rules", for details.

* WARNING: Backward-incompatibility!
  Some previous versions of GNU make had a bug where "#" in a function
  invocation such as $(shell ...) was treated as a make comment.  A
  workaround was to escape these with backslashes.  This bug has been
  fixed: if your makefile uses "\#" in a function invocation the
  backslash is now preserved, so you'll need to remove it.

* New command-line option: -L (--check-symlink-times).  On systems that
  support symbolic links, if this option is given then GNU make will
  use the most recent modification time of any symbolic links that are
  used to resolve target files.  The default behavior remains as it
  always has: use the modification time of the actual target file only.

* The "else" conditional line can now be followed by any other valid
  conditional on the same line: this does not increase the depth of the
  conditional nesting, so only one "endif" is required to close the
  conditional.

* All pattern-specific variables that match a given target are now used
  (previously only the first match was used).

* Target-specific variables can be marked as exportable using the
  "export" keyword.

* In a recursive $(call ...) context, any extra arguments from the outer
  call are now masked in the context of the inner call.

* Implemented a solution for the "thundering herd" problem with "-j -l".
  This version of GNU make uses an algorithm suggested by Thomas Riedl
  <thomas.riedl@siemens.com> to track the number of jobs started in the
  last second and artificially adjust GNU make's view of the system's
  load average accordingly.

* New special variables available in this release:
   - .INCLUDE_DIRS: Expands to a list of directories that make searches
     for included makefiles.
   - .FEATURES: Contains a list of special features available in this
     version of GNU make.
   - .DEFAULT_GOAL: Set the name of the default goal make will
     use if no goals are provided on the command line.
   - MAKE_RESTARTS: If set, then this is the number of times this
     instance of make has been restarted (see "How Makefiles Are Remade"
     in the manual).
   - New automatic variable: $| (added in 3.80, actually): contains all
     the order-only prerequisites defined for the target.

* New functions available in this release:
   - $(lastword ...) returns the last word in the list.  This gives
     identical results as $(word $(words ...) ...), but is much faster.
   - $(abspath ...) returns the absolute path (all "." and ".."
     directories resolved, and any duplicate "/" characters removed) for
     each path provided.
   - $(realpath ...) returns the canonical pathname for each path
     provided.  The canonical pathname is the absolute pathname, with
     all symbolic links resolved as well.
   - $(info ...) prints its arguments to stdout.  No makefile name or
     line number info, etc. is printed.
   - $(flavor ...) returns the flavor of a variable.
   - $(or ...) provides a short-circuiting OR conditional: each argument
     is expanded.  The first true (non-empty) argument is returned; no
     further arguments are expanded.  Expands to empty if there are no
     true arguments.
   - $(and ...) provides a short-circuiting AND conditional: each
     argument is expanded.  The first false (empty) argument is
     returned; no further arguments are expanded.  Expands to the last
     argument if all arguments are true.

* Changes made for POSIX compatibility:
   - Only touch targets (under -t) if they have at least one command.
   - Setting the SHELL make variable does NOT change the value of the
     SHELL environment variable given to programs invoked by make.  As
     an enhancement to POSIX, if you export the make variable SHELL then
     it will be set in the environment, just as before.

* On MS Windows systems, explicitly setting SHELL to a pathname ending
  in "cmd" or "cmd.exe" (case-insensitive) will force GNU make to use
  the DOS command interpreter in batch mode even if a UNIX-like shell
  could be found on the system.

* On VMS there is now support for case-sensitive filesystems such as ODS5.
  See the readme.vms file for information.

* Parallel builds (-jN) no longer require a working Bourne shell on
  Windows platforms.  They work even with the stock Windows shells, such
  as cmd.exe and command.com.

* Updated to autoconf 2.59, automake 1.9.5, and gettext 0.14.1.  Users
  should not be impacted.

* New translations for Swedish, Chinese (simplified), Ukrainian,
  Belarusian, Finnish, Kinyarwandan, and Irish.  Many updated
  translations.

A complete list of bugs fixed in this version is available here:

  http://savannah.gnu.org/bugs/index.php?group=make&report_id=111&fix_release_id=103
