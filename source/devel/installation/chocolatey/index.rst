


.. index::
   pair: Installer; Chocolatey
   pair: Chocolatey; PowerShell
   ! Chocolatey

.. _chocolatey:
.. _choco:

==========================================================================
Chocolatey NuGet (like apt-get, but for Windows)
==========================================================================


.. seealso::

   - http://chocolatey.org/
   - https://github.com/chocolatey/chocolatey/wiki/CreatePackages
   - :ref:`powershell`
   - :ref:`nuget`


.. figure:: chocolateyicon.gif
   :align: center


.. contents::
   :depth: 3

Introduction
============

Chocolatey NuGet is a Machine Package Manager, somewhat like apt-get,
but built with Windows in mind.

Source requirements
====================

- .NET Framework 4.0
- PowerShell 2.0+


chocolatey ?
=============

Chocolatey is a global PowerShell execution engine using the NuGet
packaging infrastructure.

**Think of it as the ultimate automation tool for Windows**.

Chocolatey is like apt-get, but built with Windows in mind (there are
differences and limitations).

For those unfamiliar with apt/debian, think about chocolatey as a global
silent installer for applications and tools.

It can also do configuration tasks and anything that you can do with
PowerShell. The power you hold with a tool like chocolatey is only
limited by your imagination!

You can develop your tools and applications with NuGet, and release
them with chocolatey!

But chocolatey is not just for .NET tools.

It's for nearly any windows application/tool !


::

    C:\>@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex
    ((new-object net.webclient).DownloadString('http://chocolatey.org/install.ps1'))"
    && SET PATH=%PATH%;%systemdrive%\chocolatey\bin


::

    Mode                LastWriteTime     Length Name
    ----                -------------     ------ ----
    d----        11/03/2013     08:54            chocInstall
    Downloading http://chocolatey.org/api/v2/package/chocolatey/ to C:\DOCUME~1\pvergain\LOCALS~1\Temp\chocolatey\chocInstall\chocolatey.zip
    Extracting C:\DOCUME~1\pvergain\LOCALS~1\Temp\chocolatey\chocInstall\chocolatey.
    zip to ...
    Installing chocolatey on this machine
    Creating ChocolateyInstall as a User Environment variable and setting it to 'C:\Chocolatey'
    We are setting up the Chocolatey repository for NuGet packages that should be at
     the machine level. Think executables/application packages, not library packages
    .
    That is what Chocolatey NuGet goodness is for.
    The repository is set up at 'C:\Chocolatey'.
    The packages themselves go to 'C:\Chocolatey\lib' (i.e. C:\Chocolatey\lib\yourPackageName).
    A batch file for the command line goes to 'C:\Chocolatey\bin' and points to an executable in 'C:\Chocolatey\lib\yourPackageName'.

    Creating Chocolatey NuGet folders if they do not already exist.

    d----        11/03/2013     08:54            bin
    d----        11/03/2013     08:54            lib
    d----        11/03/2013     08:54            chocolateyinstall
    Copying the contents of 'C:\Documents and Settings\pvergain\Local Settings\Temp\chocolatey\chocInstall\tools\chocolateyInstall' to 'C:\Chocolatey'.
    Creating 'C:\Chocolatey\bin\chocolatey.bat' so you can call 'chocolatey' from anywhere.
    Creating 'C:\Chocolatey\bin\cinst.bat' so you can call 'chocolatey install' from a shortcut of 'cinst'.
    Creating 'C:\Chocolatey\bin\cinstm.bat' so you can call 'chocolatey installmissing' from a shortcut of 'cinstm'.
    Creating 'C:\Chocolatey\bin\cup.bat' so you can call 'chocolatey update' from ashortcut of 'cup'.
    Creating 'C:\Chocolatey\bin\clist.bat' so you can call 'chocolatey list' from a shortcut of 'clist'.
    Creating 'C:\Chocolatey\bin\cver.bat' so you can call 'chocolatey version' from a shortcut of 'cver'.
    Creating 'C:\Chocolatey\bin\cwebpi.bat' so you can call 'chocolatey webpi' from a shortcut of 'cwebpi'.
    Creating 'C:\Chocolatey\bin\cwindowsfeatures.bat' so you can call 'chocolatey windowsfeatures' from a shortcut of 'cwindowsfeatures'.
    Creating 'C:\Chocolatey\bin\ccygwin.bat' so you can call 'chocolatey cygwin' from a shortcut of 'ccygwin'.
    Creating 'C:\Chocolatey\bin\cpython.bat' so you can call 'chocolatey python' from a shortcut of 'cpython'.
    Creating 'C:\Chocolatey\bin\cgem.bat' so you can call 'chocolatey gem' from a shortcut of 'cgem'.
    Creating 'C:\Chocolatey\bin\cpack.bat' so you can call 'chocolatey pack' from a shortcut of 'cpack'.
    Creating 'C:\Chocolatey\bin\cpush.bat' so you can call 'chocolatey push' from a shortcut of 'cpush'.
    Creating 'C:\Chocolatey\bin\cuninst.bat' so you can call 'chocolatey uninstall'
    from a shortcut of 'cuninst'.

    PATH environment variable does not have 'C:\Chocolatey\bin' in it. Adding.
    Processing ccygwin.bat to make it portable
    Processing cgem.bat to make it portable
    Processing chocolatey.bat to make it portable
    Processing cinst.bat to make it portable
    Processing cinstm.bat to make it portable
    Processing clist.bat to make it portable
    Processing cpack.bat to make it portable
    Processing cpush.bat to make it portable
    Processing cpython.bat to make it portable
    Processing cuninst.bat to make it portable
    Processing cup.bat to make it portable
    Processing cver.bat to make it portable
    Processing cwebpi.bat to make it portable
    Processing cwindowsfeatures.bat to make it portable
    Chocolatey is now ready.


You can call chocolatey from anywhere, command line or powershell by typing
chocolatey.

Run chocolatey /? for a list of functions.

You may need to shut down and restart powershell and/or consoles first prior to
using chocolatey.

If you are upgrading chocolatey from an older version (prior to 0.9.8.15) and
don't use a custom chocolatey path, please find and delete the C:\NuGet folder
after verifying that C:\Chocolatey has the same contents (minus chocolateyinstall
of course).

Ensuring chocolatey commands are on the path


::


    C:\CHOCOLATEY
    |
    +---bin
    |       AddWindowsExplorerShortcut.bat
    |       ccygwin.bat
    |       cgem.bat
    |       chocolatey.bat
    |       cinst.bat
    |       cinstm.bat
    |       clist.bat
    |       cpack.bat
    |       cpush.bat
    |       cpython.bat
    |       cuninst.bat
    |       cup.bat
    |       cver.bat
    |       cwebpi.bat
    |       cwindowsfeatures.bat
    |       lessmsi.bat
    |       _processed.txt
    |
    +---chocolateyinstall
    |   |   chocolatey.cmd
    |   |   chocolatey.config
    |   |   chocolatey.ps1
    |   |   chocolateyInstall.log
    |   |   error.log
    |   |   install.log
    |   |   LICENSE.txt
    |   |   list.log
    |   |   NuGet.exe
    |   |   NuGet.exe.ignore
    |   |
    |   +---functions
    |   |       Chocolatey-Cygwin.ps1
    |   |       Chocolatey-Help.ps1
    |   |       Chocolatey-Install.ps1
    |   |       Chocolatey-InstallAll.ps1
    |   |       Chocolatey-InstallExtension.ps1
    |   |       Chocolatey-InstallIfMissing.ps1
    |   |       Chocolatey-List.ps1
    |   |       Chocolatey-NuGet.ps1
    |   |       Chocolatey-Pack.ps1
    |   |       Chocolatey-PackagesConfig.ps1
    |   |       Chocolatey-Push.ps1
    |   |       Chocolatey-Python.ps1
    |   |       Chocolatey-RubyGem.ps1
    |   |       Chocolatey-Sources.ps1
    |   |       Chocolatey-Uninstall.ps1
    |   |       Chocolatey-Update.ps1
    |   |       Chocolatey-Version.ps1
    |   |       Chocolatey-WebPI.ps1
    |   |       Chocolatey-WindowsFeatures.ps1
    |   |       Create-InstallLogIfNotExists.ps1
    |   |       Delete-ExistingErrorLog.ps1
    |   |       Generate-BinFile.ps1
    |   |       Get-ChocolateyBins.ps1
    |   |       Get-ConfigValue.ps1
    |   |       Get-GlobalConfigValue.ps1
    |   |       Get-LatestPackageVersion.ps1
    |   |       Get-LongPackageVersion.ps1
    |   |       Get-PackageFoldersForPackage.ps1
    |   |       Get-PackageFolderVersions.ps1
    |   |       Get-SourceArguments.ps1
    |   |       Get-Sources.ps1
    |   |       Get-UserConfigValue.ps1
    |   |       Get-VersionsForComparison.ps1
    |   |       Remove-LastInstallLog.ps1
    |   |       Run-ChocolateyProcess.ps1
    |   |       Run-ChocolateyPS1.ps1
    |   |       Run-NuGet.ps1
    |   |       Write-UserConfig.ps1
    |   |
    |   \---helpers
    |       |   chocolateyInstaller.psm1
    |       |
    |       \---functions
    |               Get-ChocolateyUnzip.ps1
    |               Get-ChocolateyWebFile.ps1
    |               Get-FtpFile.ps1
    |               Get-WebFile.ps1
    |               Install-ChocolateyDesktopLink.ps1
    |               Install-ChocolateyEnvironmentVariable.ps1
    |               Install-ChocolateyExplorerMenuItem.ps1
    |               Install-ChocolateyFileAssociation.ps1
    |               Install-ChocolateyInstallPackage.ps1
    |               Install-ChocolateyPackage.ps1
    |               Install-ChocolateyPath.ps1
    |               Install-ChocolateyPinnedTaskBarItem.ps1
    |               Install-ChocolateyPowershellCommand.ps1
    |               Install-ChocolateyVsixPackage.ps1
    |               Install-ChocolateyZipPackage.ps1
    |               Start-ChocolateyProcessAsAdmin.ps1
    |               Uninstall-ChocolateyPackage.ps1
    |               UnInstall-ChocolateyZipPackage.ps1
    |               Update-SessionEnvironment.ps1
    |               Write-ChocolateyFailure.ps1
    |               Write-ChocolateySuccess.ps1
    |               Write-Debug.ps1
    |               Write-Error.ps1
    |               Write-Host.ps1
    |
    \---lib
        +---lessmsi.1.0.9
        |   |   lessmsi.1.0.9.nupkg
        |   |   lessmsiInstall.zip.txt
        |   |
        |   \---tools
        |           AddWindowsExplorerShortcut.exe
        |           ChocolateyInstall.ps1
        |           lessmsi.exe
        |           libmspackn.dll
        |           mspack.dll
        |           wix.dll
        |           wixcab.dll
        |
        \---PowerShell.3.0.20121027
                ChocolateyInstall.ps1
                PowerShell.3.0.20121027.nupkg


Chocolatey packages
===================

.. seealso:: http://chocolatey.org/packages?sortOrder=package-download-count&page=5&prerelease=False


Is there a video I can watch to show me chocolatey in action ?

There is! This is a long video due to slow internet connections, but
watch the first 1:30ish minutes and the last 1:30ish minutes and
that will give you a general idea. http://www.youtube.com/watch?v=N-hWOUL8roU

.. note:: This video shows dependency chaining, so you are seeing it
  install 11 applications/tools.

.. toctree::
   :maxdepth: 3
   
   packages/index


Source requirements
===================

- .NET Framework 4.0
- PowerShell 2.0+

Dependency Chaining
===================

You can make packages that depend on other packages just by adding those
dependencies to the nuspec.

Take a look at `ferventcoder.chocolatey.utilities nuspec`_


.. _`ferventcoder.chocolatey.utilities nuspec`:  https://github.com/ferventcoder/nugetpackages/blob/master/ferventcoder.chocolatey.utilities/ferventcoder.chocolatey.utilities.nuspec



Chocolatey source code
======================

::

    https://github.com/chocolatey/chocolatey



Chocolatey news
================

.. toctree::
   :maxdepth: 3

   news/index




