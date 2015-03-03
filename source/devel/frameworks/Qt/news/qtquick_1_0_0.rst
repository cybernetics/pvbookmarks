

.. index::
   Qt Quick
   Qt Quick Designer !

=====================================================
Qt Quick 1.0 and beyond (or, the post of many links)
=====================================================


.. seealso:: http://labs.qt.nokia.com/2011/03/01/qt-quick-1-0-and-beyond-or-the-post-of-many-links/



UI developers rejoice; Today we are launching Qt Quick 1.0! For those of you who
have been active members of our growing community, there might not be a whole
lot of zero-day news here, except perhaps a bit of clarity on where this path
leads you. For those of you who have only recently discovered how great Qt Quick
is, let me summarize a bit for you;

Qt Quick is a collection of three technologies
==============================================

QtDeclarative
-------------

The native library in Qt deliving native integration and the Qt Quick UI runtime


.. seealso:: http://doc.qt.nokia.com/4.7/qtdeclarative.html

QML
---

the Qt MetaObject Language, allowing declaration of User Interfaces and
Experiences

.. seealso:: http://doc.qt.nokia.com/4.7/qdeclarativeintroduction.html

Qt Creator
----------

support for QML-based projects and code integration.

.. seealso:: http://doc.qt.nokia.com/qtcreator-snapshot/creator-qml-application.html



Qt Quick and the QML language is declarative, using JavaScript in bindings and
property values; so while QML reduces the footprint of your code while providing
blistering performance, keep in mind that JavaScriptCore (the JavaScript engine
we currently use) will require an additional memory overhead.

For the last year, QML and QtDeclarative has been available to both early
adopters as well as mainstream developers through code pushed to gitorious as
well as Qt 4.7.0 and 4.7.1 releases.

Since the first release of QML we have both validated the incredible productivity
benefits of the engine and declarative language, but also received tremendous
help from our community in making sure performance and stability is up to scratch.

A massive thanks to everybody who have embraced and help lift this technology up !

**Today we are launching the final piece of the puzzle; Qt Creator with the
Qt Quick Designer !**

Qt Quick Designer is a WYSIWYG editor for QML UI’s, allowing you to visually
create and arrange your UI’s while staying in perfect sync with your QML code.

No, this does not use a separate generative step like Qt Designer did – but
directly manipulates your QML code.

You can get Qt Creator along with the Qt Quick Designer and all the other
features supporting Qt Quick from our downloads page.

Our team of wizards and magicians in Berlin have been concocting this out in the
open on gitorious.org, so you might have seen it already.
If you’re interested in seeing future developments – please try out the master branch!

In the near-term future we are working on some additional features for Qt Quick
that we think will become useful and increasingly relevant;

This includes use-case specific elements for pinching touch interaction, free
form touch interaction, support for Right-To-Left layouting and many other
features and suggestions that come from the community via bugreports.qt.nokia.com.

We also started last fall to build Qt Quick components for MeeGo and Symbian
– and as you might have seen, we stopped pushing commits to Qt Quick components
for MeeGo a while back.
While work is still continuing at a brisk pace on the MeeGo style, the Symbian
style has now been fully transitioned to gitorious.org, allowing anyone to try
it out on their Symbian3 device. This makes creating new Apps with native look
and feel a lot easier and obsoletes the task of each developer having to creating
reusable elements such as Button’s, ListItem’s and so forth.

Prime your ‘git clone’ and head to http://qt.gitorious.org/qt-components.

To provide feedback you can use bugreports, and if you want to discuss you can
use the mailing list or IRC.

So, what about the desktop you say? Well, the desktop support in Qt is still
going strong; we have our supported platforms that are tried and tested every
day, with new tests and features being added all the time.

You can also use Qt Quick to spice up your traditional desktop application,
with partial QML content that is fluently animated and adds visual
differentiation to your UI.

Or, go all the way like mixd.tv have done. But as mentioned in Volker’s post,
there isn’t a whole lot of innovation happening on the desktop (Yes I know,
Lion will make me eat my words). But, we’re preparing for the future in our
own way and are exploring ways to make Qt Quick components relevant on the
desktop as well. <tease>More on that in an upcoming blog post… </tease>

There’s also even more greatness on the horizon. As graphic acceleration is
becoming more mainstream in devices, the need for a canvas architecture driven
by painter’s algorithm is diminishing, replaced by more direct approaches that
gives the end-user more bang for the buck. Here’s where scenegraph will make y
our UI feel like velvet, and allow even more amazing UI’s based on OpenGL ES.

In addition, we are also exploring ways to simplify 3D creation and integration
of 3D into UI with our Qt/3D integration to QML making it possible for your
grandpa to make a teapot.

So, throwing our glove; Qt Quick 1.0 has landed. Time to conquer the world.



