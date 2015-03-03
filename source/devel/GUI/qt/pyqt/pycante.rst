
.. index::
   pair: pyQt; pycante


.. _pycante:

================
pycante
================


.. seealso::

   - http://pypi.python.org/pypi/pycante/1.0


The hotest way to deal with PyQt.

Allows a unique way to deal with QtDesigner .ui files.

Example
=======

::

    from PyQt4 import QtGui
    import pycante

    class MyWidget(pycante.E("/path/to/file.ui"), AnotherClass);
        pass

    class MyAnotherWidget(pycante.E(QtGui.QFrame), AnotherClass):
        pass

    w0 = MyWidget()
    w1 = MyAnotherWidget()


