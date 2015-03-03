

.. index::
   pair: Wheel; Distlib


.. _distlib_wheel_tutorials:

========================
Distlib Wheel tutorials
========================


.. seealso::

   - https://distlib.readthedocs.org/en/latest/tutorial.html#using-the-wheel-api
   
   
   
You can use the ``distlib.wheel`` package to build and install from files in
the Wheel format, defined in :ref:`427 <python_pep_0427>`.

Building wheels
================

.. index::
   pair: building; wheels


Building wheels is straightforward::

    from distlib.wheel import Wheel

    wheel = Wheel()

    # Set the distribution's identity
    wheel.name = 'name_of_distribution'
    wheel.version = '0.1'

    # Indicate where the files to go in the wheel are to be found
    paths = {
        'prefix': '/path/to/installation/prefix',
        'purelib': '/path/to/purelib',  # only one of purelib
        'platlib': '/path/to/platlib',  # or platlib should be set
        'scripts': '/path/to/scripts',
        'headers': '/path/to/headers',
        'data': '/path/to/data',
    }

    wheel.dirname = '/where/you/want/the/wheel/to/go'
    # Now build
    wheel.build(paths)

If the ``'data'``, ``'headers'`` and ``'scripts'`` keys are absent, or point to
paths which don't exist, nothing will be added to the wheel for these
categories. The ``'prefix'`` key and one of ``'purelib'`` or ``'platlib'``
*must* be provided, and the paths referenced should exist.
