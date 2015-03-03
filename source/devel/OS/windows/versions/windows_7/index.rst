
.. index::
   pair: Windows OS; Windows 7

.. _windows_7:

===============
Windows 7 (6.1)
===============

.. seealso::

   - http://en.wikipedia.org/wiki/Windows_7
   - http://en.wikipedia.org/wiki/Features_new_to_Windows_7


====================  =======  ===================================================
Platform support      Version  Current version
IA-32, x86-64         6.1      6.1 (build 7600.16385.090713-1255) October 22, 2009
====================  =======  ===================================================

.. seealso:: :ref:`innosetup_examples`



.. _windows_7_64bits:


Win32, Win64
============

.. _file_system_redirector:

File System Redirector
----------------------

.. seealso:: http://msdn.microsoft.com/en-us/library/aa384187%28VS.85%29.aspx

The %windir%\System32 directory is reserved for 64-bit applications. Most
DLL file names were not changed when 64-bit versions of the DLLs were
created, so 32-bit versions of the DLLs are stored in a different
directory. WOW64 hides this difference using a file system redirector.

In most cases, whenever a 32-bit application attempts to access
%windir%\System32, the access is redirected to %windir%\SysWOW64.
Access to %windir%\lastgood\system32 is redirected to
%windir%\lastgood\SysWOW64. Access to %windir%\regedit.exe is
redirected to %windir%\SysWOW64\regedit.exe.

Certain subdirectories are exempt from redirection. Access to these
subdirectories is not redirected to %windir%\SysWOW64:

- %windir%\system32\catroot
- %windir%\system32\catroot2
- %windir%\system32\driversstore
- %windir%\system32\drivers\etc
- %windir%\system32\logfiles
- %windir%\system32\spool

If the access causes the system to display the UAC prompt, redirection
does not occur. Instead, the 64-bit version of the requested file is
launched. To prevent this problem, either specify the SysWOW64 directory
to avoid redirection and ensure access to the 32-bit version of the file,
or run the 32-bit application with administrator privileges so the
UAC prompt is not displayed.


