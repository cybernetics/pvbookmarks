

.. index::
   pair: building tool ; Qmake
   pair: Cross-compilation; Qmake
   ! Qmake

.. _qmake:

=====
qmake
=====

.. seealso::

   - http://doc.trolltech.com/3.0/qmake.html
   - http://fr.wikipedia.org/wiki/Qt#qmake
   - http://mingw-cross-env.nongnu.org/#tutorial
   - http://paulf.free.fr/undocumented_qmake.html
   - http://www.qtcentre.org/wiki/index.php?title=Undocumented_qmake
   - http://www.qtcentre.org/wiki/index.php?title=Deploying_Qt_Applications

.. contents::
   :depth: 3
   

http://mingw-cross-env.nongnu.org/#tutorial
===========================================

Step 5c: Cross compile your Project (Qt)
-----------------------------------------

If you have a Qt application, all you have to do is::

    i686-pc-mingw32-qmake
    make

If you are using Qt plugins such as the svg or ico image handlers, you should
also have a look at the Qt documentation about `static plugins`_.


.. _`static plugins`: http://qt.nokia.com/doc/plugins-howto.html#static-plugins


Some thoughts on Qt
===================

.. seealso:: http://ubuntuwicohan.blogspot.com/2011/07/some-thoughts-on-qt-automake-and-cmake.html


