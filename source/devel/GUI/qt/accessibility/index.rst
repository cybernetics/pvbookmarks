
.. index::
   Qt (accessibility)

========================
Qt accessibility
========================

.. image:: accessibilityteam.png

.. seealso:: http://blog.didrocks.fr/post/Accessible-Qt-now-in-Oneiric!


When we announced that Unity 2D will be the fallback if you have no required
hardware or driver for unity 3D, one of the compulsory request for that is that
Unity 2D should be accessible.
Even if one of the goal for the cycle is to make Unity fully accessible[1] we
should still consider people needed accessibility and not filling the
requirements for it.

In addition to that, we have now in Oneiric Qt installed by default as
previously decided, and if we want to be toolkit agnostic, we need a good
accessibility story on that toolkit as well… and Qt is known to have a blurry
story about accessibility :)

Unity 2D is written in QML, and so based on Qt technology. So what happens?

It's been already some monthes that Qt people are working on accessibility in Qt
and QML itself, basically working with at-spi2 technology (the same used in GNOME).

Last week, a lot of Qt contributors gathered at the and I had the chance to
spend some time in Berlin there too. The awesome and very friendly
Frederik Gladhorn worked to backport the QML accessible branch (done in a
in-development 4.8 branch, with some nice features of Qt 5 ;)) to cut all non
relevant parts down and backport to a 4.7 branch (as we have 4.7.3 in ubuntu
and will probably stick with 4.7.4 in Oneiric looking at the schedule).

I just started from it, rebased on 4.7.3 and uploaded today (after some staging
test days in the ubuntu-desktop ppa) to Oneiric!

So, if you upgrade your oneiric box and install as well the new qt-at-spi
package (in universe right now, but should be soon land in main), you will get
an accessible Qt and QML! To activate it (it's not activated by the global
configuration over dbus right now), launch Orca or accerciser
(common accessibility tools) and run your Qt application with QT_ACCESSIBILITY=1.

We know right now that it's a little crashy (only with the environment variable set),
but do not hesitate to test! Please report crashes/issues to the Qt package in
launchpad and tag them a11y so that it's easier for us to find and leverage
issues upstream. We can't do it without your helps and we need feedbacks, so
please test. :)

That won't unfortunately make unity 2D instantly accessible though.
Indeed, QML has not right now a standard desktop toolkit[2], every QML project
creates right now its own components, and so, there is no accessiblity magic to
now what to expose or not. Consequently, the unity 2D guys will implement and
test the new property to be set so that Orca (for instance), can read the
widgets content. Accerciser though already introspects unity 2D and other QML
projects content, which means that it seems to work. :)

Thanks again to Frederik, it's a pleasure to work with him and thanks to all
guys working on Qt making that possible! Let's continue working together and
push accessibility in Qt and QML as far as possible.





.. _QML: http://doc.qt.nokia.com/4.7-snapshot/qdeclarativeintroduction.html

