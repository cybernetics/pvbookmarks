

.. index::
   pair: Virtualenvwrapper; Windows
   pair: pywin; py.exe


.. _virtualenvwrapper_windows:

============================
Virtualenvwrapper On windows
============================

.. seealso::

   - http://pypi.python.org/pypi/virtualenvwrapper-win
   - https://pytools.codeplex.com/wikipage?title=Virutal%20Env


.. contents::
   :depth: 3

Introduction
============

.. seealso:: https://raw.github.com/davidmarble/virtualenvwrapper-win/master/README.rst

This is a port of Doug Hellmann's 'virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_
to Windows batch scripts.

The idea behind virtualenvwrapper is to ease usage of Ian Bicking's virtualenv,
a tool for creating isolated Python virtual environments, each with their own
libraries and site-packages.

These should work on any version of Windows (Windows XP, Windows Vista, Windows 7).
They do not require Powershell.


Installation
=============


Optional: pywin python version switcher (not included)
-------------------------------------------------------

.. seealso:: https://github.com/davidmarble/pywin

If you use several versions of python, you can switch between them using 
a separate project pywin. 

It's a lightweight python 2.5-3.3 launcher and switcher I wrote for the 
Windows command line and MSYS/MINGW32. 

It's similar to the py.exe launcher/switcher available in python 3.3, but 
written with basic Windows batch scripts and a shell script for MSYS/MINGW32 
support. I use bash and command line shell tools from msysgit, based on 
MSYS/MINGW32, to do most of my python development on Windows.



**For Windows only**

Installed scripts are placed in ``%PYTHONHOME%\Scripts``.

To install, run the following::

    pip install virtualenvwrapper-win
    pyassoc

or download the source and run the following::

    python setup.py install
    pyassoc

**Optional**: Add an environment variable WORKON_HOME to specify the path to store environments. By default, this is ``%USERPROFILE%\Envs``.

**Note**: ``pyassoc``
    Note that the batch script ``pyassoc`` associates .py files with ``python.bat``,
    a simple batch file that calls the right ``python.exe`` based on whether you
    have an active virtualenv. This allows you to call python scripts from the
    command line and have the right python interpreter invoked.
    Take a look at the source -- it's incredibly simple but the best way I've
    found to handle conditional association of a file extension.
    **You will need to run this for each user, or alternatively run it in an
    elevated command prompt once.**

Main Commands
-------------


``mkvirtualenv <name>``
    Create a new virtualenv environment named *<name>*.  The environment will
    be created in WORKON_HOME.

``lsvirtualenv``
    List all of the enviornments stored in WORKON_HOME.

``rmvirtualenv <name>``
    Remove the environment *<name>*. Uses ``folder_delete.bat``.

``workon [<name>]``
    If *<name>* is specified, activate the environment named *<name>* (change
    the working virtualenv to *<name>*). If a project directory has been defined,
    we will change into it.
    If no argument is specified, list the available environments.

``deactivate``
    Deactivate the working virtualenv and switch back to the default system
    Python.

``add2virtualenv <full_path>``
    If a virtualenv environment is active, appends *<full_path>* to
    ``virtualenv_path_extensions.pth`` inside the environment's site-packages,
    which effectively adds *<full_path>* to the environment's PYTHONPATH.
    If a virtualenv environment is not active, appends *<full_path>* to
    ``virtualenv_path_extensions.pth`` inside the default Python's
    site-packages.

Convenience Commands
--------------------
``cdproject``
    If a virtualenv environment is active and a projectdir has been defined,
    change the current working directory to active virtualenv's project directory.
    ``cd-`` will return you to the last directory you were in before calling
    ``cdproject``.

``cdsitepackages``
    If a virtualenv environment is active, change the current working
    directory to the active virtualenv's site-packages directory. If
    a virtualenv environment is not active, change the current working
    directory to the default Python's site-packages directory. ``cd-``
    will return you to the last directory you were in before calling
    ``cdsitepackages``.

``cdvirtualenv``
    If a virtualenv environment is active, change the current working
    directory to the active virtualenv base directory. If a virtualenv
    environment is not active, change the current working directory to
    the base directory of the default Python. ``cd-`` will return you
    to the last directory you were in before calling ``cdvirtualenv``.

``lssitepackages``
    If a virtualenv environment is active, list that environment's
    site-packages. If a virtualenv environment is not active, list the
    default Python's site-packages. Output includes a basic listing of
    the site-packages directory, the contents of easy-install.pth,
    and the contents of virtualenv_path_extensions.pth (used by
    ``add2virtualenv``).

``setprojectdir <full_path>``
    If a virtualenv environment is active, define *<full_path>* as project
    directory containing the source code.  This allows the use of ``cdproject``
    to change the working directory. In addition, the directory will be
    added to the environment using ``add2virtualenv``.

``toggleglobalsitepackages``
    If a virtualenv environment is active, toggle between having the
    global site-packages in the PYTHONPATH or just the virtualenv's
    site-packages.

``whereis <file>``
    A batch file used in many of the scripts above. Returns directory locations
    of `file` and `file` with any executable extensions. So you can call
    ``whereis python`` to find all executables starting with ``python`` or
    ``whereis python.exe`` for an exact match.


Virtualenvwrapper windows source code
=====================================

.. seealso::

   - https://github.com/davidmarble/virtualenvwrapper-win/



Virtualenvwrapper upgrade
=========================

::


    C:\> pip install virtualenvwrapper-win --upgrade
    Downloading/unpacking virtualenvwrapper-win from http://pypi.python.org/packages
    /source/v/virtualenvwrapper-win/virtualenvwrapper-win-1.0.9.zip#md5=3f79c140b655
    ec0a2b43374d3c226a5f
    Downloading virtualenvwrapper-win-1.0.9.zip
    Running setup.py egg_info for package virtualenvwrapper-win

    Downloading/unpacking virtualenv from http://pypi.python.org/packages/source/v/v
    irtualenv/virtualenv-1.8.4.tar.gz#md5=1c7e56a7f895b2e71558f96e365ee7a7 (from vir
    tualenvwrapper-win)
    Downloading virtualenv-1.8.4.tar.gz (1.9Mb): 1.9Mb downloaded
    Running setup.py egg_info for package virtualenv

    Installing collected packages: virtualenvwrapper-win, virtualenv
    Found existing installation: virtualenvwrapper-win 1.0.2
    Uninstalling virtualenvwrapper-win:
    Successfully uninstalled virtualenvwrapper-win
    Running setup.py install for virtualenvwrapper-win

    Found existing installation: virtualenv 1.7.1.2
    Uninstalling virtualenv:
    Successfully uninstalled virtualenv
    Running setup.py install for virtualenv

    Installing virtualenv-script.py script to c:\python27\Scripts
    Installing virtualenv.exe script to c:\python27\Scripts
    Installing virtualenv-2.7-script.py script to c:\python27\Scripts
    Installing virtualenv-2.7.exe script to c:\python27\Scripts
    Successfully installed virtualenvwrapper-win virtualenv
    Cleaning up...


Python Tools for Visual Studio (PTVS) and virtualenv
=====================================================

.. seealso::

   - https://pytools.codeplex.com/wikipage?title=Virutal%20Env
   - :ref:`ptvs_2.0`
