

.. index::
   pair: Sphinx ; literalinclude
   pair: Sphinx ; encoding
   pair: Sphinx ; emphasize-lines
   pair: literalinclude ; emphasize-lines
   pair: literalinclude ; linenos
   pair: literalinclude ; lineno-start
   pair: literalinclude ; diff


.. _literal_include:

==============
literalinclude
==============

.. seealso::

   - http://sphinx-doc.org/markup/code.html
   - http://pygments.org/docs/lexers/


.. contents::
   :depth: 3


``rst:directive:: .. literalinclude:: filename``
================================================

.. rst:directive:: .. literalinclude:: filename

   Longer displays of verbatim text may be included by storing the example text in
   an external file containing only plain text.  The file may be included using the
   ``literalinclude`` directive. For example, to include the Python source file
   :file:`example.py`, use::

      .. literalinclude:: example.py

   The file name is usually relative to the current file's path.  However, if it
   is absolute (starting with ``/``), it is relative to the top source
   directory.

   Tabs in the input are expanded if you give a ``tab-width`` option with the
   desired tab width.



.. _linenos:

``:linenos:``
==============

   The directive also supports the ``linenos`` flag option to switch on line
   numbers, and a ``language`` option to select a language different from the
   current file's standard language.  Example with options::

      .. literalinclude:: example.rb
         :language: ruby
         :linenos:


.. _lineno_start:

``:lineno-start:``
===========================

.. seealso::

   - http://sphinx-doc.org/latest/changes.html?highlight=literalinclude#release-1-3-in-development

.. versionadded:: 1.3
   The ``lineno-start`` option.


The first line number can be selected with the lineno-start option. 
If present, linenos is automatically activated as well.


    .. literalinclude:: example.py
       :lineno-start: 15


.. literalinclude:: example.py
   :lineno-start: 15




.. _literal_include_diff:

``:diff:``
===========================

.. versionadded:: 1.3
   The ``diff`` option.


If you want to show the diff of the code, you can specify the old file by 
giving a diff option::

    .. literalinclude:: example.py
       :diff: example.py.orig


.. literalinclude:: example.py
   :diff: example.py.orig


.. _literal_caption:

``:caption:``
===========================

.. versionadded:: 1.3
   The ``caption`` option.


literalinclude supports the ``caption`` option, with the additional feature that 
if you leave the value empty, the shown filename will be exactly the one given 
as an argument::

    .. literalinclude:: example.py
       :linenos: 
       :caption:


.. literalinclude:: example.py
   :linenos: 
   :caption: 



.. _emphasize_lines:

``:emphasize-lines:``
=====================

    Additionally, an ``emphasize-lines`` option can be given to have Pygments
    emphasize particular lines::

        .. code-block:: python
           :emphasize-lines: 3,5

           def some_function():
               interesting = False
               print 'This line is highlighted.'
               print 'This one is not...'
               print '...but this one is.'


.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'


.. versionchanged:: 1.1
   ``emphasize-lines`` has been added.


.. _lines:

``:lines: xxx``
==================


   Alternately, you can specify exactly which lines to include by giving a
   ``lines`` option::

      .. literalinclude:: example.py
         :lines: 1,3,5-10,20-

   This includes the lines 1, 3, 5 to 10 and lines 20 to the last line.

   You can combine ``lines`` with  :ref:`emphasize_lines`


``:encoding: latin-1``
=======================

.. seealso:: http://sphinx-doc.org/config.html#confval-source_encoding


   Include files are assumed to be encoded in the source_encoding.
   If the file has a different encoding, you can specify it with the
   ``encoding`` option::

      .. literalinclude:: example.py
         :language: python
         :encoding: latin-1



``:pyobject: xxx``
==================

   The directive also supports including only parts of the file.  If it is a
   Python module, you can select a class, function or method to include using
   the ``pyobject`` option::

      .. literalinclude:: example.py
         :pyobject: Timer.start

   This would only include the code lines belonging to the ``start()`` method in
   the ``Timer`` class within the file.




``:language: python``
=====================

.. seealso::

   - http://pygments.org/docs/lexers/
   - http://sphinx-doc.org/config.html#confval-highlight_language
   - http://sphinx-doc.org/markup/code.html#code-examples


The valid values for the highlighting language are:

- none (no highlighting)
- python (the default when highlight_language isn’t set)
- guess (let Pygments guess the lexer based on contents, only works with certain well-recognizable languages)
- rest
- c
- ... and any other lexer name that Pygments supports.




