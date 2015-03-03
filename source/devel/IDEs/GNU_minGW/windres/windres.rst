
.. index::
   pair: Resource ; Compiler
   ! windres

.. _windres:

=================================
MinGW Resource Compiler (windres)
=================================

.. seealso::

   - http://oldwiki.mingw.org/index.php/MS%20resource%20compiler
   - http://www.mingw.org/wiki/MS_resource_compiler


.. contents::
   :depth: 3

Introduction
============

The MinGW32 compilers come with a fairly decent resource compiler for
Windows resources. There is no visual editor though, so you will have
to your own resource scripts and have some other means to create ICO
files and the like.

The main difference between using the MS resource tools and the GNU
tools is that MS rc generates a ".res" file in a special binary resource
format, which can be passed directly to MS link, while the GNU linker
ld  only supports resources  in ".o" (same as ".obj") format (although
windres can output in both formats).

Therefore, to convert commands like this:::

    rc foo.rc
    link -out:foo.exe foo.obj foo.res

You need something like the following for the GNU tools::

    windres foo.rc foores.o
    gcc -o foo.exe foo.o foores.o

windres -h
==========


::


    C:\MinGW\bin>windres -h
    Usage: windres [options] [fichier-d-entrée] [fichier-de-sortie]
     The options are:
      -i --input=<file>            Name input file
      -o --output=<file>           Name output file
      -J --input-format=<format>   Specify input format
      -O --output-format=<format>  Specify output format
      -F --target=<target>         Specify COFF target
         --preprocessor=<program>  Program to use to preprocess rc file
      -I --include-dir=<dir>       Include directory when preprocessing rc file
      -D --define <sym>[=<val>]    Define SYM when preprocessing rc file
      -U --undefine <sym>          Undefine SYM when preprocessing rc file
      -v --verbose                 Verbose - tells you what it's doing
      -c --codepage=<codepage>     Specify default codepage
      -l --language=<val>          Set language when reading rc file
         --use-temp-file           Use a temporary file instead of popen to read
                                   the preprocessor output
         --no-use-temp-file        Use popen (default)

    Les options sont:
       -r                        ignoré pour la compatibilité avec rc
      @<fichier>                 lire les options à partir du <fichier>
       -h --help                 afficher l'aide-mémoire
       -V --version              afficher le nom et la version du logiciel

    FORMAT est soit rc, res, ou coff, et est déduit à partir l'extension
    du nom de fichier, si non spécifié. Un nom simple de fichier comme fichier d'entrée
    L'entrée par défaut se fait à partir de stdin, par défaut pour rc.
    La sortie par défaut est stdout, par défaut pour rc.
    windres: cibles supportés: pe-i386 pei-i386 elf32-i386 elf32-little elf32-big srec
    symbolsrec verilog tekhex binary ihex
    Rapporter toutes anomalies à <http://www.sourceware.org/bugzilla/>

.. seealso::

   - http://sources.redhat.com/binutils/docs-2.15/binutils/windres.html


windres -h
==========

::


    C:\MinGW\bin>windres -V
    GNU windres (GNU Binutils) 2.20
    Copyright 2009 Free Software Foundation, Inc.
    This program is free software; you may redistribute it under the terms of
    the GNU General Public License version 3 or (at your option) any later version.
    This program has absolutely no warranty.


windres examples
================

::

    http://www.cs.colorado.edu/~main/cs1300/doc/mingwfaq.html
    If you have resources from a resource file (.rc) that also need to be
    added to your executable, you'll need to compile the resource file as
    well as your other source files and include the compiled resources
    when linking to create the executable. Here's an example that shows
    how to compile and link in a resource file named resfile.rc.

    windres -o resfile.o resfile.rc
    gcc -o hello hello.o resfile.o -mwindows


.. seealso::

   - http://blog.stranadurakov.com/tag/windres/
   - http://www.cs.colorado.edu/~main/cs1300/doc/mingwfaq.html


windres syntax
==============

.. seealso::

   - http://www.cygwin.com/cygwin-ug-net/windres.html

::


    What follows is a quick-reference to the syntax windres supports.

    id ACCELERATORS suboptions
    BEG
    "^C" 12
    "Q" 12
    65 12
    65 12 , VIRTKEY ASCII NOINVERT SHIFT CONTROL ALT
    65 12 , VIRTKEY, ASCII, NOINVERT, SHIFT, CONTROL, ALT
    (12 is an acc_id)
    END

    SHIFT, CONTROL, ALT require VIRTKEY


    id BITMAP memflags "filename"
    memflags defaults to MOVEABLE


    id CURSOR memflags "filename"
    memflags defaults to MOVEABLE,DISCARDABLE


    id DIALOG memflags exstyle x,y,width,height styles BEG controls END
    id DIALOGEX memflags exstyle x,y,width,height styles BEG controls END
    id DIALOGEX memflags exstyle x,y,width,height,helpid styles BEG controls END

    memflags defaults to MOVEABLE
    exstyle may be EXSTYLE=number
    styles: CAPTION "string"
        CLASS id
        STYLE  FOO | NOT FOO | (12)
        EXSTYLE number
        FONT number, "name"
        FONT number, "name",weight,italic
        MENU id
        CHARACTERISTICS number
        LANGUAGE number,number
        VERSIONK number
    controls:
        AUTO3STATE params
        AUTOCHECKBOX params
        AUTORADIOBUTTON params
        BEDIT params
        CHECKBOX params
        COMBOBOX params
        CONTROL ["name",] id, class, style, x,y,w,h [,exstyle] [data]
        CONTROL ["name",] id, class, style, x,y,w,h, exstyle, helpid [data]
        CTEXT params
        DEFPUSHBUTTON params
        EDITTEXT params
        GROUPBOX params
        HEDIT params
        ICON ["name",] id, x,y [data]
        ICON ["name",] id, x,y,w,h, style, exstyle [data]
        ICON ["name",] id, x,y,w,h, style, exstyle, helpid [data]
        IEDIT params
        LISTBOX params
        LTEXT params
        PUSHBOX params
        PUSHBUTTON params
        RADIOBUTTON params
        RTEXT params
        SCROLLBAR params
        STATE3 params
        USERBUTTON "string", id, x,y,w,h, style, exstyle
    params:
        ["name",] id, x, y, w, h, [data]
        ["name",] id, x, y, w, h, style [,exstyle] [data]
        ["name",] id, x, y, w, h, style, exstyle, helpid [data]

    [data] is optional BEG (string|number) [,(string|number)] (etc) END


    id FONT memflags "filename"
    memflags defaults to MOVEABLE|DISCARDABLE

    id ICON memflags "filename"
    memflags defaults to MOVEABLE|DISCARDABLE

    LANGUAGE num,num

    id MENU options BEG items END
    items:
        "string", id, flags
        SEPARATOR
        POPUP "string" flags BEG menuitems END
    flags:
        CHECKED
        GRAYED
        HELP
        INACTIVE
        MENUBARBREAK
        MENUBREAK

    id MENUEX suboptions BEG items END
    items:
        MENUITEM "string"
        MENUITEM "string", id
        MENUITEM "string", id, type [,state]
        POPUP "string" BEG items END
        POPUP "string", id BEG items END
        POPUP "string", id, type BEG items END
        POPUP "string", id, type, state [,helpid] BEG items END

    id MESSAGETABLE memflags "filename"
    memflags defaults to MOVEABLE

    id RCDATA suboptions BEG (string|number) [,(string|number)] (etc) END

    STRINGTABLE suboptions BEG strings END
    strings:
        id "string"
        id, "string"

    (User data)
    id id suboptions BEG (string|number) [,(string|number)] (etc) END

    id VERSIONINFO stuffs BEG verblocks END
    stuffs: FILEVERSION num,num,num,num
        PRODUCTVERSION num,num,num,num
        FILEFLAGSMASK num
        FILEOS num
        FILETYPE num
        FILESUBTYPE num
    verblocks:
        BLOCK "StringFileInfo" BEG BLOCK BEG vervals END END
        BLOCK "VarFileInfo" BEG BLOCK BEG vertrans END END
    vervals: VALUE "foo","bar"
    vertrans: VALUE num,num



    suboptions:
        memflags
        CHARACTERISTICS num
        LANGUAGE num,num
        VERSIONK num

    memflags are MOVEABLE/FIXED PURE/IMPURE PRELOAD/LOADONCALL DISCARDABLE


id3Image windows resource file example (resfile.rc)
===================================================


::

    1 VERSIONINFO
     FILEVERSION 0,1,9,0
     PRODUCTVERSION 0,1,9,0
     FILEFLAGSMASK 0x17L
     FILEOS 0x4L
     FILETYPE 0x2L
     FILESUBTYPE 0x0L
    BEGIN
        BLOCK "StringFileInfo"
        BEGIN
            BLOCK "040c04b0"
            BEGIN
                VALUE "CompanyName", "id3 Semiconductors"
                VALUE "FileDescription", "Bibliotheque id3Image.dll"
                VALUE "FileVersion", "0, 1, 9, 0"
                VALUE "InternalName", " id3Image"
                VALUE "LegalCopyright", "Copyright (C) 2009-2010"
                VALUE "OriginalFilename", " id3Image.dll"
                VALUE "ProductName", " id3Image.dll"
                VALUE "ProductVersion", "0, 1, 9, 0"
            END
        END
        BLOCK "VarFileInfo"
        BEGIN
            VALUE "Translation", 0x40c, 1200
        END
    END



.. code-block:: sh

    #/bin/sh
    windres -o resfile.o resfile.rc
    gcc -c -g -o hello.o hello.c
    gcc -o hello.exe hello.o  resfile.o -mwindows













