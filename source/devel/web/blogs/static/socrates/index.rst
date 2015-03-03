.. module:: Documenting
    :synopsis: Documenting with socrates


.. index::
   ! socrates
   pair: Documentation ; socrates

.. _documenting_with_socrates:

==========================
Documenting with socrates
==========================

.. seealso::

   - http://pypi.python.org/pypi/socrates
   - http://readthedocs.org/docs/socrates/en/latest/index.html



Socrates is a simple static site generator. It's geared towards blogs.

You write your posts in your favorite plain text to HTML language
(e.g. Markdown, textile, reStructuredText) and save them as text files on your
harddrive.

Socrates then takes them, and creates a full HTML site for you.

For free, you will get a home page which lists:

- latest posts,
- single post pages,
- category pages,
- archive pages,
- an about page
- and an atom feed.


Features
========

- Familiar Django and Jinja2 templates
- Simple install via pip
- Markdown, reStructuredText, Textile support
- YAML configuration
- Atom feed
- Github pages compatible
- Real HTML punctuation


Documentation
=============

.. seealso:: http://readthedocs.org/docs/socrates/en/latest/index.html

The documentation is contained within the docs directory and is written in
reStructuredText using Sphinx.

The documentation is easily read in a standard text editor.

However, you can build an HTML version like so:

$ pip install sphinx
$ cd docs/
$ make html
$ open _build/html/index.html

Or, you can view the online version of the `latest documentation`_.


.. _`latest documentation`:  http://readthedocs.org/docs/socrates/en/latest/index.html



