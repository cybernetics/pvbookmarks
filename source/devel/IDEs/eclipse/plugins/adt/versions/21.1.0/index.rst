


======================================================
Android Development Tools (ADT) 21.1.0 (February 2013)
======================================================


.. contents::
   :depth: 3

Dependencies
=============

- Java 1.6 or higher is required for ADT 21.1.0.
- Eclipse Helios (Version 3.6.2) or higher is required for ADT 21.1.0.
- ADT 21.1.0 is designed for use with SDK Tools r21.1. If you haven't already installed SDK Tools r21.1 into your SDK, use the Android SDK Manager to do so.

General Notes
==============

- Added new code templates for notifications, blank fragments and list fragments.
- Added support for resource rename refactoring. Renaming a resource XML file,
  drawable icon, an R. field name or ID in the layout editor invokes a refactoring
  routine to update all resource references.
- Added more than 15 new Lint checks, including checks for overriding older APIs,
  XML resource problems, graphic asset issues and manifest tags.
- Updated XML Editor to respond to refactoring shortcut keys such as Refactor > Rename.
- Updated XML Editor to improve double click handling.
- Added code completion improvements for custom views, theme references and class
  references. For example, code completion in a <fragment android:name=””> tag now
  suggests completion with a list of fragment classes.
  Similarly, code completion in the manifest now offers implementations suitable
  for the given tag.
- Updated the Project Import dialog so that it shows a table for all imported
  projects where you can edit the name of the imported project.
- Added support for layout aliases in the Layout Editor.

Bug fixes
=========

- Fixed issued with refactoring support for renaming and moving classes and packages.



