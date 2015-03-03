



.. index::
   pair: GUI; enaml
   pair: XML; enaml


.. _enaml:

================================
Enaml is not a Markup Language
================================

.. seealso::

   - https://github.com/enthought/enaml


.. contents::
   :depth: 3


Introduction
============

Enaml is a framework for writing declarative user interfaces in Python.

It provides a Yaml-ish/Pythonic syntax language for declaring a ui that binds
and reacts to changes in the user's models.

Code can freely call back and forth between Python and Enaml.

Enaml is heavily inspired by Qt's QML system, but Enaml uses native widgets
(as opposed to drawing on a 2D canvas) and is toolkit independent.

Currently supported/in-development toolkits include Wx and Qt4 via PySide.

Enaml is extensible and makes it extremely easy for the user to define their
own widgets, override existing widgets, create a new backend toolkit, or even
hook the runtime to apply their own expression dependency behavior.

Indeed, about the only thing not hookable is the Enaml language syntax itself.

The enamldoc package provides a Sphinx extension for documenting Enaml objects.


.. _didrik_pinte:

Didrik Pinte
============

.. seealso::

   - http://dpinte.wordpress.com/
   - https://github.com/dpinte


Tutorial
========

.. seealso::

   - http://python-academy.blogspot.fr/2012/09/euroscipy-2012-in-brussels-special.html
   - http://www.euroscipy.org/file/9019?vid=download
   - http://www.euroscipy.org/file/9020?vid=download


How to make writing a GUI program simple was the topic of the tutorial Enaml is
not a Markup Language by Didrik Pinte.

It looks a bit like YAML but allows to create powerful GUIs for wxPython and
PySide/PyQT backends.

There are a lot of goodies in it that help to solve common problems like
two-way communication between data and widgets with very little code,
I mean markup.

- https://github.com/enthought/enaml/downloads




