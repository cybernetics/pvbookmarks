
.. index::
   pair: Wheel ; Format
   pair: ZIP; Format
   ! Wheel


.. _wheel:
.. _wheel_format:

===========================
Wheel (ZIP-format archive)
===========================


.. seealso::

   - http://pythonwheels.com/
   - http://wheel.rtfd.org
   - :ref:`wheel_0427`
   - :ref:`python_pep_0427`


Introduction
============

A built-package format for Python.

A ``wheel`` is a ZIP-format archive with a specially formatted filename and 
the .whl extension. 

It is designed to contain all the files for a :ref:`PEP 376 <python_pep_0376>` 
compatible install in a way that is very close to the on-disk format. 

Many packages will be properly installed with only the “Unpack” step 
(simply extracting the file onto sys.path), and the unpacked archive 
preserves enough information to “Spread” (copy data and scripts to their 
final locations) at any later time.

The wheel project provides a ``bdist_wheel`` command for setuptools 
(requires distribute >= 0.6.34). 

Wheel files can be installed with a newer pip from https://github.com/pypa/pip 
or with wheel’s own command line utility.

The wheel documentation is at http://wheel.rtfd.org/. 

The file format is documented in PEP 427 (http://www.python.org/dev/peps/pep-0427/).


Reference implementation
=========================

.. seealso::

   - http://bitbucket.org/dholth/wheel/


The reference implementation is at http://bitbucket.org/dholth/wheel/


Wheel installation
==================

::

    (pythondev) C:\projects\devtools_doc>pip install wheel

::

    Downloading/unpacking wheel
    Downloading wheel-1.0.0a2.tar.gz
    Running setup.py egg_info for package wheel

    no previously-included directories found matching 'wheel\test\*\dist'
    no previously-included directories found matching 'wheel\test\*\build'
    Installing collected packages: wheel
    Running setup.py install for wheel

    no previously-included directories found matching 'wheel\test\*\dist'
    no previously-included directories found matching 'wheel\test\*\build'
    Installing wheel-script.py script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing wheel.exe script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing wheel.exe.manifest script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing wininst2wheel-script.py script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing wininst2wheel.exe script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing wininst2wheel.exe.manifest script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing egg2wheel-script.py script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing egg2wheel.exe script to C:\Users\pvergain\Envs\pythondev\Scripts
    Installing egg2wheel.exe.manifest script to C:\Users\pvergain\Envs\pythondev\Scripts
    Successfully installed wheel
    Cleaning up...


Wheel tutorials
===============

.. toctree::
   :maxdepth: 3
   
   tutorials/index
   


The Story of Wheel
==================

I was impressed with Tarek’s packaging talk at PyCon 2010, and I
admire PEP 345 (Metadata for Python Software Packages 1.2) and PEP 376
(Database of Installed Python Distributions) which standardize a richer
metadata format and show how distributions should be installed on disk. So
naturally with all the hubbub about `packaging` in Python 3.3, I decided
to try it to reap the benefits of a more standardized and predictable
Python packaging experience.

I began by converting `cryptacular`, a password hashing package which
has a simple C extension, to use setup.cfg. I downloaded the Python 3.3
source, struggled with the difference between setup.py and setup.cfg
syntax, fixed the `define_macros` feature, stopped using the missing
`extras` functionality, and several hours later I was able to generate my
`METADATA` from `setup.cfg`. I rejoiced at my newfound freedom from the
tyranny of arbitrary code execution during the build and install process.

It was a lot of work. The package is worse off than before, and it can’t
be built or installed without patching the Python source code itself.

It was about that time that distutils-sig had a discussion about the
need to include a generated setup.cfg from setup.cfg because setup.cfg
wasn’t static enough. Wait, what?

Of course there is a different way to massively simplify the install
process. It’s called built or binary packages. You never have to run
`setup.py` because there is no `setup.py`. There is only METADATA aka
PKG-INFO. Installation has two steps: ‘build package’; ‘install
package’, and you can skip the first step, have someone else do it
for you, do it on another machine, or install the build system from a
binary package and let the build system handle the building. The build
is still complicated, but installation is simple.

With the binary package strategy people who want to install use a simple,
compatible installer, and people who want to package use whatever is
convenient for them for as long as it meets their needs. No one has
to rewrite `setup.py` for their own or the 20k+ other packages on PyPi
unless a different build system does a better job.

Wheel is my attempt to benefit from the excellent distutils-sig work
without having to fix the intractable `distutils` software itself. 

Like METADATA and .dist-info directories but unlike Extension(), it’s
simple enough that there really could be alternate implementations; the
simplest (but less than ideal) installer is nothing more than “unzip
archive.whl” somewhere on sys.path.

If you’ve made it this far you probably wonder whether I’ve heard
of eggs. 

Some comparisons
------------------

* Wheel is an installation format; egg is importable. 
  Wheel archives do not need to include .pyc and are less tied to a 
  specific Python version or implementation. 
  Wheel can install (pure Python) packages built with previous versions 
  of Python so you don’t always have to wait for the packager to catch up.

* Wheel uses .dist-info directories; egg uses .egg-info. 
  Wheel is compatible with the new world of Python `packaging` and the 
  new concepts it brings.

* Wheel has a richer file naming convention for today’s multi-implementation 
  world. 
  A single wheel archive can indicate its compatibility with a number of 
  Python language versions and implementations, ABIs, and system architectures. 
  Historically the ABI has been specific to a CPython release, but when 
  we get a longer-term ABI, wheel will be ready.

* Wheel is **lossless**. 
  The first wheel implementation `bdist_wheel` always generates `egg-info`, 
  and then converts it to a `.whl`. 
  Later tools will allow for the conversion of existing eggs and bdist_wininst 
  distributions.

* Wheel is versioned. 
  Every wheel file contains the version of the wheel specification and 
  the implementation that packaged it. 
  Hopefully the next migration can simply be to Wheel 2.0.

I hope you will benefit from wheel.



News
=====

.. toctree::
   :maxdepth: 3

   news/index



