


.. index::
   pair: Qt ; qsettings
   pair: Qt ; Configuration


.. _qsettings:

===============================
Qt Configuration with qsettings
===============================

.. seealso::

   - http://doc.qt.nokia.com/4.7/qsettings.html
   - http://qt-project.org/doc/qt-4.8/qsettings.html
   - http://qt-project.org/doc/qt-5.0/qtcore/qsettings.html



.. contents::
   :depth: 3

Detailed Description
====================

The QSettings class provides persistent platform-independent application settings.

Users normally expect an application to remember its settings (window sizes and
positions, options, etc.) across sessions.

This information is often stored in the system registry on Windows, and in XML
preferences files on Mac OS X.
On Unix systems, in the absence of a standard, many applications (including the
KDE applications) use INI text files.

QSettings is an abstraction around these technologies, enabling you to save and
restore application settings in a portable manner. It also supports custom storage
formats.

QSettings's API is based on QVariant, allowing you to save most value-based
types, such as QString, QRect, and QImage, with the minimum of effort.


QSettings stores settings.
Each setting consists of a QString that specifies the setting's name (the key)
and a QVariant that stores the data associated with the key.

To write a setting, use setValue(). For example::

    settings.setValue("editor/wrapMargin", 68);


QSettings Example code
======================

::


    QSettings settings(QSettings::IniFormat, QSettings::UserScope, "Easytest2Toolbox");
    settings.setIniCodec("UTF-8");

    // On affiche l'emplacement du fichier de configuration
    // ====================================================
    sprintf_s(acComment, 800, "\nSetting.filename=<%s>\n" , settings.fileName().toStdString().c_str());
    CR_Log_Write(acComment, true);


    QString codePIN    = settings.value("PIN").toString();


