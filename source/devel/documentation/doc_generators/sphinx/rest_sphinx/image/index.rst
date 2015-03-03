

.. index::
   pair: Sphinx ; Image
   ! image
   ! Image


.. _sphinx_image:

=================
Image
=================

.. seealso::

   - http://sphinx-doc.org/latest/domains.html#directive-rst:role
   - http://docutils.sourceforge.net/docs/ref/rst/directives.html#images


image
=====

An "image" is a simple picture::

    .. image:: picture.png

The URI for the image source file is specified in the directive argument.
As with hyperlink targets, the image URI may begin on the same line as the
explicit markup start and target name, or it may begin in an indented text block
immediately following, with no intervening blank lines. If there are multiple
lines in the link block, they are stripped of leading and trailing whitespace
and joined together.

Optionally, the image link block may contain a flat field list, the image options.

For example::

    .. image:: picture.jpeg
       :height: 100px
       :width: 200 px
       :scale: 50 %
       :alt: alternate text
       :align: right




Use::

    .. image:: ../images/wiki_logo_openalea.png

to put an image

.. image:: ../images/wiki_logo_openalea.png
    :width: 200px
    :align: center
    :height: 100px
    :alt: alternate text

.. note:: As mentionned earlier, a directive may have options put between two columns:

::

    .. image:: ../images/wiki_logo_openalea.png
        :width: 200px
        :align: center
        :height: 100px
        :alt: alternate text


