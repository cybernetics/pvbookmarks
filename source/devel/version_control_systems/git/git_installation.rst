
.. index::
   pair: git; installation

=================
git installation
=================


.. seealso::

   - http://developer.qt.nokia.com/wiki/Git_Installation


Git on Mac OS X
================

On Mac OS X, you can get Git using MacPorts [macports.org] .

After installing MacPorts, do:

::

    sudo port selfupdate
    sudo port sync
    sudo port install git-core
    add /opt/local/bin to your PATH

Note that this also adds another ssh into your path. You can safely remove
:file:/opt/local/bin/ssh*, :file:/opt/local/bin/scp,  :file:/opt/local/bin/sftp
(especially if you want to use Leopard’s built-in ssh-agent).

Git on Windows
==============

.. seealso:: http://code.google.com/p/msysgit/

For Windows there exists a convenient installer as part of the MSysGit project:

.. note:: When the installer presents you with the option of how to put Git
   into your PATH choose the third option of putting Git and all its tools into
   your path!


Git on Linux
============

All major Linux distributions offer up-to-date packages of Git.

Use your distribution specific package manager to install Git.

Note that on Debian based distributions the Git package is actually called ``git-core``.


Building Git from Source
=========================

Git is easy to build from source. Just :

- download the latest release from  http://git.or.cz/ [git.or.cz],
- unpack the sources,
- run configure
- followed by make followed by make install. This will install it locally into
  your home directory, the binaries end up in $HOME/bin.

Dependency list (Kubuntu 8.4):

- libzlcore-dev
- libssl-dev
- libcurl4-openssl-dev
- libexpat1-dev
- tclx8.3
- asciidoc








