

.. index::
   pair: Doxygen ; Installation)


.. _doxygen_installation_on_linux:

==================================
doxygen installation  on GNU/Linux
==================================

.. contents::
   :depth: 3

.. _doxygen_gnu_linux_installation:

Prerequisite
============

We must be **root** to install the doxygen library (for centos).

Under ubuntu, we must be root only for make install.


Install in /opt/doxygen/1.7.2
=============================


cd <yourpath>/doxygen-1.7.2
----------------------------


./configure --prefix /opt/doxygen/1.7.2 --with-doxywizard
---------------------------------------------------------

Results

::

    cd /tmp/doxygen-1.7.2
    ./configure --prefix /opt/doxygen/1.7.2 --with-doxywizard
    make

other option for configure: --enable-debug-log --enable-examples-build


sudo make install
-----------------

Make the link to the current doxygen version
============================================

::

    su - root
    cd /opt/doxygen
    ln -s 1.7.2 current



export PATH=/opt/doxygen/current/bin:$PATH

