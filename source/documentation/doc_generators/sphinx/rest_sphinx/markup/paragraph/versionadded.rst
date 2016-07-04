

.. index::
   pair: sphinx ; versionadded


.. _versionadded:

=============
versionadded
=============


.. seealso::

   - http://sphinx-doc.org/latest/markup/para.html?highlight=versionadded#directive-versionadded


This directive documents the version of the project which added the described
feature to the library or C API. When this applies to an entire module, it
should be placed at the top of the module section before any prose.

The first argument must be given and is the version in question; you can add a
second argument consisting of a brief explanation of the change.

Example::

    .. versionadded:: 2.5
       The *spam* parameter.

.. versionadded:: 2.5
   The *spam* parameter.

Note that there must be no blank line between the directive head and the
explanation; this is to make these blocks visually continuous in the markup.

