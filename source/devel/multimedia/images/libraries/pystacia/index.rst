


.. index::
   Images (libraries)


.. _pystacia_python_image_library:

=============================
pystacia Python image library
=============================

.. seealso:: 

   - http://liquibits.bitbucket.org/
   - :ref:`imagemagick_image_library`

.. image:: logo_pystacia.png

Pystacia is a new image manipulation library born out of practical needs. 
It’s simple, it’s cross-platform, runs on Python 2.5+, 3.x, PyPy and IronPython. 

It’s compact but still appropriate for most of your day to day image handling 
tasks. 

Pystacia leverages powerful :ref:`ImageMagick library <imagemagick_image_library>` as a back-end exposing  easily 
comprehensible Pythonic API.

Here is one of the simplest code snippets showing what you can do with it::

	import pystacia
	image = pystacia.read('example.png')
	image.rescale(320, 240)
	image.rotate(30)
	image.show()
	image.write('output.jpeg')
	# free acquired resources
	image.close()


When saved to simple.py, the above script can be run via::

	$ pip install pystacia
	$ python simple.py


Motivations
===========

.. seealso:: http://liquibits.bitbucket.org/introduction/motivation.html

