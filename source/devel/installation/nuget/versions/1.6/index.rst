


=======================================
nuget 1.6
=======================================


If you are running VS 2010 SP1, you might run into an installation error when
attempting to upgrade NuGet if you have an older version installed.

The workaround is to simply uninstall NuGet and then install it from the VS Extension Gallery.

See http://support.microsoft.com/kb/2581019 for more information.

Note: If Visual Studio won't allow you to uninstall the extension (the Uninstall
button is disabled), then you likely need to restart Visual Studio using "Run as Administrator."


Features
========

Support for Semantic Versioning and Prerelease Packages
-------------------------------------------------------


NuGet 1.6 introduces support for Semantic Versioning (SemVer).

For more details on how it uses SemVer, read the Versioning documentation.

Using NuGet Without Checking In Packages (Package Restore)
----------------------------------------------------------

NuGet 1.6 now has first class support for the workflow in which NuGet packages
are not added to source control, but instead are restored at build time if missing.

For more details, read the Using NuGet without committing packages to source
control topic.


Item Templates That Install NuGet Packages
------------------------------------------

Building on the work to support preinstalled NuGet package to Visual Studio
project templates, NuGet 1.6 also adds support for Visual Studio item templates.

Item templates can have associated NuGet packages that are installed when the
template in invoked.

For more details on how to change a project/item template to install NuGet packages,
read the Packages in Visual Studio Templates topic.

Support for disabling package sources
--------------------------------------

When multiple package sources are configured, NuGet will look in each one for
packages during installation of a package and its dependencies.

A package source that is down for some reason can severely slow down NuGet.

Prior to NuGet 1.6, you could remove the package source, but then you have to
remember the details for when you want to add it back in.

NuGet 1.6 allows unchecking a package source to disable it, but keep it around.
