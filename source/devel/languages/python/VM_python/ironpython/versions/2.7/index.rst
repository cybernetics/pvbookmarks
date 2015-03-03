

===============
Ironpython 2.7
===============

.. seealso:: http://ironpython.codeplex.com/releases/view/71089


The first community release of IronPython is now available – IronPython 2.7 Beta 2
==================================================================================

At long (long) last, the first community release of IronPython is now
available – IronPython 2.7 Beta 2. The highlights of this release are
the new zlib (which also enables gzip) and subprocess modules.

There have also been a number of bug fixes.

Since Beta 1, we've moved all development to the Github IronLanguages project,
although the issue tracker is still on CodePlex.
This meant learning the build system, learning how to package a release
(something that needs some work), and various other odds 'n ends.
There are definitely some stumbling blocks that new people might trip over,
so those should be taken care of as soon as possible.


.. seealso::

   - https://github.com/IronLanguages/main
   - http://jdhardy.blogspot.com/2011/02/ironpython-27-beta-2-now-available.html



This is the first release candidate of IronPython 2.7.1. Like IronPython 2.7,
this release requires .NET 4 or Silverlight 4.

This release will replace any existing IronPython installation.

If there are no showstopping issues, this will be the only release candidate
for 2.7.1, so please speak up if you run into any roadblocks.

The highlights of 2.7.1 are:

- Updated the standard library to match CPython 2.7.2.
- Add the ast, csv, and unicodedata modules.
- Fixed several bugs.
- IronPython Tools for Visual Studio are disabled by default.
  See http://pytools.codeplex.com for the next generation of Python Visual Studio support.


.. seealso:: http://ironpython.codeplex.com/releases/view/54498

On behalf of the IronPython team, I'm very pleased to announce the release of
IronPython 2.7. This release contains all of the language features of Python 2.7,
as well as several previously missing modules and numerous bug fixes.

IronPython 2.7 also includes built-in Visual Studio support through IronPython
Tools for Visual Studio. IronPython 2.7 requires .NET 4.0 or Silverlight 4.

To download IronPython 2.7, visit http://ironpython.codeplex.com/releases/view/54498.

Any bugs should be reported at http://ironpython.codeplex.com/workitem/list/basic.

Python 2.7 includes a number of features backported from the Python 3.0 series.
This release implements the new builtin _io module, includes dictionary and set
comprehensions, set literals, supports multiple context managers in the with
statement, and adds several new functions to the itertools methods, and auto
indexing for the new string formatting. There are also numerous updates to the
standard library such as ordered dictionaries and the new argparse module.

This release also includes a “IronPython Tools for Visual Studio” option within
the IronPython installer. This enables one install to get both IronPython and
IronPython Visual Studio support assuming you have an existing installation of
Visual Studio 2010. This version of IronPython Tools includes a number of bug
fixes as improved WPF designer support. The designer fully supports XAML and
WPF including data binding to Python classes dynamically.

To improve interop with modern .NET code such as LINQ, support for extension
methods has been added as the clr.ImportExtensions method.

We’ve also updated the IronPython installer to include documentation based upon
the CPython documentation. This new .chm file includes documentation on the
Python language and standard library. It’s been extended from the normal
Python documentation to include IronPython specific topics such as the
DLR hosting APIs and extending IronPython from statically typed .NET languages.

We flushed out more support for missing built-in modules which CPython includes.
This release includes the mmap and signal modules bringing better support for
interoperating with unmanaged code, the zlib and gzip modules for compression,
and the subprocess and webbrowser modules for interacting with other programs.

