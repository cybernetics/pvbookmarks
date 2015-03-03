
.. index::
   pair: monodevelop version; 2.8.5



.. _monodevelop_2.8.5:

=====================================
monodevelop 2.8.5 (December 13, 2011)
=====================================


This release includes the following fixes and improvements:

Workarounds for some Xcode integration issues
    Fixed the case where Xcode could spontaenously restart certain circumstances
    after it was exited
    Added a workaround to try to avoid a deadlock in Xcode when it starts up

Better iPhone debugging support
    A predefined port is no longer required

Fixed rendering glitches on Windows
    Fixed the case where some windows would turn black the second (and subsequent)
    time they were viewed and would never re-render properly

Better support for both case-insensitive and case-sensitive file systems
    Correctly handle changing the case of a filename on a case-insensitive filesystem
    MacOS is now treated as case-insensitive (the default for the filesystem)

Several fixes and enhancements to the Version Control support and to SVN support
    in particular Adding a project which contains linked files to version control
    is now handled correctly

Several fixes to drag and drop support
    Dragging and dropping folders within MonoDevelop while under SVN version
    control is supported now
    If an unexpected error happens during a drag and drop operation, MonoDevelop
    will no longer hard crash


Updater
    Fixed a cause of the updater crashing on startup on Windows














