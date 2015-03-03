


.. _announce_qt_5_1_digia:

=====================
Announce Digia Qt 5.1
=====================

.. seealso::

   - http://blog.qt.digia.com/blog/2013/07/03/qt-5-1-released/
   - http://qt-project.org/wiki/New-Features-in-Qt-5.1
   


Published Wednesday July 3rd, 2013 | by Lars Knoll 
===================================================

I’m very happy to announce that Qt 5.1 is now available. 

It has taken us a little more than 6 months since we released Qt 5.0 end of 
last year. 

While we originally planned that Qt 5.1 will mainly focus on bug fixing and 
stability of Qt 5.0, we have actually achieved a lot more. 

The release contains a large amount of new functionality in addition to numerous 
smaller improvements and bug fixes. 
For more information, please have a look at our Qt 5.1 launch page.

Qt 5.1 comes bundled with a freshly released Qt Creator 2.7.2. 

They are available through a new online installer, that allows for automatic 
and seamless upgrades in the future. 

A new version of the Visual Studio Add-in is also available.

We have added many new modules that largely extend the functionality offered 
in 5.0. 

The new Qt Quick Controls and Qt Quick Layouts modules finally offer ‘widgets’ 
for Qt Quick. They contain a set of fully functional controls and layout items 
that greatly simplify the creation of Qt Quick based user interfaces.

Qt Sensors that many already know from the Qt Mobility efforts in Qt 4 has now 
been added to Qt 5.1 supporting Android, Blackberry and iOS. 

A new Qt Serialport add-on allows controlling serial connections on Linux, Mac 
and Windows.


Mobile
=======

.. seealso::

   - http://blog.qt.digia.com/blog/2013/07/03/qt-5-presentation-in-google-play/
   - http://blog.qt.digia.com/blog/2011/02/28/necessitas/
   

In addition to that our work to bring Qt to mobile operating systems is showing 
great results. 

Even though Qt for Android and Qt for iOS are not yet final, and are marked as 
technology previews in this release, they are already very usable for a large 
number of use cases.

Qt for Android supports all Qt modules that are part of 5.1 with the exception 
of Qt Serialport, Qt WebKit and parts of Qt Multimedia. 

Qt for Android also comes with a great integration into Qt Creator that allows 
you to do almost all your development until the point where you want to upload 
the application to Google Play.

Qt for iOS also already supports the same Qt modules as Android does, with the 
exception of Qt Quick 2. 
This is due to limitations in iOS that make it impossible to use V8 as the 
JavaScript engine on this operating system. 
We will provide full Qt Quick support on iOS with Qt 5.2.

You can install some demo applications that show Qt on iOS and Android from the 
App Store and Google Play. 

For Android we have a new Qt Everywhere demo as well as the Qt 5 launch demo 
available in Google Play. 
The blog post about Google Play contains more details about publishing 
Qt applications in Google Play. 

For iOS, we have Sub Attack, a small Qt based game and Qt Quicksand published 
in the app store.

As with any release also this one contains a few issues that we know about 
and probably some more we haven’t yet found. 
All of these will be collected on the Known Issues page in our wiki.

Finally, I hope that you all will enjoy Qt 5.1. I personally believe that 
this release is a great milestone for Qt. 

Qt is now a cross platform toolkit that also spans the major mobile operating 
systems in addition to the desktop platforms and many embedded OSes.

A lot of hard work has gone into making this release happen, and I’d like to 
thank everybody who contributed in one way or another to it. 

Following tradition, here are some pictures of many (but far from all) of 
the people that helped create Qt 5.1.


New modules
===========


Qt Quick Controls (formerly known as Desktop Components)
    A set of reusable UI components. For more details, see the documentation snapshot [doc-snapshot.qt-project.org]

Qt Quick Layouts
    Provides layouts for Qt Quick.

Qt Quick Dialogs
    Provides dialogs for Qt Quick.

Qt X11 Extras
    Platform specific components / APIs for X11.

Qt Sensors
    Provides access to sensor hardware and motion gesture recognition both via QML and C++ interfaces.
    Supports Android, BlackBerry, iOS and Mer platforms.

Qt Serial Port
    Provides an interface for hardware and virtual serial ports.
    
    .. seealso:: http://qt-project.org/wiki/QtSerialPort





