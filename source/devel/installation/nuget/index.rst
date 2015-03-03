

.. index::
   pair: Visual Studio 2010; Nuget
   ! Nuget


.. _nuget:

=======================================
nuget
=======================================

.. seealso::

   - http://nuget.org/
   - https://en.wikipedia.org/wiki/NuGet
   - http://nuget.codeplex.com/
   - http://docs.nuget.org/
   - :ref:`chocolatey`


.. contents::
   :depth: 3

Introduction
============


``NuGet`` is a Visual Studio extension that makes it easy to install and update
open source libraries and tools in Visual Studio.

NuGet is a free, open source developer focused package management system for
the .NET platform intent on simplifying the process of incorporating third
party libraries into a .NET application during development.

NuGet is a member of the ASP.NET Gallery in the `Outercurve Foundation`_ (see the press release).

There are a large number of useful 3rd party open source libraries out there
for the .NET platform, but for those not familiar with the OSS ecosystem, it
can be a pain to pull these libraries into a project.

Let’s take ELMAH as an example. It’s a fine error logging utility which has no
dependencies on other libraries, but is still a challenge to integrate into a
project. These are the steps it takes:

- Find ELMAH
- Download the correct zip package.
- “Unblock” the package.
- Verify its hash against the one provided by the hosting environment.
- Unzip the package contents into a specific location in the solution.
- Add an assembly reference to the assembly.
- Update web.config with the correct settings which a developer needs to search for.


And this is for a library that has no dependencies. Imagine doing this for
NHibernate.Linq which has multiple dependencies each needing similar steps.

We can do much better!

NuGet automates all these common and tedious tasks for a package as well as its
dependencies. It removes nearly all of the challenges of incorporating a third
party open source library into a project’s source tree. Of course, using that
library properly is still up to the developer.


.. _`Outercurve Foundation`:  http://outercurve.org/


Nuget versions
==============

.. toctree::
   :maxdepth: 4

   versions/index


