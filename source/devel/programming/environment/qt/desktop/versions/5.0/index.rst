


.. _qt_desktop_services_versions_5.0:

===========================================
Qt Desktopservices, QSettings versions 5.0
===========================================

.. seealso::

   - https://qt-project.org/doc/qt-5.0/qtcore/qstandardpaths.html



.. contents::
   :depth: 3





.. qt_standard_path:

QStandardPaths
=====================


.. seealso::

   - https://qt-project.org/forums/viewthread/22982
   - https://qt-project.org/doc/qt-5.0/qtgui/qdesktopservices-obsolete.html


I’m trying to port my desktop application to Qt 5, stumbled upon::

    QDesktopServices::storageLocation( QDesktopServices::DataLocation );

Can’t find a substitute in Qt 5, please advise.

Reply
------


You can use QStandardPaths_ as a replacement for QDesktopServices


.. _QStandardPaths:  https://qt-project.org/doc/qt-5.0/qtcore/qstandardpaths.html
