
.. index::
   pair: language ; Bash
   ! Bash
   ! Bourne Again SHell


.. _bash_language:

==========================
Bash (Bourne Again SHell)
==========================


.. seealso::

   - http://www.gnu.org/software/bash/
   - http://www.tldp.org/LDP/abs/html/
   - http://www.tldp.org/LDP/abs/html/sample-bashrc.html
   - http://tiswww.case.edu/php/chet/bash/bashtop.html
   - http://fr.wikipedia.org/wiki/Bourne-Again_shell
   - http://pubs.opengroup.org/onlinepubs/9699919799/utilities/sh.html

.. figure:: bash-org.jpg
   :align: center

.. contents::
   :depth: 3



Description
===========

`Bash` is the GNU Project's shell. 

Bash is the ``Bourne Again SHell``. 

Bash is an sh-compatible shell that incorporates useful features from the 
Korn shell (ksh) and C shell (csh). 
It is intended to conform to the IEEE POSIX P1003.2/ISO 9945.2 

Shell and Tools standard. It offers functional improvements over sh for both 
programming and interactive use. In addition, most sh scripts can be run by
Bash without modification.

The improvements offered by Bash include:

- Command line editing
- Unlimited size command history
- Job Control
- Shell Functions and Aliases
- Indexed arrays of unlimited size
- Integer arithmetic in any base from two to sixty-four

The maintainer_ also has a bash page which includes `Frequently-Asked-Questions`_


.. _maintainer:  http://tiswww.case.edu/php/chet/bash/bashtop.html 
.. _`Frequently-Asked-Questions`:  ftp://ftp.cwru.edu/pub/bash/FAQ 

Bash intro
===========

.. seealso::

   - tiswww.case.edu/php/chet/bash/bash-intro.html
   
   
Bash is the shell, or command language interpreter, that will appear in the 
GNU operating system. 

Bash is an sh-compatible shell that incorporates useful features from the 
Korn shell (ksh) and C shell (csh). 

It is intended to conform to the IEEE POSIX P1003.2/ISO 9945.2 

Shell and Tools standard. It offers functional improvements over sh for both 
programming and interactive use. In addition, most sh scripts can be run by Bash 
without modification. 

Bash is quite portable. It uses a configuration system that discovers 
characteristics of the compilation platform at build time, and may therefore 
be built on nearly every version of UNIX. 

Ports to UNIX-like systems such as QNX and Minix and to non-UNIX systems such 
as OS/2, Windows 95/98, and Windows NT are available. 


Sample bash-rc
==============

.. seealso::

   - http://www.tldp.org/LDP/abs/html/sample-bashrc.html
   - http://tldp.org/LDP/abs/html/index.html
   - http://www.caliban.org/bash
   - http://www.shelldorado.com/scripts/categories.html
   - http://www.dotfiles.org
   - http://www.debian-administration.org/articles/205
   - http://www.askapache.com/linux/bash-power-prompt.html
   - http://tldp.org/HOWTO/Bash-Prompt-HOWTO
   - https://github.com/nojhan/liquidprompt   

::

    # =============================================================== #
    #
    # PERSONAL $HOME/.bashrc FILE for bash-3.0 (or later)
    # By Emmanuel Rouat [no-email]
    #
    # Last modified: Tue Nov 20 22:04:47 CET 2012

    #  This file is normally read by interactive shells only.
    #+ Here is the place to define your aliases, functions and
    #+ other interactive features like your prompt.
    #
    #  The majority of the code here assumes you are on a GNU
    #+ system (most likely a Linux box) and is often based on code
    #+ found on Usenet or Internet.
    #
    #  See for instance:
    #  http://tldp.org/LDP/abs/html/index.html
    #  http://www.caliban.org/bash
    #  http://www.shelldorado.com/scripts/categories.html
    #  http://www.dotfiles.org
    #
    #  The choice of colors was done for a shell with a dark background
    #+ (white on black), and this is usually also suited for pure text-mode
    #+ consoles (no X server available). If you use a white background,
    #+ you'll have to do some other choices for readability.
    #
    #  This bashrc file is a bit overcrowded.
    #  Remember, it is just just an example.
    #  Tailor it to your needs.
    #
    # =============================================================== #


Autres liens
------------

::


    #-------------------------------------------------------------
    # Shell Prompt - for many examples, see:
    #       http://www.debian-administration.org/articles/205
    #       http://www.askapache.com/linux/bash-power-prompt.html
    #       http://tldp.org/HOWTO/Bash-Prompt-HOWTO
    #       https://github.com/nojhan/liquidprompt
    #-------------------------------------------------------------
    
    

Advanced Bash-Scripting Guide
=============================

.. seealso::

   - http://www.tldp.org/LDP/abs/html/


This tutorial assumes no previous knowledge of scripting or programming, but
progresses rapidly toward an intermediate/advanced level of instruction . . .
all the while sneaking in little nuggets of UNIX® wisdom and lore.

It serves as a textbook, a manual for self-study, and a reference and source of
knowledge on shell scripting techniques.

The exercises and heavily-commented examples invite active reader participation,
under the premise that the only way to really learn scripting is to write scripts.


Bash versions
=============

.. toctree::
   :maxdepth: 3
   
   versions/index
   
   
