.. highlightlang:: rest


.. index::
   Sphinx toctree


.. _toctree:

=======
toctree
=======

.. seealso:: http://sphinx-doc.org/latest/markup/toctree.html

::

    de  Luc Saffre <luc.saffre@gmail.com>
    heure de l'expéditeur   Envoyé à 14:26 (GMT+02:00). Heure locale : 17:00. ✆
    répondre à  sphinx-dev@googlegroups.com
    à   sphinx-dev <sphinx-dev@googlegroups.com>
    date    18 février 2011 14:26
    objet   [sphinx-dev] toctree glob ordering
    liste de diffusion  <sphinx-dev.googlegroups.com> Filtrer les messages de cette liste de diffusion


Hi,

I just discovered a useful thing that is not documented (at least not
where I would expect it to be at http://sphinx-doc.org/markup/toctree.html)

A `toctree` with `:glob:` flag option not only supports ``*`` but also
the ``?`` wildcard character.

I use this to have the correct sort order in an automatic index for
pages are named using simple numbers, starting from `1.rst`. When I have
more than 9 files (12 for example), then a simple ``*`` would yield a
toctree sorted 1, 11, 12, 2, 3, 4. But if I use the following construct::

 .. toctree::
   :maxdepth: 1
   :glob:

   ?
   ??

then I get the expected order 1, 2, 3, 4, 11, 12.

In short: Sphinx is great :-)


