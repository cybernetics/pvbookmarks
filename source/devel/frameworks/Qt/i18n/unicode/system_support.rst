

.. index::
   pair: qt ; unicode

.. _qt_unicode_system_support:

==========================
Qt unicode system support
==========================

.. warning:: Some of the operating systems and windowing systems that Qt runs on
   only have limited support for Unicode.

The level of support available in the underlying system has some influence on
the support that Qt can provide on those platforms, although in general Qt
applications need not be too concerned with platform-specific limitations.


Unix/X11
========

- Locale-oriented fonts and input methods.
  Qt hides these and provides Unicode input and output.
- Filesystem conventions such as `UTF-8`_ are under development in some Unix variants.
  All Qt file functions allow Unicode, but convert filenames to the local 8-bit encoding,
  as this is the Unix convention (see `QFile::setEncodingFunction()`_ to explore
  alternative encodings).
- File I/O defaults to the local 8-bit encoding, with Unicode options in QTextStream.
- Many Unix distributions contain only partial support for some locales.
  For example, if you have a ``/usr/share/locale/ja_JP.EUC`` directory, this does
  not necessarily mean you can display Japanese text;
  you also need JIS encoded fonts (or Unicode fonts), and the ``/usr/share/locale/ja_JP.EUC``
  directory needs to be complete.
  For best results, use complete locales from your system vendor.


.. _`UTF-8`:  http://www.ietf.org/rfc/rfc2279.txt
.. _`QFile::setEncodingFunction()`:  http://doc.qt.nokia.com/4.6/qfile.html#setEncodingFunction

Windows
=======

- Qt provides full Unicode support, including input methods, fonts, clipboard,
  drag-and-drop and file names.
- File I/O defaults to Latin1, with Unicode options in QTextStream_.
  Note that some Windows programs do not understand big-endian Unicode text files
  even though that is the order prescribed by the Unicode Standard in the absence
  of higher-level protocols.
- Unlike programs written with MFC or plain winlib, Qt programs are portable
  between Windows 98 and Windows NT.
  You do not need different binaries to support Unicode.


.. _QTextStream: http://doc.qt.nokia.com/4.6/qtextstream.html

Mac OS X
========

For details on Mac-specific translation, refer to the Qt/Mac Specific Issues
document here_.

.. _here: http://doc.qt.nokia.com/4.6/mac-differences.html#translating-the-application-menu-and-native-dialogs

