
.. index::
   pair: sphinx; CSS
   pair: sphinx; default.css
   pair: sphinx; role

.. _sphinx_css:

============================================
sphinx CSS and custom-interpreted-text-roles
============================================

.. seealso::

   - http://docutils.sourceforge.net/docs/ref/rst/directives.html#custom-interpreted-text-roles
   - http://sphinx-doc.org/latest/config.html?highlight=html_static_path#confval-html_static_path




role:: underlined
=================

I've added

::


    span.underlined {
        text-decoration: underline;
    }


to the :file:`default.css` CSS file.


and

::

    .. role:: underlined

    :underlined:`test underlined`



to the test.rst and it is underlined!

Thank You!



Tip: vertical text
==================

::

    From: Boris Kheyfets <kheyfboris@gmail.com>
    Date: 2012/9/5
    Subject: [sphinx-dev] Tip: vertical text
    To: sphinx-dev@googlegroups.com


Here's a minimal working example::

    css:
    span.vertical {
        writing-mode:tb-rl;
        -webkit-transform:rotate(270deg);
        -moz-transform:rotate(270deg);
        -o-transform: rotate(270deg);
        display:block;
        width:20px;
        height:20px;
    }



::


    rst:
    .. role:: vertical

    :vertical:`test`




default.css file
================

**html_static_path**

   A list of paths that contain custom static files (such as style sheets or
   script files).  Relative paths are taken as relative to the configuration
   directory.  They are copied to the output directory after the theme's static
   files, so a file named :file:`default.css` will overwrite the theme's
   :file:`default.css`.

   .. versionchanged:: 0.4
      The paths in `html_static_path` can now contain subdirectories.

   .. versionchanged:: 1.0
      The entries in `html_static_path` can now be single files.
