

.. index::
   pair: Sphinx ; Deprecated
   ! Deprecated


.. _sphinx_deprecated:

==========================
deprecated
==========================


.. seealso::

   - http://sphinx-doc.org/latest/markup/para.html?highlight=warning#directive-warning



.. rst:directive:: .. deprecated:: version

   Similar to :rst:dir:`versionchanged`, but describes when the feature was
   deprecated.  An explanation can also be given, for example to inform the
   reader what should be used instead.  Example::

      .. deprecated:: 3.1
         Use :func:`spam` instead.

.. deprecated:: 3.1
   Use :func:`spam` instead.
