

.. index::
   pair: sphinx ;domain
   pair: default ;domain

.. _sphinx_domain:

=============
sphinx domain
=============


.. seealso::

   - http://sphinx-doc.org/latest/domains.html
   - http://sphinx-doc.org/latest/ext/appapi.html#domain-api


.. contents::
   :depth: 3


What is a Domain ?
===================

Originally, Sphinx was conceived for a single project, the documentation of the
Python language. Shortly afterwards, it was made available for everyone as a
documentation tool, but the documentation of Python modules remained deeply
built in – the most fundamental directives, like function, were designed for
Python objects. Since Sphinx has become somewhat popular, interest developed
in using it for many different purposes: C/C++ projects, JavaScript, or even
reStructuredText markup (like in this documentation).

While this was always possible, it is now much easier to easily support
documentation of projects using different programming languages or even ones
not supported by the main Sphinx distribution, by providing a domain for every
such purpose.

A domain is a collection of markup (reStructuredText directives and roles) to
describe and link to objects belonging together, e.g. elements of a programming
language. Directive and role names in a domain have names like domain:name,
e.g. py:function. Domains can also provide custom indices (like the Python Module Index).

Having domains means that there are no naming problems when one set of
documentation wants to refer to e.g. C++ and Python classes. It also means that
extensions that support the documentation of whole new languages are much easier
to write.


Default Domain
===============

.. seealso:: http://sphinx-doc.org/latest/config.html#confval-primary_domain


To avoid having to writing the domain name all the time when you e.g. only describe
Python objects, a default domain can be selected with either the config value
primary_domain or this directive:


::

    .. default-domain:: name


Select a new default domain. While the primary_domain selects a global default,
this only has an effect within the same file.


primary_domain
===============

The name of the default domain. Can also be None to disable a default domain.
The default is 'py'. Those objects in other domains (whether the domain name is
given explicitly, or selected by a default-domain directive) will have the domain
name explicitly prepended when named (e.g., when the default domain is C,
Python functions will be named “Python function”, not just “function”).


.. toctree::
   :maxdepth: 4

   c_domain
   cplusplus_domain
