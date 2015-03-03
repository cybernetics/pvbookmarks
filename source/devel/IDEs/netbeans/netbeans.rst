.. module:: Netbeans
    :synopsis: Netbeans IDE for C development


.. index::
   pair: netbeans ; IDE

.. _c_netbeans_ide:

==================
The C Netbeans IDE
==================


`NetBeans <http://en.wikipedia.org/wiki/NetBeans>`_ refers to both a platform for the
development of applications for the network (using Java, JavaScript, PHP, `Python <http://www.python.org>`_,
Ruby, Groovy, `C <http://en.wikipedia.org/wiki/C_%28programming_language%29>`_
, and C++), and an integrated development environment (IDE) developed using the NetBeans Platform.
The NetBeans IDE is an open-source integrated development environment written entirely in Java using the NetBeans Platform.
NetBeans IDE supports development of all Java application types (Java SE, web, EJB and mobile applications) out of the box.
Among other features are an `Ant-based <http://en.wikipedia.org/wiki/Apache_Ant>`_  project system, version control
(supporting CVS, Subversion, Mercurial and Clearcase) and refactoring.

.. seealso::

    - http://netbeans.org/downloads/index.html
    - http://fr.wikipedia.org/wiki/Netbeans
    - http://code.google.com/p/winant/


.. index::
   CDDL Sun's Common  Development and Distribution License
   Sun's Common  Development and Distribution License (CDDL)
   License netbeans

License
=======

From July 2006 through 2007, NetBeans IDE was licensed under `Sun's`_ Common
Development and Distribution License (CDDL_), a license based on the Mozilla
Public License (MPL).

In October 2007, Sun announced that NetBeans would henceforth be offered
under a dual license of the CDDL and the GPL version 2 licenses, with the GPL
linking exception for GNU Classpath.

.. _CDDL: http://en.wikipedia.org/wiki/Common_Development_and_Distribution_License
.. _`Sun's`: http://fr.wikipedia.org/wiki/Sun_Microsystems



Netbeans tool collection
========================

The free GCC tools use are the :ref:`mingw`.


.. index::
   windows resource file


Netbeans windows version resource
=================================

.. seealso:: :ref:`windres`


To add the version of the id3Image.dll file we must:

- create a resource file: 'windows_resource/version.rc'

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
                VALUE "FileDescription", "Bibliotheque id3Image.dll "
                VALUE "FileVersion", "0, 1, 9, 0"
                VALUE "InternalName", "id3Image"
                VALUE "LegalCopyright", "Copyright (C) 2009-2010"
                VALUE "OriginalFilename", "id3Image.dll"
                VALUE "ProductName", " id3Image.dll"
                VALUE "ProductVersion", "0, 1, 9, 0"
            END
        END
        BLOCK "VarFileInfo"
        BEGIN
            VALUE "Translation", 0x40c, 1200
        END
    END

- compile the version.rc file with the :ref:`windres`

.. code-block:: sh

    #/bin/sh
    windres -o version.o version.rc


- link against the id3Image.dll

::

    -Wl,--output-def,${CND_DISTDIR}/${CND_CONF}/id3Image.def, --out-implib,${CND_DISTDIR}/${CND_CONF}/id3Image.a version.o



The id3Image.dll with the version information
---------------------------------------------

















