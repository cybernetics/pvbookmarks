

.. index::
   pair: sphinx ; code-block
   pair: sphinx ; pygments

.. _rest_code_block:

=================================
code-block (pygments, highlight)
=================================

.. seealso:: 

   - http://sphinx-doc.org/latest/markup/code.html#index-0
   - http://pygments.org/docs/lexers/


Sphinx does syntax highlighting using the Pygments library.


For documents that have to show snippets in different languages, there's also
a :rst:dir:`code-block` directive that is given the highlighting language
directly::

.. code-block:: python

   Some python code.


You can specify different highlighting for a code block using the following syntax:

Default highlighter
===================

::

	With two colons you start a code block using the default highlighter::

		# Some Python code here
		# The language defaults to Python, we don't need to set it
		if 1 == 2:
			pass


With two colons you start a code block using the default highlighter::

    # Some Python code here
    # The language defaults to Python, we don't need to set it
    if 1 == 2:
        pass


	

python highlighter
==================

You can specify the language used for syntax highlighting by using code-block:

::

	.. code-block:: python

		if "foo" == "bar":
			# This is Python code
			pass


.. code-block:: python

    if "foo" == "bar":
        # This is Python code
        pass

xml highlighter
===============

For example, to specify XML:

::

	.. code-block:: xml

		<somesnippet>Some XML</somesnippet>


.. code-block:: xml

    <somesnippet>Some XML</somesnippet>


console highlighter
===================


... or UNIX shell:

::

	.. code-block:: console

	   # A comment
	   sh myscript.sh


.. code-block:: console

   # A comment
   sh myscript.sh


ini highlighter
==================

... or a buildout.cfg:

::

	.. code-block:: ini

	   [some-part]
	   # A random part in the buildout
	   recipe = collective.recipe.foo
	   option = value


.. code-block:: ini

   [some-part]
   # A random part in the buildout
   recipe = collective.recipe.foo
   option = value


pycon python console highlighter
=====================================

... or interactive Python:

::

	.. code-block:: pycon

	   >>> class Foo:
	   ...     bar = 100
	   ...
	   >>> f = Foo()
	   >>> f.bar
	   100
	   >>> f.bar / 0
	   Traceback (most recent call last):
		 File "<stdin>", line 1, in <module>
	   ZeroDivisionError: integer division or modulo by zero



.. code-block:: pycon

   >>> class Foo:
   ...     bar = 100
   ...
   >>> f = Foo()
   >>> f.bar
   100
   >>> f.bar / 0
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ZeroDivisionError: integer division or modulo by zero


highlighting mode for the whole document
========================================


Setting the highlighting mode for the whole document::

    .. highlight:: console
    

.. highlight:: console

All code blocks in this doc use console highlighting by default::

   some shell commands

If syntax highlighting is not enabled for your code block, you probably have a 
syntax error and Pygments will fail silently.

The full list of lexers and associated short names is here: http://pygments.org/docs/lexers/

