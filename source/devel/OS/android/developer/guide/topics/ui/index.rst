

.. index::
   pair: Android; User Interface

.. _android_ui:


============================
Android ui (User Interface)
============================

.. seealso::

   - https://developer.android.com/guide/topics/ui/index.html
   - https://developer.android.com/guide/topics/ui/overview.html


.. contents::
   :depth: 3

Introduction
============

Your app's user interface is everything that the user can see and interact with.

Android provides a variety of pre-build UI components such as structured layout
objects and UI controls that allow you to build the graphical user interface for
your app.

Android also provides other UI modules for special interfaces such as dialogs,
notifications, and menus.



Layout
======

.. seealso:: https://developer.android.com/guide/topics/ui/declaring-layout.html


A layout defines the visual structure for a user interface, such as the UI for
an activity or app widget. You can declare a layout in two ways:


- Declare UI elements in XML. Android provides a straightforward XML vocabulary
  that corresponds to the View classes and subclasses, such as those for widgets
  and layouts.
- Instantiate layout elements at runtime. Your application can create View and
  ViewGroup objects (and manipulate their properties) programmatically.



Styles/Themes
=============


.. seealso::

   - https://developer.android.com/guide/topics/ui/themes.html

A style is a collection of properties that specify the look and format for a
View or window.

A style can specify properties such as height, padding, font color, font size,
background color, and much more.

A style is defined in an XML resource that is separate from the XML that specifies
the layout.

Styles in Android share a similar philosophy to cascading stylesheets in web
design—they allow you to separate the design from the content.


Animation
=========
.. seealso::

   - https://developer.android.com/guide/topics/graphics/index.html

Android provides a variety of powerful APIs for applying animation to UI elements
and drawing custom 2D and 3D graphics.

The sections below provide an overview of the APIs and system capabilities
available and help you decide with approach is best for your needs.
