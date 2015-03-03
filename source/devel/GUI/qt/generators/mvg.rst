
.. index::
   Qt mvg Dialog generator for Qt

========================
Dialog generator for Qt
========================

.. seealso:: http://www.holgerschurig.de/projects/mvg.html#dialog_code_generation


Qt's Model/View Programming might be extremely flexibly.

This flexibility comes at the price of tedious programming, even for simple case.

What could be simple than having a struct filed with data, an array of such
struct (either C++ array, or QList, or QVector, whatever), and a widget where
you can see all those items and edit them.

A simple task, needed in many programs, no ?

Yet is is quite tedious to implement this in Qt 4.x:

- You have to hand-code an editor (Dialog) for it.
- You have to hand-code a model for it.
- You have to hand-code a view for it, or re-use QTableView.

mvg.py is a Model-View Generator and is a tool to solve this.

