


.. _gradle_android_studio:

===============
Android Studio 
===============

.. seealso:: http://tools.android.com/tech-docs/new-build-system/user-guide


.. contents::
   :depth: 3
   


Goals of the new Build System
==============================

The goals of the new build system are:

- Make it easy to reuse code and resources
- Make it easy to create several variants of an application, either for 
  multi-apk distribution or for different flavors of an application
- Make it easy to configure, extend and customize the build process
- Good IDE integration

Why Gradle ?
=============


Gradle is an **advanced build system** as well as an advanced build toolkit allowing 
to create custom build logic through plugins.

Here are some of its features that made us choose Gradle:

- Domain Specific Language (DSL) to describe and manipulate the build logic
- Build files are Groovy based and allow mixing of declarative elements through 
  the DSL and using code to manipulate the DSL elements to provide custom logic.
- Built-in dependency management through Maven and/or Ivy.
- Very flexible. Allows using best practices but doesn’t force its own way of doing things.
- Plugins can expose their own DSL and their own API for build files to use.
- Good Tooling API allowing IDE integration

