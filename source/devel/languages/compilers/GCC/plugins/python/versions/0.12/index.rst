

.. _gcc_python_plugin_012:

============================================
gcc-python-plugin 0.12
============================================


.. contents::
   :depth: 3

GCC 4.8 compatibility
======================

This release of the plugin adds support for gcc 4.8 (along with continued support
for gcc 4.7 and gcc 4.6).


gcc-c-api
==========

The source tree contains a new component: ``gcc-c-api``.


This provides a wrapper library libgcc-c-api.so that hides much of the details
of GCC’s internals (such as the binary layout of structures, and the differences
between GCC 4.6 through 4.8).

I plan for this to eventually be its own project, aiming at providing a stable
API and ABI for working with GCC, once it has proven itself in the context of the
python plugin.

The API provides an XML description of itself, which should greatly simplify the
job of generating bindings for accessing GCC internals from other languages.
