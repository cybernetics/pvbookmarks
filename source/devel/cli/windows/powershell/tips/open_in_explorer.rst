
.. index::
   pair: Explorer; PowerShell


.. _open_powershell_in_explorer:

========================================
Open PowerShell in explorer
========================================


.. seealso::

   - http://stackoverflow.com/questions/183901/how-to-start-powershell-from-windows-explorer
   

.. contents::
   :depth: 3   

Introduction
=============

::


    Windows Registry Editor Version 5.00

    [HKEY_CLASSES_ROOT\Directory\shell\powershell]
    @="Open PowerShell here"
    "NoWorkingDirectory"=""
    "Extended"=""

    [HKEY_CLASSES_ROOT\Directory\shell\powershell\command]
    @="C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe -NoExit -Command Set-Location -LiteralPath ‘%L’"
