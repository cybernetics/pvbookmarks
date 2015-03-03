
.. index::
   pair: Tor ; Stem
   ! Stem

.. _stem:

====================
Stem
====================

.. seealso::

   - https://stem.torproject.org/index.html
   - https://git.torproject.org/stem.git


.. contents::
   :depth: 3

Introduction
=============

.. seealso:: https://gitweb.torproject.org/stem.git/blob_plain/HEAD:/docs/index.rst

Stem is a python controller library for `Tor <https://www.torproject.org/>`_. 
Like its predecessor, `TorCtl <https://gitweb.torproject.org/pytorctl.git>`_, 
it uses Tor's `control protocol <https://gitweb.torproject.org/torspec.git/blob/HEAD:/control-spec.txt>`_ to 
help developers program against the Tor process, enabling them to build 
things similar to `Vidalia <https://www.torproject.org/getinvolved/volunteer.html.en#project-vidalia>`_ 
and `arm <http://www.atagar.com/arm/>`_.


.. _stem_sphinx_haiku:

Stem sphinx Haiku theme
========================


.. seealso::

   - :ref:`haiku_theme`


::

    Sujet:  [sphinx-users] Navbar Menu for Haiku Theme
    Date :  Mon, 8 Apr 2013 11:57:12 -0700
    De :    Damian Johnson <atagar@torproject.org>
    Répondre à :    sphinx-users@googlegroups.com
    Pour :  sphinx-users@googlegroups.com


Hi all. This last weekend I sunk a little time into replacing the
default 'Previous / Contents / Next' header in the Haiku theme with a
css-based dropdown menu...

https://stem.torproject.org/

Is this something that upstream would be interested in incorporating?
If so then all it would take is...

1. A little additional css (see below).
2. Block statement for the header and footer sections where the nav()
   macro is used (presently those are just within the content block so
   replacing them pretty much requires the user to fork the layout).
3. Instructions for the site on how to overwrite the added navbar
   block with their menu.

I can send a commit upstream if there's interest. Here's the commit
where I did this for my site...

https://gitweb.torproject.org/stem.git/commitdiff/c719b1e5680898e9d1f6ede953b3169d12580f64

Cheers! -Damian

