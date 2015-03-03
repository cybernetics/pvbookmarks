
.. index::
   pair:  doxygen; 1.8.0
   pair: UML; notations



===========================
Doxygen 1.8.0 (25-02-2012)
===========================


.. seealso:: http://www.stack.nl/~dimitri/doxygen/changelog.html


.. contents::
   :depth: 3


Changes
=======

Auto list items can now consist of multiple paragraphs.

The indentation of the (first line) of a new paragraph detemines to which list
item the paragraph belongs or if it marks the end of the list.

When UML_LOOK is enabled, relations shown on the edge of a graph are not shown
as attributes (conform to the UML notation)

Updated the manual and improved the look
-----------------------------------------

Made the contents in the navigation tree more consistent for groups, pages with
subpages, and grouped subpages.

id 669079: Latex: made the margins of latex page layout smaller using the
geometry package.

doxytag removed
===============

The tool doxytag has been declared obsolete and is removed (it wasn't working
properly anyway).
Same goes for the installdox script.

Updated the copyright in source code and doxywizard "about" to 2012.
id 668008: HTML version of the manual now has the treeview enabled for easier navigation.

New features
============

Markdown support
----------------

.. seealso::

   - http://michelf.com/projects/php-markdown/extra/#table
   - http://freewisdom.org/projects/python-markdown/Fenced_Code_Blocks


Added support for :ref:`Markdown <markdown>` formatting. This is enabled by
default, but can be disabled by setting MARKDOWN_SUPPORT to NO.

When enabled the following is processed differently:

- tabs are converted to spaces according to TAB_SIZE.
- blockquotes are created for lines that start with one or more >'s (amount of >'s
  detemine the indentation level).
- emphasis using *emphasize this* or emphasis this or strong emphasis using
  **emphasis this**. Unlike classic Markdown 'some_great_indentifier' is not touched.
- code spans can be created using back-ticks, i.e. `here's an example`
- Using three or more -'s or * 's alone on a line with only spaces will produce
  a horizontal ruler.
- A header can be created by putting a ===== (for h1) or ----- (for h2) on the
  next line or by using 1 to 6 #'s at the start of a line for h1-h6.
- auto lists item can also start with + or * instead of only -
- ordered lists can be made using 1. 2. ... labels.
- verbatim blocks can be produced by indenting 4 additional spaces.
  Note that doxygen uses a relative indent of 4 spaces, not an absolute indent
  like Markdown does.
- Markdown style hyperlinks and hyperlink references.
- Simple tables can be created using the `Markdown Extra format`_.
- `Fenced code blocks`_ are also supported, include language selection.
- files with extension .md or .markdown are converted to related pages.
- See the section about Markdown support in the manual for details.


.. _`Markdown Extra format`:  http://michelf.com/projects/php-markdown/extra/#table
.. _`Fenced code blocks`:  http://freewisdom.org/projects/python-markdown/Fenced_Code_Blocks


It is now possible to add user defined tabs or groups of tabs to the navigation
menu using the layout file (see the section of the manual about customizing the
output for details).

\tableofcontents
-----------------

Added new command \tableofcontents (or [TOC] if you prefer Markdown) which can
be used in a related page with sections to produce a table of contents at the
top of the HTML page (for other formats the command has no effect).

When using SVG images and INTERACTIVE_SVG is enabled, a print icon will be
visible along with the navigation controls to facilitate printing of the part
of the graph that is visible on screen.

Added obfuscation of email addresses for the HTML output to make email
harvesting more difficult.

targets for 64 bits
-------------------

Added build targets for 64 bit Windows (thanks to Vladimir Simonov).
The installer script is also updated to install a 64 bit version of doxygen
on 64 bit systems and the 32 bit version on 32 bit systems.

Added support for using the HTML tag <blockquote> in comments.

Included patch by Gauthier Haderer that fixes some issues with the dbus XML parser.

Added support for Markdown style fenced code blocks.

Added option to @code command to force parsing and syntax highlighting according
to a particular language.

Section of pages are now added to the navigation index.

Added support for cell alignment and table header shading in LaTeX and RTF output.

Added -d filteroutput option to show the output of an input filter (thanks to
Albert for the patch).

id 668010: Latex: for Windows doxygen new generates a makepdf.bat file in the
latex output dir to create the latex documentation.


