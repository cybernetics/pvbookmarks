
.. index::
   pair: sphinx; templating
   pair: sphinx; javascript


.. _sphinx_templating:

============================================================
Sphinx templating
============================================================


.. seealso::

   - http://sphinx-doc.org/templating.html
   - http://sphinx-doc.org/latest/theming.html?highlight=template


.. contents::
   :depth: 3


Add javascript files
====================

.. seealso:: 

   - http://sphinx-doc.org/ext/appapi.html#sphinx.application.Sphinx.add_javascript



Creating themes
===============

.. seealso:: http://sphinx-doc.org/latest/theming.html?highlight=template


As said, themes are either a directory or a zipfile (whose name is the theme
name), containing the following:

* A :file:`theme.conf` file, see below.
* HTML templates, if needed.
* A ``static/`` directory containing any static files that will be copied to the
  output static directory on build.  These can be images, styles, script files.

The :file:`theme.conf` file is in INI format [1]_ (readable by the standard
Python :mod:`ConfigParser` module) and has the following structure:

.. sourcecode:: ini

    [theme]
    inherit = base theme
    stylesheet = main CSS name
    pygments_style = stylename

    [options]
    variable = default value

* The **inherit** setting gives the name of a "base theme", or ``none``.  The
  base theme will be used to locate missing templates (most themes will not have
  to supply most templates if they use ``basic`` as the base theme), its options
  will be inherited, and all of its static files will be used as well.

* The **stylesheet** setting gives the name of a CSS file which will be
  referenced in the HTML header.  If you need more than one CSS file, either
  include one from the other via CSS' ``@import``, or use a custom HTML template
  that adds ``<link rel="stylesheet">`` tags as necessary.  Setting the
  `html_style` config value will override this setting.

* The **pygments_style** setting gives the name of a Pygments style to use for
  highlighting.  This can be overridden by the user in the
  `pygments_style` config value.

* The **options** section contains pairs of variable names and default values.
  These options can be overridden by the user in `html_theme_options`
  and are accessible from all templates as ``theme_<name>``.


.. [1] It is not an executable Python file, as opposed to :file:`conf.py`,
       because that would pose an unnecessary security risk if themes are
       shared.

CSS and roles
==============

.. toctree::
   :maxdepth: 3

   css_and_roles
   
   
TIPS
==============

.. toctree::
   :maxdepth: 3

   tips/index
   
      
