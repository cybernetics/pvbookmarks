


.. index::
   pair: Sphinx; Read the docs
   ! Read the docs

.. _read_the_doc:
.. _read_the_docs:

=======================
Sphinx on Read the docs
=======================

.. figure:: read_the_doc.png
   :align: center

.. seealso::

   - http://read-the-docs.readthedocs.org/en/latest/index.html
   - http://read-the-docs.readthedocs.org/en/latest/getting_started.html


.. contents::
   :depth: 3

Introduction
============

Read the Docs hosts documentation for the open source community.

It supports Sphinx docs written with reStructuredText, and can pull from your
Subversion, Bazaar, Git, and Mercurial repositories.

The code is open source, and available on github::

    git clone http://github.com/rtfd/readthedocs.org.git


Read the docs on twitter
========================

- https://twitter.com/readthedocs



New theme (4th of november 2013)
================================

.. seealso::

   - http://ericholscher.com/blog/2013/nov/4/new-theme-read-the-docs/



Using it
---------

There are two ways that you can use this theme on Read the Docs. 

The first is to simply leave your html_theme variable set to default. 
This is now the default Read the Docs theme. 

You can also set RTD_NEW_THEME = True in your project’s conf.py, and we will 
use our theme when building on Read the Docs no matter what html_theme is set to.

After you change these settings, simply rebuild your docs and the theme should 
update. More information about the theme can be found on the theme documentation page

If you want to continue using the old theme, simply set RTD_OLD_THEME = True 
in your conf.py.

Conclusion
-----------

This theme is a great addition to the documentation ecosystem. 
It is highly functional and beautiful, allowing users to easily navigate and 
find what they need.

We have a few more tricks up our sleeves, but theme is ready to launch today. 
Over the next few weeks we’ll be adding a bit more functionality to it, which 
should be even more delightful.

I hope that you enjoy using it. If you have any feedback, please open an issue 
on GitHub. To follow announcements for Read the Docs, follow us on Twitter.

If you want to support work like this, help fund development on Read the Docs 
on Gittip.


Projects on Read the docs
=========================

.. toctree::
   :maxdepth: 3
   
   projects/projects
   
   


