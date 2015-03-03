

.. index::
   pair: Rest Documentation; docutils


.. _docutils_rest_documentation:

============================
rst2html
============================


.. seealso::

   - http://docutils.sourceforge.net/docs/user/tools.html#rst2html-py
   - http://docutils.sourceforge.net/docs/howto/html-stylesheets.html


.. contents::
   :depth: 3
   

Description
===========

The rst2html.py front end reads standalone reStructuredText source files and 
produces HTML 4 (XHTML 1) output compatible with modern browsers that support 
cascading stylesheets (CSS). 

A stylesheet is required for proper rendering; a simple but complete stylesheet 
is installed and used by default (see Stylesheets below).

For example, to process a reStructuredText file "test.txt" into HTML:

rst2html.py test.txt test.html

Now open the "test.html" file in your favorite browser to see the results. 
To get a footer with a link to the source file, date & time of processing, 
and links to the Docutils project, add some options::

    rst2html.py -stg test.txt test.html

Stylesheets
============

rst2html.py inserts into the generated HTML a cascading stylesheet (or a link 
to a stylesheet, when passing the "--link-stylesheet" option). 

A stylesheet is required for proper rendering. 

The default stylesheet (docutils/writers/html4css1/html4css1.css, located in 
the installation directory) is provided for basic use. 

To use a different stylesheet, you must specify the stylesheet's location with 
a "--stylesheet" (for a URL) or "--stylesheet-path" (for a local file) 
command-line option, or with configuration file settings 
(e.g. ./docutils.conf or ~/.docutils). 

To experiment with styles, please see the `guide to writing HTML (CSS) stylesheets`_ 
for Docutils.


.. _`guide to writing HTML (CSS) stylesheets`:  http://docutils.sourceforge.net/docs/howto/html-stylesheets.html













