
.. index::
   pair: python Qt; Pyside
   ! PySide


.. _pyside:

=======
Pyside
=======

.. seealso::

   - https://qt-project.org/wiki/Get-PySide
   - http://qt.gitorious.org/pyside
   - http://qt-project.org/wiki/PySide   
   - :ref:`pyqt`
   - http://pyqt.developpez.com/
   - http://www.qtrac.eu/pyqtbook.html#pyside
   - :ref:`watchvideo`


.. contents::
   :depth: 3

pyside-examples
===============

::

    git clone git://gitorious.org/pyside/pyside-examples.git



Sites
=====



http://www.pyside.org/docs/pseps/psep-0101.html
===============================================

PyQt4 provides two different (and incompatible) APIs. API 1 is the original
API and the one supported by PySide. API 2 is a new Python 3-specific API
that is much more Pythonic. This PSEP proposes that PySide adopt PyQt4's
API 2 for PySide.


Rationale
---------

PyQt4 provides two different (and incompatbile) APIs [1]. API 1 is useful for
those using PyQt4 to prototype C++/Qt programs since it is very close to the
C++/Qt API. However, for those who want to create Python Qt programs in their
own right, and especially for existing Python programmers, API 1 is cumbersome
and un-Pythonic when it comes to handling QStrings and QVariants, both of
which are used a lot.

If PySide were to support API 2, it will make PySide much more attractive
to Python 3 programmers.

Also, supporting API 2 will mean that existing Python 3/PyQt4 programs
that use API 2 by default will be able to switch to PySide.

One key purpose of API 2 is to avoid the need for Python programmers to
have to worry or even know about QString or QVariant. For Python
programmers str is the string they are used to so translation to/from
QString should be transparent and automatic. Similarly, why should Python
programmers have to know about QVariant when that is a C++ workaround
for C++'s lack of support for duck typing etc.? Again, translation to/from
QVariant should be transparent and automatic. API 2 achieves this and
eliminates QString and (to some extent) QVariant.



Compiling pyside
================

::

    Hi,

    2011/3/10 Mark Summerfield <list@qtrac.plus.com>:
    > Hi,
    >
    > When I build PySide on debian testing it finds the system's Qt 4.6.3.
    >
    > However, I'd like it to use my locally built $HOME/opt/qt470, but I
    > don't know how to tell cmake to do that. Can anyone tell me?
    >


You can try to set the cmake parameter -DQT_QMAKE_EXECUTABLE=<path to qmake>
for example -DQT_QMAKE_EXECUTABLE=$HOME/opt/qt470/bin/qmake

Regards


GUI compiling with pyside-uic
=============================


.. seealso:: http://www.qtrac.eu/pyqtbook.html#pyside

::

    Hi,
    2011/5/15 Thorsten Kampe <thorsten@thorstenkampe.de>:
    > I've ported a simple PyQt4 (4.8.4) application to PySide 1.0.0 according
    > to http://www.qtrac.eu/pyqtbook.html#pyside. This works pretty well,
    > except that I cannot use the PyQt4 UI code generator generated UI file:

You should use the utility "pyside-uic" instead of "pyuic4" if you
want to use PySide. It's basically the same utility, but for PySide.


PySide news
===========

.. toctree::
   :maxdepth: 4

   news/index


