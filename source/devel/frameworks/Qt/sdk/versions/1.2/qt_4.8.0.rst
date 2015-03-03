
.. index::
   pair: Qt ; 4.8.0


.. _qt_4.8.0:

=============================
Qt 4.8.0 , December 15, 2011
=============================

.. seealso::

   - http://labs.qt.nokia.com/2011/12/15/qt-4-8-0-released/
   - http://developer.qt.nokia.com/doc/qt-4.8/qt4-8-intro.html


Posted by Sinan Tanilkan on December 15, 2011 · 101 comments

Qt has reached another important evolutionary milestone today. We are very proud
to announce that Qt 4.8.0 has now been released. Many people have worked long
and hard to deliver Qt 4.8.0.

Today that hard work reaches final release maturity, and we are celebrating!

Featuring Qt Platform Abstraction, threaded OpenGL support, multithreaded HTTP
and optimized file system access, Qt 4.8.0 can be downloaded as binary or source
packages


Content
=======

Those of you that have been testing and using Qt 4.8 through its earlier stages
will know the key benefits it brings.

If you haven’t been following it, here are some key features that are new in
Qt 4.8.0:



Qt Quick 1.1
============

introduces new changes such as new properties and better performance.

- Right-To-Left text support
- Improved image caching
- Text input improvements - Support for split-screen virtual keyboard
- PinchArea Element - enables simple pinch gesture handling
- New properties for QML Elements.


Qt Platform Abstraction (QPA)  -- Lighthouse
============================================

QPA restructures the GUI stack to enable easier porting of Qt to different
windowing systems and devices. More info on: Lighthouse has grown up now.


Threaded OpenGL support
=======================

Enables those of us that are not OpenGL-ninjas to render OpenGL from more than
one thread concurrently. More info on: Threaded OpenGL in 4.8.


Multithreaded HTTP
==================

HTTP requests are now handled in a separate thread by default.

This should make application guis smoother, as networking will no longer use
the main event loop.


Optimized file system acces
===========================

The file system stack received some heavy lifting under the hood.

The result is better I/O performance, achieved by reducing the number of system
calls performed for I/O and by better use of cached data, when available.

The improvements in performance can be seen across all platforms.

Qt 4.8.0 ships with QtWebKit 2.2.1.

More details of the major changes can be found in the Qt 4.8 beta blog post.


Qt 4.8 introduces changes to the Qt API
=======================================


C++ 11 support
---------------


**Qt supports some of the features of the C++11 standard**

- QList, QVector and QStringList can be initialized with initializer lists.
- Most of the tool classes have a move operator.
- It is possible to use lambda functions in some of the QtConcurrent_ functions.


.. _QtConcurrent:  http://developer.qt.nokia.com/doc/qt-4.8/qtconcurrent.html

Localization API
================

Changes to the Localization APIs include improvements to QLocale and more
support for different language code formats.

- QLocale::quoteString() - for localized quotes
- QLocale::createSeparatedList() - for localized list separation (e.g. "1, 2 and 3")
- QLocale::bcp47Name() - for locale names in the canonical form according to RFC 5646 - BCP47
- QLocale::matchingLocales() - to get a list of locales that match a criteria - e.g. a list of locales that use French language.
- QLocale::firstDayOfWeek()
- QLocale::weekdays()
- QLocale::currencySymbol()
- QLocale::toCurrencyString() - number formatting for currencies
- QLocale::uiLanguages()
- QLocale::nativeLanguageName()
- QLocale::nativeCountryName()


IP Multicast API
----------------

Multithreaded HTTP
------------------

QThreadLocalStorage
-------------------

can now store simple objects in addition to pointers




