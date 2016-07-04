



============================
tinkerer 0.2
============================


- Support for Drafts.
- Fixes for cross-references and embedded images which were not displaying
  correctly on home page and RSS feed.
- Ensure Tinkerer runs only from the blog root directory unless when setting up
  a new blog (this prevents accidental deletes and mysterious exceptions).
- Minimal support for documentation - prev and next links will be displayed on
  pages under doc/ or docs/ path.
- Many other small extension fixes.
- CSS fixes (gradient not showing in Firefox, page not scaling correctly on
  retina displays).


Upgrading from 0.1
==================


There are a couple of steps required if upgrading from 0.1:

In your conf.py replace::

    # Add file patterns to exclude from build
    exclude_patterns = []

with::

    # Add file patterns to exclude from build
    exclude_patterns = ["drafts/*"]



This will make Sphinx stop warning you about drafts not being included in the build.

Make sure your master.rst file ends with a blank line. If not, append a blank l
ine at the end of it.

Thank You!

A big Thank You to everyone who showed interest in the project and for the
valuable feedback you provided.


