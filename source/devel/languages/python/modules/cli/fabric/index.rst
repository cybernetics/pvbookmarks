

.. index::
   pair: CLI ; Fabric
   pair: Fabfile ; Fabric
   ! Fabric
   ! Fabfile

.. _fabric:

=================
Fabric (Fabfile)
=================


.. seealso::

   - http://fabfile.org
   - https://github.com/bitprophet   
   - http://www.debian-administration.org/article/671/A_simple_introduction_to_fabric
   - :ref:`Pyinvoke`


.. contents::
   :depth: 3

Introduction
=============

Fabric is a Python library and command-line tool for streamlining the
use of SSH for application deployment or systems administration tasks.

It provides a basic suite of operations for executing local or remote shell
commands (normally or via ``sudo``) and uploading/downloading files, as well as
auxiliary functionality such as prompting the running user for input, or
aborting execution.

Typical use involves creating a Python module containing one or more functions,
then executing them via the ``fab`` command-line tool. Below is a small but
complete "fabfile" containing a single task::

    from fabric.api import run

    def host_type():
        run('uname -s')

Once a task is defined, it may be run on one or more servers, like so::

    $ fab -H localhost,linuxbox host_type
    [localhost] run: uname -s
    [localhost] out: Darwin
    [linuxbox] run: uname -s
    [linuxbox] out: Linux

    Done.
    Disconnecting from localhost... done.
    Disconnecting from linuxbox... done.

In addition to use via the ``fab`` tool, Fabric's components may be imported
into other Python code, providing a Pythonic interface to the SSH protocol
suite at a higher level than that provided by e.g. Paramiko (which
Fabric itself leverages.)

Fabric source code
==================

.. seealso::

   - https://github.com/fabric/fabric


Fabric versions
================

.. toctree::
   :maxdepth: 3

   versions/index



Projects using fabric
=====================

.. toctree::
   :maxdepth: 3

   projects_using_fabric/index


Fabric tips
============

.. toctree::
   :maxdepth: 3

   tips/index

