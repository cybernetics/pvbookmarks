

.. index::
   pair: Qt; 5
   ! Qt5

.. _qt_5:

============
Qt 5
============


.. seealso::

   - https://qt.gitorious.org/qt/qt5
   - http://qt-project.org/wiki/Qt-5
   - http://qt-project.org/wiki/Category:Developing_with_Qt::Qt-5
   - http://qt-project.org/wiki/Qt-5Features



.. contents::
   :depth: 3

Mission of release
==================

Qt 5 will be the foundation for a new way of developing applications, where
Qt Quick is in the center of Qt.

Qt 5 continues to offer all of the power of native Qt C++, and we don’t want
Qt 5 to be disruptive for existing code developed for Qt 4.

Qt 5 enables highly sophisticated user experiences, offering applications the
full capabilities of OpenGL/OpenGL ES graphics acceleration.

In this respect, Qt 5.0 is a feature-driven release with time-to-market
requirements especially for embedded environments.

This implies that we should keep the scope of Qt 5.0 limited to the essential,
and add more features and add-on modules in the upcoming minor releases.


Qt source code
===============

.. seealso::

   - https://qt.gitorious.org/qt
   - https://qt-project.org/wiki/Get_The_Source
   - https://qt-project.org/wiki/Building-Qt-5-from-Git

Qt 5
-----

Getting the Qt 5 sources is a bit more complicated than Qt 4.x, due to the various
Qt libraries being split into several repositories.

Building Qt 5 from Git has the details on how to `get the Qt 5 sources`_.


Qt5 for android for linux-x86_64
++++++++++++++++++++++++++++++++

.. seealso::

   - http://qt-project.org/wiki/Qt5ForAndroidBuilding


::

    git clone https://git.gitorious.org/qt/qt5.git qt5
    cd qt5
    perl init-repository
    ./configure -developer-build -xplatform android-g++ -nomake tests -nomake examples -android-ndk <path/to/ndk> -android-sdk <path/to/sdk> -android-ndk-host <e.g. linux-x86_64> -skip qttools -skip qttranslations -skip qtwebkit -skip qtserialport -skip qtwebkit-examples
    ANDROID_TARGET_ARCH=armeabi make



Cleaning
+++++++++

To get a really clean tree use:

    git submodule foreach --recursive "git clean -dfx"

since make confclean no longer works from the top-level of the repo.
Getting updates

To update both the ``qt5.git`` repo as well as the submodules to the list of 
revisions that are known to work, run::

    git pull
    git submodule sync
    git submodule update --recursive


.. _`get the Qt 5 sources`:   https://qt-project.org/wiki/Building-Qt-5-from-Git





Qt5 versions
=============

.. toctree::
   :maxdepth: 3

   sub_versions/index








