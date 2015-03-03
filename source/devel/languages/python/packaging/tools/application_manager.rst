

.. _application_manager:

==========================
Application manager
==========================

.. seealso::

   - http://pypi.python.org/pypi/infi.recipe.application_packager
   - https://github.com/Infinidat/infi.recipe.application_packager


Overview
========

At Infinidat, we write products in Python, and not just a bunch of scripts. 

We want our products to be isolated from global Python installations and 
site-packages.

The solution we came with is as follows:

Bundle the interpreter itself in the application, along with all the 
dependencies.

If there are binary dependencies, compile it when building the application 
package
This is our buildout recipe for creating the platform-specific packages.

The currently supported packages/platforms, are:

- RPM on RedHat/CentOS
- DEB on Ubuntu
- MSI on Windows

