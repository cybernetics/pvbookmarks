
.. index::
   pair: Qt; QDir
   pair: tempPath; QDir
   pair: temp ; Path


.. _qdir:

===================
Qdir
===================

.. seealso::

   - http://qt-project.org/doc/qt-5.0/qtcore/qdir.html


.. contents::
   :depth: 3

QDir example call
==================


::

    #include <QDir>

    const QString data_location = QStandardPaths::writableLocation(QStandardPaths::DataLocation);
    QDir dirDataLocation(data_location);
    if (!dirDataLocation.exists())
    {
       bool mkpath_ok = dirDataLocation.mkpath(data_location);
       if (!mkpath_ok)
       {
           qDebug() << "Pb to mkpath("  << data_location << endl;
       }
    }


QDir::tempPath()
=================

Returns the absolute path of the system's temporary directory.

On Unix/Linux systems this is the path in the TMPDIR environment variable or 
/tmp if TMPDIR is not defined. 

On Windows this is usually the path in the TEMP or TMP environment variable.

On windows 8::

    C:/Users/%USERNAME%/AppData/Local

 

Whether a directory separator is added to the end or not, depends on the 
operating system.

See also temp(), currentPath(), homePath(), and rootPath().





