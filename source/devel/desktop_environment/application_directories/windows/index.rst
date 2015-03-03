
.. index::
   pair: Windows ; Application Directories
   pair: CISL ; Application Directories


.. _windows_appdirectories:

================================
Windows Application directories 
================================


.. seealso::

   - http://technet.microsoft.com/en-us/library/cc766489%28WS.10%29.aspx

.. contents::
   :depth: 3

CISL
====

.. seealso::

   - http://msdn.microsoft.com/en-us/library/windows/desktop/bb762494%28v=vs.85%29.aspx



Note  As of Windows Vista, these values have been replaced by KNOWNFOLDERID 
values. 

See that topic for a list of the new constants and their corresponding CSIDL 
values. For convenience, corresponding KNOWNFOLDERID values are also noted here 
for each CSIDL value.

The CSIDL system is supported under Windows Vista for compatibility reasons. 
However, new development should use KNOWNFOLDERID values rather than CSIDL values.

CSIDL (constant special item ID list) values provide a unique system-independent 
way to identify special folders used frequently by applications, but which may 
not have the same name or location on any given system. 

For example, the system folder may be "C:\Windows" on one system and "C:\Winnt" 
on another. These constants are defined in Shlobj.h.


KNOWNFOLDERID
=============


.. seealso::

   - http://msdn.microsoft.com/en-us/library/windows/desktop/dd378457%28v=vs.85%29.aspx


The KNOWNFOLDERID constants represent GUIDs that identify standard folders 
registered with the system as Known Folders. 

These folders are installed with Windows Vista and later operating systems, and 
a computer will have only folders appropriate to it installed


