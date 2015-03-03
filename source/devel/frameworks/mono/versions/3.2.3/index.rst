
.. index::
   pair: Mono; 3.2.3


.. _mono_3.2.3:

=============================
Mono 3.2.3
=============================


.. seealso::

   - http://www.mono-project.com/Release_Notes_Mono_3.2#New_in_Mono_3.2.3


.. contents::
   :depth: 3

New in Mono 3.2.3
=================


This release features over 2 months of fixes a few nice features.

We're now back to do simultaneous releases to Windows, Linux and Mac.

The C# compiler has a lot of fixes for async related issues.

New static and dynamic hardware capabilities probing, mono can now exploit 
hardware caps in many more cases than before.

Blended v5/v7 mode for arm. Some ARM targets require binaries that support all 
the way from very old CPUs to the most modern ones. 
Previously we would fail to work on SMP machines when built for UP targets.

Added skeletons for both System.DirectoryServices and System.Windows.Forms.DataVisualization.Charting.

New server focused flag. Run mono with --server to tell the runtime to target 
performance. With this release, this means an aggressive threadpool scheduler 
that creates additional threads faster.

We put a lot of effort on windows for this release. 
Builds are now based on a recent mingw toolchain. We fixes a good number of 
build issues and bugs in the windows backed.

We have finally switched to use vectored exception handling on windows, which 
makes it possible, for those of us that like Inception, to debug mono's debugger.

And, finally, PCL has arrived. This means a few fixes in the runtime, class 
libraries and build tools. And, on Mac, we now ship PCL reference assemblies. 




