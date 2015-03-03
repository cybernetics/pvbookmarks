
.. index::
   pair: Qt ; Application Directories


.. _qt_appdirectories:

=========================================
Qt Application directories (QSettings)
=========================================



.. seealso::

   - http://qt-project.org/doc/qt-5/QSettings.html#platform-specific-notes


Detailed Description
======================

The QSettings class provides persistent platform-independent application settings.

Users normally expect an application to remember its settings (window sizes and 
positions, options, etc.) across sessions. 

This information is often stored in the system registry on Windows, and in XML 
preferences files on Mac OS X. 

On Unix systems, in the absence of a standard, many applications (including the 
KDE applications) use INI text files.

QSettings is an abstraction around these technologies, enabling you to save and 
restore application settings in a portable manner. 

It also supports `custom storage formats`_.

.. _`custom storage formats`:   http://qt-project.org/doc/qt-5/qsettings.html#registerFormat
