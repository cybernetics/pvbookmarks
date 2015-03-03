


.. index::
   pair: Pkg-config; Qt

.. _pkg_conf_qt:

==================
Pkg-config with Qt
==================


.. seealso::

   - https://www.developer.nokia.com/Community/Wiki/Using_pkg-config_with_qmake

.. contents::
   :depth: 3


How to use pkg-config with qmake
=================================

Qt Project files (.pro) contain several variables used by the compiler, such as
LIBS and INCLUDE.

These variables contain the name and the location of the library required by the
linker and the location of the include files used by the compiler.

When qmake creates a Makefile, it takes into account the predefined value of
LIBS and INCLUDE coming from a Qt mkspec.

The mkspec files are platform specific and they are stored in /usr/share/qt4/mkspecs/platform_name.

Anyway, Mkspecs files just keep Qt libs data. Therefore, a developer who wants
to add new libraries has to tell to the compiler where the new libs are located.

This can be easily done by adding 2 lines to the project file

::

    unix {
        CONFIG += link_pkgconfig
        PKGCONFIG += <pc_file_without_extension>
    }
