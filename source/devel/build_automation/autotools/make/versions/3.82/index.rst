



.. _gnu_make_3_82:

===============================================
GNU Make 3.82 , mer. 28 juil. 2010 06:56:40 UTC
===============================================


.. seealso::

   - https://savannah.gnu.org/forum/forum.php?forum_id=6446
   - http://sv.gnu.org/bugs/index.php?group=make&report_id=111&fix_release_id=104&set=custom


.. contents::
   :depth: 3

Introduction
=============

The next stable version of GNU make, version 3.81, has been released and is
available for download from http://ftp.gnu.org/gnu/make/.

This version contains many bug fixes, as well as feature enhancements.

There are also some backward-incompatibilities. Please see the NEWS file that comes with the GNU make distribution for complete details on user-visible changes.


A complete list of bugs fixed in this version is available `here <http://sv.gnu.org/bugs/index.php?group=make&report_id=111&fix_release_id=104&set=custom>`_


Changes
=======


* Compiling GNU make now requires a conforming ISO C 1989 compiler and
  standard runtime library.

* WARNING: Future backward-incompatibility!
  Wildcards are not documented as returning sorted values, but up to and
  including this release the results have been sorted and some makefiles are
  apparently depending on that.  In the next release of GNU make, for
  performance reasons, we may remove that sorting.  If your makefiles
  require sorted results from wildcard expansions, use the $(sort ...)
  function to request it explicitly.

* WARNING: Backward-incompatibility!
  The POSIX standard for make was changed in the 2008 version in a
  fundamentally incompatible way: make is required to invoke the shell as if
  the '-e' flag were provided.  Because this would break many makefiles that
  have been written to conform to the original text of the standard, the
  default behavior of GNU make remains to invoke the shell with simply '-c'.
  However, any makefile specifying the .POSIX special target will follow the
  new POSIX standard and pass '-e' to the shell.  See also .SHELLFLAGS
  below.

* WARNING: Backward-incompatibility!
  The '$?' variable now contains all prerequisites that caused the target to
  be considered out of date, even if they do not exist (previously only
  existing targets were provided in $?).

* WARNING: Backward-incompatibility!
  As a result of parser enhancements, three backward-compatibility issues
  exist: first, a prerequisite containing an "=" cannot be escaped with a
  backslash any longer.  You must create a variable containing an "=" and
  use that variable in the prerequisite.  Second, variable names can no
  longer contain whitespace, unless you put the whitespace in a variable and
  use the variable.  Third, in previous versions of make it was sometimes
  not flagged as an error for explicit and pattern targets to appear in the
  same rule.  Now this is always reported as an error.

* WARNING: Backward-incompatibility!
  The pattern-specific variables and pattern rules are now applied in the
  shortest stem first order instead of the definition order (variables
  and rules with the same stem length are still applied in the definition
  order). This produces the usually-desired behavior where more specific
  patterns are preferred. To detect this feature search for 'shortest-stem'
  in the .FEATURES special variable.

* WARNING: Backward-incompatibility!
  The library search behavior has changed to be compatible with the standard
  linker behavior. Prior to this version for prerequisites specified using
  the -lfoo syntax make first searched for libfoo.so in the current
  directory, vpath directories, and system directories. If that didn't yield
  a match, make then searched for libfoo.a in these directories. Starting
  with this version make searches first for libfoo.so and then for libfoo.a
  in each of these directories in order.

* New command line option: --eval=STRING causes STRING to be evaluated as
  makefile syntax (akin to using the $(eval ...) function).  The evaluation
  is performed after all default rules and variables are defined, but before
  any makefiles are read.

* New special variable: .RECIPEPREFIX allows you to reset the recipe
  introduction character from the default (TAB) to something else.  The
  first character of this variable value is the new recipe introduction
  character.  If the variable is set to the empty string, TAB is used again.
  It can be set and reset at will; recipes will use the value active when
  they were first parsed.  To detect this feature check the value of
  $(.RECIPEPREFIX).

* New special variable: .SHELLFLAGS allows you to change the options passed
  to the shell when it invokes recipes.  By default the value will be "-c"
  (or "-ec" if .POSIX is set).

* New special target: .ONESHELL instructs make to invoke a single instance
  of the shell and provide it with the entire recipe, regardless of how many
  lines it contains.  As a special feature to allow more straightforward
  conversion of makefiles to use .ONESHELL, any recipe line control
  characters ('@', '+', or '-') will be removed from the second and
  subsequent recipe lines.  This happens _only_ if the SHELL value is deemed
  to be a standard POSIX-style shell.  If not, then no interior line control
  characters are removed (as they may be part of the scripting language used
  with the alternate SHELL).

* New variable modifier 'private': prefixing a variable assignment with the
  modifier 'private' suppresses inheritance of that variable by
  prerequisites.  This is most useful for target- and pattern-specific
  variables.

* New make directive: 'undefine' allows you to undefine a variable so that
  it appears as if it was never set. Both $(flavor) and $(origin) functions
  will return 'undefined' for such a variable. To detect this feature search
  for 'undefine' in the .FEATURES special variable.

* The parser for variable assignments has been enhanced to allow multiple
  modifiers ('export', 'override', 'private') on the same line as variables,
  including define/endef variables, and in any order.  Also, it is possible
  to create variables and targets named as these modifiers.

* The 'define' make directive now allows a variable assignment operator
  after the variable name, to allow for simple, conditional, or appending
  multi-line variable assignment.
