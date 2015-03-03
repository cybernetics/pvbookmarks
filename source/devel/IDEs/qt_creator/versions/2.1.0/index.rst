
.. _qt_creator_2_1_0:

=============================================
Qt creator  2.1.0
=============================================

.. seealso:: http://labs.qt.nokia.com/2011/03/01/qt-creator-2-1-0-released/

Today we release Qt Creator 2.1.0 as well as the Qt SDK 1.1 beta and Qt 4.7.2 .

We did a few important fixes since the 2.1.0 release candidate, including
adaptions of the mobile application project wizards and deployment related files,
and updated documentation. Together with the Qt SDK 1.1 beta we are now confident
that Qt Creator 2.1.0 is ready to provide a great experience.

The overall agenda for Qt Creator 2.1.0 was enhanced Qt Quick and mobile
application support.

And of course it got lots of improvements in all other areas as well.

For all of you who didn’t follow the pre-releases closely, here are again a few
random things from the release (no specific order, no specific relevance, not
complete):

- Semantic C++ highlighting: Highlighting of types (no “Q…” magic anymore, hurray),
  local variables vs members, virtual methods
- Generic highlighting adds highlighting for various file types based on the
  `Kate highlight definition specification`_
- C++ class view and image viewer contributed by Denis Mingulov
- Outline views for C++ and QML
- Searching for C++ symbols matching a pattern (via advanced find dialog)
- Wizard for adding libraries to pro files, including all the necessary fancy
  magic for include paths and static libs
- Various debugging improvements on all platforms
- Improved QML code editing with a faster code model and a new indenter
- Find usages and improved follow symbols in QML code
- Graphical QML tool bar (that you can get on request) for setting e.g. fonts
  and colors in the QML code editor
- Project wizards for Qt Quick applications that also handle deployment to
  devices, and for custom QML extension plugins
- Mobile application project wizards that provide you with the needed setup for
  Symbian and Maemo, and packaging and deployment
- Various improvements to deployment to Maemo targets and Symbian support
- Click on QObject::connect warnings in application output to jump to the code
- More, more, more


So grab the Qt SDK 1.1 beta release (includes Qt Creator 2.1.0) or get the
Qt Creator-only binary packages from our `download server`_.


.. _`download server`:  http://qt.nokia.com/downloads
.. _`Kate highlight definition specification`:  http://docs.kde.org/stable/en/kdesdk/kate/katehighlight-xml-format.html






