
.. index::
   pair: Program; Version


.. _windows_get_program_version:

=========================
Get program version
=========================


.. seealso::

   - :ref:`choco`
   

.. contents::
   :depth: 3   

Introduction
=============

Some programs come with a built-in auto-update, like Notepad++, Firefox, 
LibreOffice, Google Chrome and more.

If a program gets updated without the use of Chocolatey, Chocolatey of 
course does not detect it. When after some time the package maintainer 
updates the package of the affected program, the same as the installed 
version of the program gets downloaded and installed again.

This behavior is of course not optimal, because it consumes time, download 
bandwith, cpu usage and hard disk/SSD usage with no use, especially when 
there are huge file sizes.

In PowerShell there exists a simple way to get the installed program 
versions through registry keys

For every program on 32-bit-systems and for 64-bit-software on 64-bit systems
-----------------------------------------------------------------------------

::

    # For every program on 32-bit-systems and for 64-bit-software on 64-bit systems
    $programName = # name of the program
    $installedVersion = (Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\$programName).DisplayVersion


For 32-bit-software on 64-bit systems
-------------------------------------

    # For 32-bit-software on 64-bit systems
    $programName = # name of the program
    $installedVersion = (Get-ItemProperty HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\$programName).DisplayVersion


The version if the installed program could then be compared to the package 
version. When the same version is already installed, the 
Install-ChocolateyPackage helper could be skipped.

How about integrating this into Chocolatey packages?


The code I posted first was not working with every program, so here the 
improved code bundled with two program examples::

    # For every program on 32-bit-systems and for 64-bit-software on 64-bit systems
    $programUninstallEntryName = CCleaner # The value which contains the registry-key “DisplayName” of the affected program
    $installedVersion = (Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\* | Select DisplayName, DisplayVersion | Where-Object {$_.DisplayName -eq "$programUninstallEntryName"}).DisplayVersion
    # $installedVersion is the value of the registry-key “DisplayVersion” of the affected program

    # For 32-bit-software on 64-bit systems
    $programUninstallEntryName = CDBurnerXP
    $installedVersion = (Get-ItemProperty HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select DisplayName, DisplayVersion | Where-Object {$_.DisplayName -eq "$programUninstallEntryName"}).DisplayVersion


The problem is that the two registry values used here (DisplayName and DisplayVersion) 
do not always match with the package ID and package version.

A few examples are::

    Here everything matches:
    DisplayName: CDBurnerXP
    DisplayVersion: 4.5.1.3868
    Here the DisplayName-entry also contains the version:
    DisplayName: LibreOffice 4.0.3.3
    DisplayVersion: 4.0.3.3
    Here nothing matches exactly with the package ID and the package version
    DisplayName: Java 7 Update 21
    DisplayVersion: 7.0.210

Due to these different possibilities, it is impossible to integrate this 
code into Chocolatey directly to automatically prevent a program from 
installing again when the same version is already installd.

But how about a helper for the chocolateyInstall.ps1 script? It could 
look like this::

    Check-InstalledProgramVersion $programUninstallEntryName $installedVersionMatch


If then the program which the package wants to install is already 
installed in the latest version (identifiable with  $installedVersionMatch), 
this helper should skip every other command in the chocolateyInstall.ps1 script.

