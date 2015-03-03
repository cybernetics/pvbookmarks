
.. index::
   pair: Documentation ; doxygen
   pair: Analyseur; Code C

.. _doxygen:

=======================
Doxygen
=======================


.. seealso::

   - http://www.stack.nl/~dimitri/doxygen/index.html
   - https://github.com/doxygen/doxygen.git
   - https://github.com/doxygen/doxygen
   - :ref:`doxygen_sphinx_extension`


.. figure:: Doxygen_logo.png

   *Doxygen logo*


.. contents::
   :depth: 3


Introduction
=============

``Doxygen`` is a documentation system for C++, C, Java, Objective-C, 
Python, IDL(Corba and Microsoft flavors), Fortran, VHDL, PHP, C#, and 
to some extent D.

It can help you in three ways:

- It can generate an on-line documentation browser (in HTML) and/or an off-line
  reference manual (in $\mbox{\LaTeX}$) from a set of documented source files.
  There is also support for generating output in RTF (MS-Word), PostScript,
  hyperlinked PDF, compressed HTML, and Unix man pages.
  The documentation is extracted directly from the sources, which makes it much
  easier to keep the documentation consistent with the source code.
- You can configure doxygen to extract the code structure from undocumented
  source files. This is very useful to quickly find your way in large source
  distributions.
  You can also visualize the relations between the various elements by means of
  include dependency graphs, inheritance diagrams, and collaboration diagrams,
  which are all generated automatically.
- You can even *abuse* doxygen for creating normal documentation (as I did for
  this manual).

Doxygen is developed under Linux and Mac OS X, but is set-up to be highly portable.
As a result, it runs on most other Unix flavors as well. Furthermore, executables
for Windows are available.

Furthermore, executables for Windows are available.

Example
=======

::

    ///
    /// <summary>
    /// CR_RFID_DecouvrirLecteurs() Retourne la liste des lecteurs PS/SC de type
    /// sous la forme d une liste de noms de la forme : "CodeRousseau RFID".
    /// </summary>
    /// <param name="ppListeNomsLecteursRFID"> [out] pointeur sur une liste de noms de lecteurs RFID.</param>.
    /// <remarks>
    /// </remarks>
    /// <returns>
    /// - COMMAND_SUCCESS: La commande s'est bien passee.
    /// - COMMAND_FAILED: La commande a echoue.
    /// </returns>
    extern DWORD CR_RFID_DecouvrirLecteurs(ST_LIST_STRING **ppListeNomsLecteursRFID);


Doxygen source code
====================

.. seealso::

   - https://github.com/doxygen/doxygen
   - https://github.com/doxygen/doxygen.git
   
   
In May 2013, Doxygen moved from subversion to git hosted at github::

    https://github.com/doxygen/doxygen

Enjoy,

Dimitri van Heesch (dimitri at stack.nl)

 
Issues, bugs, requests, ideas
=============================

.. seealso

   - https://bugzilla.gnome.org/enter_bug.cgi?product=doxygen
   

Use the bug tracker to report bugs:

* current list:
    * Bugzilla_
    
* Submit a new bug or feature request 
    * `Enter bug`_ 
   

.. _Bugzilla : https://bugzilla.gnome.org/buglist.cgi?product=doxygen&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED
.. _`Enter bug` : https://bugzilla.gnome.org/enter_bug.cgi?product=doxygen

Projects using doxygen
======================

.. toctree::
   :maxdepth: 4

   projects_using_doxygen/index



Doxygen formats
================

.. toctree::
   :maxdepth: 4

   formats/index


Doxygen versions
================

.. toctree::
   :maxdepth: 4

   versions/index




