

.. index::
   pair: Python ; Mingw


.. _py_mingw:

==================
Mingw for python
==================


.. seealso::

   - https://github.com/numpy/numpy/wiki/Mingw-static-toolchain


::

	Sujet : 	Re: [Python-Dev] Microsoft Visual C++ Compiler for Python 2.7
	Date : 	Sat, 27 Sep 2014 15:59:26 +0000 (UTC)
	De : 	Sturla Molden <sturla.molden@gmail.com>
	Pour : 	python-dev@python.org


Christian Heimes <christian@python.org> wrote:

> Is it possible to compile extensions from Python's numerical stack such
> as NumPy, SciPy and SciKit, too?

The official NumPy installer is currently built with VC9, so probably yes.
Other parts of the SciPy stack needs a Fortran compiler as well, so those
might be more tricky. Currently the limitation to Fortran 77 is considered
lifted, Fortran 90 and later will be allowed, so g77 is no longer an
option. In practice you will need Intel ifort or a patched MinGW gfortran. 

Because of this the SciPy community has been creating a customized MinGW
toolchain (including gfortran) for **building binary wheels on Windows**. 

It is patched to make sure that e.g. the MinGW runtime does not 
conflict with the VC9 code in the official Python 2.7 installer 
and that libgfortran uses the correct C runtime. 

The stack alignment is also changed to make it VC9 compatible. 

There was also a customization of the C++ exception handling.
In addition to this the MinGW runtime and libgfortran are statically
linked, so there are no extra runtime DLLs to install.

https://github.com/numpy/numpy/wiki/Mingw-static-toolchain

The toolchain also contains a build of OpenBLAS to use as BLAS and LAPACK
when building NumPy and the SciPy stack. Intel MKL or ATLAS might be
preferred though, due to concerns about the maturity of OpenBLAS.

Sturla Molden
	
