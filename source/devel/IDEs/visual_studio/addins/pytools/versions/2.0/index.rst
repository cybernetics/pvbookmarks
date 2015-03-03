
.. index::
   pair: PTVS; 2.0


.. _ptvs_2.0:

=================================================================
Python Tools for Visual Studio (PTVS) 2.0  alpha (7 march 2013)
=================================================================


.. seealso::

   - https://pytools.codeplex.com/releases/view/72638


.. contents::
   :depth: 3

Release Notes
=============


We’re pleased to announce the release of Python Tools for Visual Studio 2.0 Alpha.

Python Tools for Visual Studio (PTVS) is an open-source plug-in for Visual Studio
which supports programming with the Python language.

PTVS supports a broad range of features including CPython/IronPython,
Edit/Intellisense/Debug/Profile, Cloud, HPC, IPython, and cross platform debugging
support.

For a quick overview of the general IDE experience, please watch this video

There are a number of exciting improvement in this release compared to 1.5, all
based on your feedback & suggestions.

Here’s a summary:

.. note:: this is an Alpha release which is primarily meant for feedback
   purposes and has not been tested as much as the 1.5.x RTM releases!
   This release works with both VS2010 and VS2012.
   Alpha limitations are noted in the corresponding docs for each feature.
   Please try these bits and let us know what you think!


.. _virtualenv_windows:

IDE
----

.. seealso::

   - https://pytools.codeplex.com/wikipage?title=Virutal%20Env
   - :ref:`virtualenvwrapper_windows`


- Vastly improved analysis and intellisense – you can now get much deeper and
  extensive intellisense. Please refer to the documentation or this video for an overview.
- Remote Debugging! PTVS already supported “attach” style debugging locally and
  on clusters, now you do full remote debugging, even on Linux and Macs!
  Please refer to the docs or this video for an overview.
- Code formatting – now you can format code based on various standards & parameters.
  See the overview.
- Virtual Env – PTVS has early support for `virtual envs <virtualenv>`. Overview or video.
- Debug Script – you can now debug a python script without first setting up a VS
  project for it. Just right click & debug away. Docs or video.
- Navigate To – this feature provide a convenient way to navigate around your code. Docs
- Support for zip files – you can include zip file in your project. Support is preliminary.
  lots of bug fixes & smaller enhancements

Cloud
------

- Azure Web Sites **you can now publish a Django site to Azure** with minimum number
  of clicks. Azure provides free hosting to kick the tires. See an overview.
- Simplified deployment (Python 2.7 is now preconfigured on Azure servers).
- Various bug fixes to the Azure SDK.
