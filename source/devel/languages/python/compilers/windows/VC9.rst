

.. index::
   pair: Python ; VC9


.. _py_VC9:

=======================
VC9 for Python 
=======================

.. seealso::

   - https://mail.python.org/pipermail/distutils-sig/2014-September/024885.html

.. contents::
   :depth: 3

Annonce de Steve Dower le 27 septembre 2014
============================================


.. seealso::

   - :ref:`visual_c_2008`
   - http://aka.ms/vcpython27

::

	Hi all,

	(This is advance notice since people on this list will be interested. 
	Official announcements are coming when setuptools makes their next 
	release.)

	Microsoft has released a compiler package targeting Python 2.7 
	(i.e. VC9). 
	We've produced this package to help library developers build wheels 
	for Windows, but also to help users unblock themselves when they need 
	to build C extensions themselves.

	The Microsoft Visual C++ Compiler for Python 2.7 is available 
	from: http://aka.ms/vcpython27

	This package contains all the tools and headers required to build 
	C extension modules for Python 2.7 32-bit and 64-bit (note that some 
	extension modules require 3rd party dependencies such as OpenSSL or 
	libxml2 that are not included). 
	Other versions of Python built with Visual C++ 2008 are also supported.

	You can install the package without requiring administrative 
	privileges and, with the latest version of setuptools (when it releases), 
	use tools such as pip, wheel, or a setup.py file to produce binaries 
	on Windows.

	Unfortunately, this package isn't necessarily going to help with 
	building CPython 2.7 itself, as the build process is complicated 
	and Visual Studio 2008 is practically required. 
	However, as most people aren't building CPython on Windows, this 
	isn't a huge issue. This compiler package should be sufficient for 
	most extension modules.

	I should also point out that VC9 is no longer supported by Microsoft. 
	This means there won't be any improvements or bug fixes coming, and 
	there's no official support offered. 
	Feel free to contact me directly <steve.dower@microsoft.com> if there 
	are issues with the package.

	Cheers,
	Steve



	I'll post this on the various other lists later, but I promised 
	distutils-sig first taste, especially since the discussion has been 
	raging for a few days (if you're following the setuptools repo, you may 
	already know, but let me take the podium for a few minutes anyway :) )

	Microsoft has released a compiler package for Python 2.7 to make it 
	easier for people to build and distribute their C extension modules 
	on Windows. 
	The Microsoft Visual C++ Compiler for Python 2.7 (a.k.a. VC9) is available 
	from: http://aka.ms/vcpython27

	This package contains all the tools and headers required to build C 
	extension modules for Python 2.7 32-bit and 64-bit (note that some
	extension modules require 3rd party dependencies such as OpenSSL or 
	libxml2 that are not included). 
	Other versions of Python built with Visual C++ 2008 are also supported, 
	so "Python 2.7" is just advertising - it'll work fine with 2.6 and 3.2.

	You can install the package without requiring administrative privileges 
	and, with the latest version of setuptools (from the source repo  
	there's no release yet), use tools such as pip, wheel, or a setup.py 
	file to produce binaries on Windows.

	The license prevents redistribution of the package itself (obviously you 
	can do what you like with the binaries you produce) and IANAL but there 
	should be no restriction on using this package on automated build systems 
	under the usual one-developer rule (http://stackoverflow.com/a/779631/891 
	in effect, the compilers are licensed to one user who happens to be using 
	it on a remote machine).

	My plan is to keep the download link stable so that automated scripts 
	can reference and install the package. I have no idea how long that will 
	last... :)

	Our intent is to heavily focus on people using this package to produce
	wheels rather than trying to get this onto every user machine. 

	Binary distribution is the way Windows has always worked and we want to 
	encourage that, though we do also want people to be able to unblock 
	themselves with these compilers.

	I should also point out that VC9 is no longer supported by Microsoft. 

	This means there won't be any improvements or bug fixes coming, and 
	there's no official support offered. Feel free to contact me directly 
	<steve.dower@microsoft.com> if there are issues with the package.

	Cheers,
	Steve


::

	-------- Message transféré --------
	Sujet : 	Re: [Distutils] Microsoft Visual C++ Compiler for Python 2.7
	Date : 	Sat, 27 Sep 2014 15:32:45 +0000
	De : 	Steve Dower <Steve.Dower@microsoft.com>
	Pour : 	Piotr Dobrogost <p@2014.dobrogost.net>
	Copie à : 	distutils sig <distutils-sig@python.org>


	It's free (VC Express 2008 is behind a pay wall these days)
	It's small (85MB download, 300mb on installed)
	It's a per-user install with no reboot required

	If you have the permissions, time, and access for VC Express 2008, it 
	gains you nothing. You're not the intended target audience (I thought I 
	had that wording in the announcement, but I guess not).

	Most people don't have or want Visual Studio installed on their machine, 
	or need to install on a machine where they're not admin (think university 
	student on a lab machine who needs Cython).


::

	-------- Message transféré --------
	Sujet : 	Re: [Python-Dev] Microsoft Visual C++ Compiler for Python 2.7
	Date : 	Sat, 27 Sep 2014 15:38:36 +0000
	De : 	Steve Dower <Steve.Dower@microsoft.com>
	Pour : 	Antoine Pitrou <solipsis@pitrou.net>, python-dev@python.org <python-dev@python.org>


	The SDK compilers are not easily fixable (I've tried). 
	The installation is basically corrupt as far as the non-x86 compilers 
	are concerned.

	The package we just put out is exactly the same files as the SDK with 
	those issues fixed. There's no reason to encourage the SDK at all now 
	(which was the point of the whole exercise from my point of view).

	Cheers,
	Steve
	

Is it possible to compile extensions from Python's numerical stack such as NumPy, SciPy and SciKit, too ?	
==========================================================================================================


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
		

setuptools/tests/test_msvc9compiler.py
=======================================

.. seealso::

   - https://bitbucket.org/pypa/setuptools/commits/2e6ea8a0635a4667aed6ba072fe718f8cf3e0521

 
::

	"""msvc9compiler monkey patch test

	This test ensures that importing setuptools is sufficient to replace
	the standard find_vcvarsall function with our patched version that
	finds the Visual C++ for Python package.
	"""

	import os
	import shutil
	import sys
	import tempfile
	import unittest
	import distutils.errors

	# importing only setuptools should apply the patch
	__import__('setuptools')

	class MockReg:
		"""Mock for distutils.msvc9compiler.Reg. We patch it
		with an instance of this class that mocks out the
		functions that access the registry.
		"""

		def __init__(self, hkey_local_machine={}, hkey_current_user={}):
			self.hklm = hkey_local_machine
			self.hkcu = hkey_current_user

		def __enter__(self):
			self.original_read_keys = distutils.msvc9compiler.Reg.read_keys
			self.original_read_values = distutils.msvc9compiler.Reg.read_values

			_winreg = getattr(distutils.msvc9compiler, '_winreg', None)
			winreg = getattr(distutils.msvc9compiler, 'winreg', _winreg)

			hives = {
				winreg.HKEY_CURRENT_USER: self.hkcu,
				winreg.HKEY_LOCAL_MACHINE: self.hklm,
			}

			def read_keys(cls, base, key):
				"""Return list of registry keys."""
				hive = hives.get(base, {})
				return [k.rpartition('\\')[2]
						for k in hive if k.startswith(key.lower())]

			def read_values(cls, base, key):
				"""Return dict of registry keys and values."""
				hive = hives.get(base, {})
				return dict((k.rpartition('\\')[2], hive[k])
							for k in hive if k.startswith(key.lower()))

			distutils.msvc9compiler.Reg.read_keys = classmethod(read_keys)
			distutils.msvc9compiler.Reg.read_values = classmethod(read_values)

			return self

		def __exit__(self, exc_type, exc_value, exc_tb):
			distutils.msvc9compiler.Reg.read_keys = self.original_read_keys
			distutils.msvc9compiler.Reg.read_values = self.original_read_values

	class TestMSVC9Compiler(unittest.TestCase):

		def test_find_vcvarsall_patch(self):
			if not hasattr(distutils, 'msvc9compiler'):
				# skip
				return

			self.assertEqual(
				"setuptools.extension",
				distutils.msvc9compiler.find_vcvarsall.__module__,
				"find_vcvarsall was not patched"
			)

			find_vcvarsall = distutils.msvc9compiler.find_vcvarsall
			query_vcvarsall = distutils.msvc9compiler.query_vcvarsall

			# No registry entries or environment variable means we should
			# not find anything
			old_value = os.environ.pop("VS90COMNTOOLS", None)
			try:
				with MockReg():
					self.assertIsNone(find_vcvarsall(9.0))

					try:
						query_vcvarsall(9.0)
						self.fail('Expected DistutilsPlatformError from query_vcvarsall()')
					except distutils.errors.DistutilsPlatformError:
						exc_message = str(sys.exc_info()[1])
					self.assertIn('aka.ms/vcpython27', exc_message)
			finally:
				if old_value:
					os.environ["VS90COMNTOOLS"] = old_value

			key_32 = r'software\microsoft\devdiv\vcforpython\9.0\installdir'
			key_64 = r'software\wow6432node\microsoft\devdiv\vcforpython\9.0\installdir'

			# Make two mock files so we can tell whether HCKU entries are
			# preferred to HKLM entries.
			mock_installdir_1 = tempfile.mkdtemp()
			mock_vcvarsall_bat_1 = os.path.join(mock_installdir_1, 'vcvarsall.bat')
			open(mock_vcvarsall_bat_1, 'w').close()
			mock_installdir_2 = tempfile.mkdtemp()
			mock_vcvarsall_bat_2 = os.path.join(mock_installdir_2, 'vcvarsall.bat')
			open(mock_vcvarsall_bat_2, 'w').close()
			try:
				# Ensure we get the current user's setting first
				with MockReg(
					hkey_current_user={key_32: mock_installdir_1},
					hkey_local_machine={
						key_32: mock_installdir_2,
						key_64: mock_installdir_2,
					}
				):
					self.assertEqual(mock_vcvarsall_bat_1, find_vcvarsall(9.0))

				# Ensure we get the local machine value if it's there
				with MockReg(hkey_local_machine={key_32: mock_installdir_2}):
					self.assertEqual(mock_vcvarsall_bat_2, find_vcvarsall(9.0))

				# Ensure we prefer the 64-bit local machine key
				# (*not* the Wow6432Node key)
				with MockReg(
					hkey_local_machine={
						# This *should* only exist on 32-bit machines
						key_32: mock_installdir_1,
						# This *should* only exist on 64-bit machines
						key_64: mock_installdir_2,
					}
				):
					self.assertEqual(mock_vcvarsall_bat_1, find_vcvarsall(9.0))
			finally:
				shutil.rmtree(mock_installdir_1)
				shutil.rmtree(mock_installdir_2)
 
 
setuptools / setuptools / msvc9_support.py 
==============================================
 
::

	import sys

	import distutils.msvc9compiler

	def patch_for_specialized_compiler():
		"""
		Patch functions in distutils.msvc9compiler to use the standalone compiler
		build for Python (Windows only). Fall back to original behavior when the
		standalone compiler is not available.
		"""
		VC_BASE = r'Software\%sMicrosoft\DevDiv\VCForPython\%0.1f'
		find_vcvarsall = distutils.msvc9compiler.find_vcvarsall
		query_vcvarsall = distutils.msvc9compiler.query_vcvarsall
		if find_vcvarsall and find_vcvarsall.__module__.startswith('setuptools.'):
			# Already patched
			return

		def _find_vcvarsall(version):
			Reg = distutils.msvc9compiler.Reg
			try:
				# Per-user installs register the compiler path here
				productdir = Reg.get_value(VC_BASE % ('', version), "installdir")
			except KeyError:
				try:
					# All-user installs on a 64-bit system register here
					productdir = Reg.get_value(VC_BASE % ('Wow6432Node\\', version), "installdir")
				except KeyError:
					productdir = None

			if productdir:
				import os
				vcvarsall = os.path.join(productdir, "vcvarsall.bat")
				if os.path.isfile(vcvarsall):
					return vcvarsall

			return find_vcvarsall(version)

		def _query_vcvarsall(version, *args, **kwargs):
			try:
				return query_vcvarsall(version, *args, **kwargs)
			except distutils.errors.DistutilsPlatformError:
				exc = sys.exc_info()[1]
				if exc and "vcvarsall.bat" in exc.args[0]:
					message = 'Microsoft Visual C++ %0.1f is required (%s).' % (version, exc.args[0])
					if int(version) == 9:
						# This redirection link is maintained by Microsoft.
						# Contact vspython@microsoft.com if it needs updating.
						raise distutils.errors.DistutilsPlatformError(
							message + ' Get it from http://aka.ms/vcpython27'
						)
					raise distutils.errors.DistutilsPlatformError(message)
				raise

		distutils.msvc9compiler.find_vcvarsall = _find_vcvarsall
		distutils.msvc9compiler.query_vcvarsall = _query_vcvarsall


