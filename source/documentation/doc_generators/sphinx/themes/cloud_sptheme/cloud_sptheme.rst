
.. index::
   ! Cloud sptheme
   pair: ReadTheDocs; Cloud theme


.. _cloud_sptheme:
.. _cloud_theme:

===================
Sphinx cloud theme
===================

.. seealso::

   - http://packages.python.org/cloud_sptheme/
   - http://inasafe.readthedocs.org/en/latest/index.html
   - https://bitbucket.org/ecollins/cloud_sptheme
   - :ref:`passlib_sphinx`


.. contents::
   :depth: 3


Introduction
============

This page contains examples of various features of the Cloud theme.
It's mainly useful internally, to make sure everything is displaying correctly.


Installation
============

::

    pip install -U cloud_sptheme


Inline Text
=============

::

    Inline literal: ``literal text``.


Inline literal: ``literal text``.

::

    External links are prefixed with an arrow: `<http://www.google.com>`_.


External links are prefixed with an arrow: `<http://www.google.com>`_.

::

    But email links are not prefixed: bob@example.com.


But email links are not prefixed: bob@example.com.


::

    Issue tracker link: :issue:`5`.



::

    extensions = [
        # http://pythonhosted.org/cloud_sptheme/index.html#extensions
        # https://bitbucket.org/ecollins/cloud_sptheme

        'cloud_sptheme.ext.issue_tracker',
    ]

    # set path to issue tracker:
    issue_tracker_url = "https://bitbucket.org/ecollins/cloud_sptheme/issue/{issue}"



Admonition Styles
=================

::

    .. note::
        This is a note.


.. note::
    This is a note.


::

    .. warning::

        This is warning.

.. warning::

    This is warning.

::

    .. seealso::

        This is a "see also" message.

.. seealso::

    This is a "see also" message.


::

    .. todo::

        This is a todo message.

        With some additional next on another line.


.. todo::

    This is a todo message.

    With some additional next on another line.


::

    .. deprecated:: XXX This is a deprecation warning.



.. deprecated:: XXX This is a deprecation warning.


::

    .. rst-class:: floater

    .. note::
        This is a floating note.


.. rst-class:: floater

.. note::
    This is a floating note.


Table Styles
============

::

    extensions = [
        # http://pythonhosted.org/cloud_sptheme/index.html#extensions
        # https://bitbucket.org/ecollins/cloud_sptheme

        'cloud_sptheme.ext.table_styling',
    ]


::

    .. table:: Normal Table


.. table:: Normal Table

    =========== =========== ===========
    Header1     Header2     Header3
    =========== =========== ===========
    Row 1       Row 1       Row 1
    Row 2       Row 2       Row 2
    Row 3       Row 3       Row 3
    =========== =========== ===========

::

    .. rst-class:: plain

    .. table:: Plain Table (no row shading)


.. rst-class:: plain

.. table:: Plain Table (no row shading)

    =========== =========== ===========
    Header1     Header2     Header3
    =========== =========== ===========
    Row 1       Row 1       Row 1
    Row 2       Row 2       Row 2
    Row 3       Row 3       Row 3
    =========== =========== ===========

::

    .. rst-class:: centered

    .. table:: Centered Table


.. rst-class:: centered

.. table:: Centered Table

    =========== =========== ===========
    Header1     Header2     Header3
    =========== =========== ===========
    Row 1       Row 1       Row 1
    Row 2       Row 2       Row 2
    Row 3       Row 3       Row 3
    =========== =========== ===========

::

    .. rst-class:: fullwidth

    .. table:: Full Width Table


.. rst-class:: fullwidth

.. table:: Full Width Table

    =========== =========== ===========
    Header1     Header2     Header3
    =========== =========== ===========
    Row 1       Row 1       Row 1
    Row 2       Row 2       Row 2
    Row 3       Row 3       Row 3
    =========== =========== ===========


::

    .. table:: Table Styling Extension
        :widths: 1 2 3
        :header-columns: 1
        :column-alignment: left center right
        :column-dividers: none single double single
        :column-wrapping: nnn



::

    .. rst-class:: html-toggle

    .. _toggle-test-link:



.. rst-class:: html-toggle

.. _toggle-test-link:

Toggleable Section
==================

This section is collapsed by default.
But if a visitor follows a link to this section or something within it
(such as :ref:`this <toggle-test-link>`), it will automatically be expanded.

::

    .. rst-class:: html-toggle expanded


.. rst-class:: html-toggle expanded

Toggleable Subsection
---------------------

Subsections can also be marked as toggleable.
This one should be expanded by default.

::

    .. rst-class:: emphasize-children


.. rst-class:: emphasize-children

Section With Emphasized Children
================================

Mainly useful for sections with many long subsections,
where a second level of visual dividers would be useful.

Child Section
----------------

Should be have slightly lighter background, and be indented.

::

    .. rst-class:: html-toggle


.. rst-class:: html-toggle

Toggleable Subsection
---------------------

Test of emphasized + toggleable styles. Should be collapsed by default.

ReadTheDocs
===========

.. seealso::

   - https://github.com/fedora-infra/fedmsg/blob/develop/doc


To use this theme on `<http://readthedocs.org>`_:

1. If it doesn't already exist, add a pip ``requirements.txt`` file to
   your documentation (e.g. alongside ``conf.py``).
   It should contain a minimum of the following lines::

       sphinx
       cloud_sptheme

   ... as well as any other build requirements for your project's documentation.

2. When setting up your project on ReadTheDocs, enter the path to ``requirements.txt``
   in the *requirements file* field on the project configuration page.

3. ReadTheDocs will now automatically download the latest version of :mod:`!cloud_sptheme`
   when building your documentation.


Project using cloud_sptheme
===========================

Fedmsg (on read the docs)
-------------------------

.. seealso::

   - :ref:`fedmsg_cloud_theme`

Passlib conf.py
---------------

.. literalinclude:: passlib/conf.txt
  :linenos:

