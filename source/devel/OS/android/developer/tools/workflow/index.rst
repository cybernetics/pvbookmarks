
.. index::
   pair: Android ; Tools (Workflow)


.. _android_developer_tools_workflow:

=================================
Android Developer Tools workflow
=================================

.. seealso::

   - https://developer.android.com/tools/workflow/index.html
   - :ref:`android_developer`


Introduction
============

To develop apps for Android devices, you use a set of tools that are included in
the Android SDK. Once you've downloaded and installed the SDK, you can access
these tools right from your Eclipse IDE, through the ADT plugin, or from the
command line.

Developing with Eclipse is the preferred method because it can directly invoke
the tools that you need while developing applications.

However, you may choose to develop with another IDE or a simple text editor and
invoke the tools on the command line or with scripts.

This is a less streamlined way to develop because you will sometimes have to call
command line tools manually, but you will have access to the same number of features
that you would have in Eclipse.


Development phases
===================

The development steps encompass four development phases, which include:

Setup
------

During this phase you install and set up your development environment. You also
create Android Virtual Devices (AVDs) and connect hardware devices on which you
can install your applications.

See Managing Virtual Devices and Using Hardware Devices for more information.

Development
-----------

.. seealso::

   - https://developer.android.com/tools/building/index.html
   - https://developer.android.com/tools/projects/index.html

During this phase you set up and develop your Android project, which contains
all of the source code and resource files for your application.

For more informations, see Create an Android project.

During this phase you build your project into a debuggable .apk package that you
can install and run on the emulator or an Android-powered device.

If you are using Eclipse, builds are generated each time you project is saved.
If you're using another IDE, you can build your project using Ant and install it
on a device using adb.

For more information, see Build and run your application.

Debugging and Testing
---------------------

.. seealso::

   - https://developer.android.com/tools/testing/index.html
   - https://developer.android.com/tools/debugging/index.html


Next, you debug your application using a JDWP-compliant debugger along with the
debugging and logging tools that are provided with the Android SDK.

Eclipse already comes packaged with a compatible debugger.

For more information see, Debug your application with the SDK debugging and
logging tools.

Last, you test your application using various Android SDK testing tools.

For more information, see Test your application with the Testing and Instrumentation
framework.

Publishing
-----------

.. seealso::  https://developer.android.com/tools/publishing/publishing_overview.html

During this phase you configure and build your application for release and
distribute your application to users.

For more information, see Publishing Overview.






