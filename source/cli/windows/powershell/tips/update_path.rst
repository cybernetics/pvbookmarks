
.. index::
   pair: PATH; Powershell


.. _path_powershell:

================================================================
Add the directories for your default Python version to the PATH
================================================================

.. seealso::

   - http://docs.python-guide.org/en/latest/starting/install/win/

.. contents::
   :depth: 3   

Introduction
=============

Typing the full path name for a Python interpreter each time quickly gets 
tedious, so add the directories for your default Python version to the PATH. 

Assuming that your Python installation is in C:\Python27\, add this to your PATH::

    C:\Python27\;C:\Python27\Scripts\


You can do this easily by running the following in powershell

::

    Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
