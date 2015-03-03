
.. index::
   pair: Qt Creator; 3.0.0


.. _qt_creator_3_0_0:

=================================================
Qt Creator 3.0.0 ( Thursday December 12th, 2013)
=================================================


.. seealso::

   - http://blog.qt.digia.com/blog/2013/12/12/qt-creator-3-0-released/
   - :ref:`qt_creator_android_5.2`
   - :ref:`qt_5_2`


.. contents::
   :depth: 3



Introduction
=============

Published March 21, 2013 | By Eike Ziller

We are happy to announce the Qt Creator 2.7.0 release today, which comes with
loads of new features, improvements and bug fixes.

C++ support
-----------

C++ support in Qt Creator got even more improvements for C++11, like handling of:

- alignof,
- alignas and noexcept,
- brace initializers,
- and more lambda fixes.

Also, if Qt Creator cannot find out if your tool chain expects C++11 or C++98/03,
it defaults to C++11 now, for a better out of the box experience.

Qt Quick2
---------

Also there are improvements on the refactoring actions side, for example quick
fixes for adding getters and setters for class members, and for adding the getters
and setters that are specified in a Q_PROPERTY.

QML support got lots of fixes for Qt Quick 2 in the code editor, and there was a
lot of work done to make Qt Quick Designer work with Qt Quick 2.

Please note though that the Qt Creator standalone binary packages are based on
Qt 4 and do not provide the necessary Qt Quick 2 based external worker tool
(which of course needs to be built with Qt 5).

For now you either need to compile Qt Creator with Qt 5 yourself, or at least
compile the qml2puppet yourself with Qt 5 (qt-creator/share/qtcreator/qml/qmlpuppet/qml2puppet)
and put that into qtbase/bin of your Qt 5 install (and make sure that your project
uses a Kit that uses that Qt version).

Or you wait for Qt 5.0.2 packages that will contain a Qt 5 based build of
Qt Creator again.

Blackberry
-----------

On the BlackBerry support side, we got a new settings page, which allows to
easily generate Kits (and the necessary Qt version and compiler information)
from an NDK path, and helps users with registering and generating developer
certificates and other files that are needed for uploading apps to their devices.

Also the editor for bar descriptor files, which define application appearance
and behavior, can now be switched between editing the pure XML and a graphical
editor. There were many other improvements as well, for example regarding debugging
on devices.

QBS build tool
---------------

Experimental support for the (also experimental) QBS build tool was added to
Qt Creator, and the binary packages now also contain it (in contrast to the
prereleases), though it is disabled by default.

To enable it, open “Help > About Plugins” (on Mac it’s in “Qt Creator > About Plugins”),
tick the QbsProjectManager, and restart Qt Creator, no further downloads/installations
are necessary.

The Qt Creator sources themselves also come with QBS project files, if you were
wondering which project you can open with it now ;) . If you want to build
Qt Creator with QBS support yourself, you first need to pull in its sources:
Qt Creator’s git repository now has QBS as a submodule, so::

     git submodule update –init && qmake -r && make”


in the top-level directory of your git checkout should be all you need to do.

Of course this is only a very small part of the actual improvements that were done,
but talking about all of them – Debugging, Android, VCS, FakeVim, just to mention
a few – would be beyond the scope of the blog post.

Even bookmarks got some love this time, thanks Vasiliy Sorokin :) .

If you want to know more about changes in this version, you might want to have
a look at our change log.

.. _`changes file`:  https://qt.gitorious.org/qt-creator/qt-creator/blobs/2.7/dist/changes-2.7.0



   
   
