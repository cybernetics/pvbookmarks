
.. index::
   pair: Qt Creator; 2.5.0


.. _qt_creator_2_5_0:

=============================================
Qt Creator 2.5.0 (May 9, 2012)
=============================================


.. seealso::

   - http://qt-project.org/news/view/qt-creator-2.5.0-released
   - http://labs.qt.nokia.com/2012/05/09/qt-creator-2-5-0-released/



.. contents::
   :depth: 3



The Qt tools team in Berlin has released a new stable version of Qt Creator today.

You can read about all the great improvements and features on Eike’s release blog.
Or just get it straight away from our downloads page.


http://labs.qt.nokia.com/2012/05/09/qt-creator-2-5-0-released/
===============================================================


The Qt Creator 2.5.0 final has been released! There are lots of new features and
improvements in this release, I’ll highlight a few here, some others are probably
already mentioned in our beta blog post, and you’ll find a more complete list
in our `changes file`_.

So, new features and improvements include but are not limited to:

- You can repeat a recent search with the same parameters with a simple click on
  “Search Again”
- “Execute” Locator filter lets you run arbitrary commands in a shell from Qt Creator
  (“! <some command>”) (thanks to Yuchen Deng!)
- Experimental plugin that shows “TODO” items from your sources (thanks to Dmitry
  Savchenko and Vasiliy Sorokin!)
- Experimental plugin for autotools based projects (thanks to Patricia Santana
  Cruz and Openismus GmbH!)
- Mac OS X Lion users will we happy to know that QTCREATORBUG-6222 which prevented
  adding some Qt Versions has finally been fixed
- A very basic version of a C++ refactoring action that adds an #include for an
  unknown identifier has been added (move cursor on identifier, press Alt+Return
  (Option+Return on Mac OS X))
- A very basic version of a C++ “extract method” refactoring action
- Improved support of C++11 (nullptr, constexpr, static_assert, noexcept, inline
  namespaces, auto, lambdas)
- Rearrange C++ method arguments (thanks to Bojan Petrovic!)
- New hints and warnings for QML code, including an option to prevent them for
  specific lines (with a special comment)


.. _`changes file`:  http://qt.gitorious.org/qt-creator/qt-creator/blobs/2.5/dist/changes-2.5.0
