

.. index::
   pair: pip ; Usage


.. _pip_usage:

==========
pip Usage
==========


.. seealso::

   - http://tech.marksblogg.com/better-python-package-management.html

.. contents::
   :depth: 3
   
   

.. _pip install:

pip install
===========


.. _pip_install_examples:

Examples
---------

1) Install `SomePackage` and it's dependencies 

::

  $ pip install SomePackage            # latest version
  $ pip install SomePackage==1.0.4     # specific version
  $ pip install SomePackage>=1.0.4     # minimum version


2) Install a list of requirements specified in a file.  

::

  $ pip install -r requirements.txt


3) Upgrade an already installed `SomePackage` to the latest from PyPI.

::

  $ pip install --upgrade SomePackage


4) Install a local project in "editable" mode. 

::

  $ pip install -e .                     # project in current directory
  $ pip install -e path/to/project       # project in another directory


5) Install a project from VCS in "editable" mode. 

::

  $ pip install -e git+https://git.repo/some_pkg.git#egg=SomePackage          # from git
  $ pip install -e hg+https://hg.repo/some_pkg.git#egg=SomePackage            # from mercurial
  $ pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomePackage         # from svn
  $ pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomePackage  # from 'feature' branch


6) Install a package with `setuptools extras`_.

::

  $ pip install SomePackage[PDF]
  $ pip install SomePackage[PDF]==3.0
  $ pip install -e .[PDF]==3.0  # editable project in current directory


7) Install a particular source archive file.

::

  $ pip install ./downloads/SomePackage-1.0.4.tar.gz
  $ pip install http://my.package.repo/SomePackage-1.0.4.zip


8) Install from alternative package repositories.

Install from a different index, and not `PyPI`_::

  $ pip install --index-url http://my.package.repo/simple/ SomePackage

  Search an additional index during install, in addition to `PyPI`_::

  $ pip install --extra-index-url http://my.package.repo/simple SomePackage

  Install from a local flat directory containing archives (and don't scan indexes)::

  $ pip install --no-index --find-links:file:///local/dir/ SomePackage
  $ pip install --no-index --find-links:/local/dir/ SomePackage
  $ pip install --no-index --find-links:relative/dir/ SomePackage


9) Find pre-release and development versions, in addition to stable versions.  By default, pip only finds stable versions.


::

  $ pip install --pre SomePackage



.. _PyPI: http://pypi.python.org/pypi
.. _setuptools extras: http://packages.python.org/distribute/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies


pip uninstall
=============


Examples
--------

1) Uninstall a package.

::

    $ pip uninstall simplejson
    Uninstalling simplejson:
      /home/me/env/lib/python2.7/site-packages/simplejson
      /home/me/env/lib/python2.7/site-packages/simplejson-2.2.1-py2.7.egg-info
    Proceed (y/n)? y
      Successfully uninstalled simplejson


.. _`pip freeze`:

pip freeze
===========

Examples
--------

1) Generate output suitable for a requirements file.

::

  $ pip freeze
  Jinja2==2.6
  Pygments==1.5
  Sphinx==1.1.3
  docutils==0.9.1


2) Generate a requirements file and then install from it in another environment.

::

  $ env1/bin/pip freeze > requirements.txt
  $ env2/bin/pip install -r requirements.txt



pip list
=========


Examples
---------

1) List installed packages
----------------------------

::

  $ pip list
  Pygments (1.5)
  docutils (0.9.1)
  Sphinx (1.1.2)
  Jinja2 (2.6)

2) List outdated packages (excluding editables), and the latest version available ``pip list --outdated``
-----------------------------------------------------------------------------------------------------------

::

  $ pip list --outdated
  docutils (Current: 0.9.1 Latest: 0.10)
  Sphinx (Current: 1.1.2 Latest: 1.1.3)

pip show
=========


Examples
---------

1. Show information about a package ``pip show sphinx``
-----------------------------------------------------------

::

    $ pip show sphinx
    ---
    Name: Sphinx
    Version: 1.1.3
    Location: /my/env/lib/pythonx.x/site-packages
    Requires: Pygments, Jinja2, docutils

pip search
===========


Examples
---------

1. Search for "peppercorn"

::

  $ pip search peppercorn
  pepperedform    - Helpers for using peppercorn with formprocess.
  peppercorn      - A library for converting a token stream into [...]



.. _pip wheel:

pip wheel
===========


Examples
---------

1. Build wheels for a requirement (and all its dependencies), and then install

::

    $ pip wheel --wheel-dir=/tmp/wheelhouse SomePackage
    $ pip install --use-wheel --no-index --find-links=/tmp/wheelhouse SomePackage



