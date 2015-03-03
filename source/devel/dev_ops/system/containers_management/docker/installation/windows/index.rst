
.. index::
   pair: Docker; Installation (Windows)


.. _docker_windows_installation:

===============================================================
Docker windows installation
===============================================================

.. seealso::

   - https://github.com/boot2docker/windows-installer


.. contents::
   :depth: 3
   

Description
============

Installation instructions available on the Docker documentation site.

What is included:

- msys-git 1.9.0 for tools like OpenSSH and BASH
- VirtualBox 4.3.10
- Boot2Docker-cli management tool v 0.9.2
- Boot2Docker ISO v0.9.1

Why InnoSetup ?
================

I've chosen to make a simple installer using innosetup because that is what the 
msysGit installer is built with.

(It also happens that I've used InnoSetup before, so I can make something faster.

Making a simple Wix for the Boot2Docker-cli should be simple, and this can then 
be used in this all-in-one installer too.



Versions
=========

.. toctree::
   :maxdepth: 3
   
   versions/index
   
   
