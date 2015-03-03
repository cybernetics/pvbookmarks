

.. index::
   pair: Python ; Wand
   ! Wand


.. _wand:

==========================
Wand
==========================


.. seealso::

   - http://docs.wand-py.org
   - https://github.com/dahlia/wand
   - https://stackoverflow.com/questions/19470099/view-pdf-image-in-an-ipython-notebook
   
   

Wand
====

Wand is a :mod:`ctypes`-based simple ImageMagick_ binding for Python. ::

    from wand.image import Image
    from wand.display import display

    with Image(filename='mona-lisa.png') as img:
        print(img.size)
        for r in 1, 2, 3:
            with img.clone() as i:
                i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
                i.rotate(90 * r)
                i.save(filename='mona-lisa-{0}.png'.format(r))
                display(i)

You can install it from PyPI_ (and it requires MagickWand library):

.. sourcecode:: bash

   $ apt-get install libmagickwand-dev
   $ pip install Wand

.. _ImageMagick: http://www.imagemagick.org/
.. _PyPI: https://pypi.python.org/pypi/Wand


Why just another binding?
-------------------------

There are already many MagickWand API bindings for Python, however they
are lacking something we need:

- Pythonic and modern interfaces
- Good documentation
- Binding through :mod:`ctypes` (not C API) --- we are ready to go PyPy!
- Installation using :program:`pip` or :program:`easy_install`
