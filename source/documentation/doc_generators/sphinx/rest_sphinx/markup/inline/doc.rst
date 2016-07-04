

.. index::
   pair: sphinx ; doc


.. _sphinx_doc_s:

==============================
doc
==============================


.. seealso:: http://sphinx-doc.org/latest/markup/inline.html?highlight=doc#role-doc



Link to the specified document; the document name can be specified in absolute
or relative fashion.


If no explicit link text is given  the link caption will be the title of the
given document.


Example 1 : local link
=========================

::

    For example, if the reference :doc:`command` occurs in the document inline/index,
    then the link refers to :file:`inline/command`.

For example, if the reference :doc:`command` occurs in the document inline/index,
then the link refers to :file:`inline/command`.


Example 2 : with explicit link text
===================================

::

    reference is :doc:`Index principal </index>` or :doc:`Index local <../index>`


reference is :doc:`Index principal </index>` or :doc:`Index local <../index>`


Example 3 no explicit link text
===============================


::

    reference is :doc:`/index` or :doc:`../index`


reference is :doc:`/index` or :doc:`../index`


