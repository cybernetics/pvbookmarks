
.. index::
   pair: 1.x.y; IPython



.. _ipython_version.1.0.0:

===============================================================
IPython 1.x.y versions "An Afternoon Hack" 
===============================================================


.. seealso::

   - http://ipython.org/ipython-doc/1/index.html
   - http://ipython.org/ipython-doc/1/whatsnew/version1.0.html


.. contents::
   :depth: 3

Description
============

IPython 1.0 requires Python ≥ 2.6.5 or ≥ 3.2.1.
It does not support Python 3.0, 3.1, or 2.5.

This is a big release.  The principal milestone is the addition of :mod:`IPython.nbconvert`,
but there has been a great deal of work improving all parts of IPython as well.

The previous version (0.13) was released on June 30, 2012,
and in this development cycle we had:

- ~12 months of work.
- ~700 pull requests merged.
- ~600 issues closed (non-pull requests).
- contributions from ~150 authors.
- ~4000 commits.

The amount of work included in this release is so large that we can only cover
here the main highlights; please see our detailed release statistics for links 
to every issue and pull request closed on GitHub
as well as a full list of individual contributors.

It includes

Reorganization
--------------

There have been two major reorganizations in IPython 1.0:

- Added :mod:`IPython.kernel` for all kernel-related code.
  This means that :mod:`IPython.zmq` has been removed,
  and much of it is now in :mod:`IPython.kernel.zmq`,
  some of it being in the top-level :mod:`IPython.kernel`.
- We have removed the `frontend` subpackage,
  as it caused unnecessary depth.  So what was :mod:`IPython.frontend.qt`
  is now :mod:`IPython.qt`, and so on.  The one difference is that
  the notebook has been further flattened, so that
  :mod:`IPython.frontend.html.notebook` is now just `IPython.html`.
  There is a shim module, so :mod:`IPython.frontend` is still
  importable in 1.0, but there will be a warning.
- The IPython sphinx directives are now installed in :mod:`IPython.sphinx`,
  so they can be imported by other projects.

.. _nbconvert1:

NbConvert
---------

The major milestone for IPython 1.0 is the addition of :mod:`IPython.nbconvert` 
tools for converting

IPython notebooks to various other formats.

.. warning::

    nbconvert is α-level preview code in 1.0

To use nbconvert to convert various file formats::

    ipython nbconvert --to html *.ipynb

See ``ipython nbconvert --help`` for more information.
nbconvert depends on `pandoc`_ for many of the translations to and from various formats.


.. _pandoc: http://johnmacfarlane.net/pandoc/

Notebook
--------

Major changes to the IPython Notebook in 1.0:

- The notebook is now autosaved, by default at an interval of two minutes.
  When you press 'save' or Ctrl-S, a *checkpoint* is made, in a hidden folder.
  This checkpoint can be restored, so that the autosave model is strictly safer
  than traditional save. If you change nothing about your save habits,
  you will always have a checkpoint that you have written,
  and an autosaved file that is kept up to date.
- The notebook supports :func:`raw_input` / :func:`input`, and thus also ``%debug``,
  and many other Python calls that expect user input.
- You can load custom javascript and CSS in the notebook by editing the files
  :file:`$(ipython locate profile)/static/custom/custom.{js,css}`.
- Add ``%%html``, ``%%svg``, ``%%javascript``, and ``%%latex`` cell magics
  for writing raw output in notebook cells.
- add a redirect handler and anchors on heading cells, so you can link
  across notebooks, directly to heading cells in other notebooks.
- Images support width and height metadata,
  and thereby 2x scaling (retina support).
- ``_repr_foo_`` methods can return a tuple of (data, metadata),
  where metadata is a dict containing metadata about the displayed object.
  This is used to set size, etc. for retina graphics. To enable retina matplotlib figures,
  simply set ``InlineBackend.figure_format = 'retina'`` for 2x PNG figures,
  in your IPython config file or via the ``%config`` magic.
- Add display.FileLink and FileLinks for quickly displaying HTML links to local files.
- Cells have metadata, which can be edited via cell toolbars.
  This metadata can be used by external code (e.g. reveal.js or exporters),
  when examining the notebook.
- Fix an issue parsing LaTeX in markdown cells, which required users to type ``\\\``,
  instead of ``\\``.
- Notebook templates are rendered with Jinja instead of Tornado.
- ``%%file`` has been renamed ``%%writefile`` (``%%file`` is deprecated).
- ANSI (and VT100) color parsing has been improved in both performance and
  supported values.
- The static files path can be found as ``IPython.html.DEFAULT_STATIC_FILES_PATH``,
  which may be changed by package managers.
- IPython's CSS is installed in :file:`static/css/style.min.css`
  (all style, including bootstrap), and :file:`static/css/ipython.min.css`,
  which only has IPython's own CSS. The latter file should be useful for embedding
  IPython notebooks in other pages, blogs, etc.
- The Print View has been removed. Users are encouraged to test :ref:`ipython
  nbconvert <nbconvert1>` to generate a static view.

Javascript Components
*********************

The javascript components used in the notebook have been updated significantly.

- updates to jQuery (2.0) and jQueryUI (1.10)
- Update CodeMirror to 3.14
- Twitter Bootstrap (2.3) for layout
- Font-Awesome (3.1) for icons
- highlight.js (7.3) for syntax highlighting
- marked (0.2.8) for markdown rendering
- require.js (2.1) for loading javascript

Some relevant changes that are results of this:

- Markdown cells now support GitHub-flavored Markdown (GFM),
  which includes `````python`` code blocks and tables.
- Notebook UI behaves better on more screen sizes.
- Various code cell input issues have been fixed.


Kernel
------

The kernel code has been substantially reorganized.

New features in the kernel:

- Kernels support ZeroMQ IPC transport, not just TCP
- The message protocol has added a top-level metadata field,
  used for information about messages.
- Add a `data_pub` message that functions much like `display_pub`,
  but publishes raw (usually pickled) data, rather than representations.
- Ensure that ``sys.stdout.encoding`` is defined in Kernels.
- Stdout from forked subprocesses should be forwarded to frontends (instead of crashing)

Sub-versions
=============


.. toctree::
   :maxdepth: 3
   
   1.2.1
