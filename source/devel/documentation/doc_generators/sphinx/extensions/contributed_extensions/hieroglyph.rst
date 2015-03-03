
.. index::
   pair: sphinx extension ; hieroglyph

.. _sphinx_hieroglyph_extension:

=============================
Sphinx hieroglyph extension
=============================

.. seealso::

   - https://github.com/nyergler/hieroglyph


.. contents::
   :depth: 3


Introduction
============

hieroglyph is an extension for Sphinx which builds HTML5 slides from
ReStructured Text documents.


Installing
==========

You can install Hieroglyph using easy_install or pip:

$ easy_install hieroglyph


Using Hieroglyph
=================

Add Hieroglyph as a Sphinx extension to your configuration::

    extensions = [
        'hieroglyph',
    ]

Build your slides
------------------

::

    $ sphinx-build -b slides sourcedir outdir


Where sourcedir is the directory containing the Sphinx conf.py file and outdir
is where you want your slides to output to.



License
=======

Hieroglyph is made available under a BSD license; see LICENSE for details.

Included slide CSS and JavaScript originally based on `HTML 5 Slides`_ licensed
under the Apache Public License.


.. _`HTML 5 Slides`:   http://code.google.com/p/html5slides/

Examples
========

- https://raw.github.com/AndreaCrotti/pyconuk2012_slides/master/zeromq/zeromq.rst




