

.. index::
   pair: Python2; Virtualenv
   pair: mkvirtualenv; Python2


.. _python2_virtualenv:

====================
Python2 virtualenv
====================

.. seealso::

   - https://github.com/pypa/virtualenv
   - http://pypi.python.org/pypi/virtualenv
   - :ref:`pip`
   - :ref:`virtualenv`

.. contents::
   :depth: 5

What It Does
============

``virtualenv`` is a tool to create isolated Python environments.

The basic problem being addressed is one of dependencies and versions, and
indirectly permissions.

**Imagine you have an application that needs version 1 of LibFoo, but another
application requires version 2.
How can you use both these applications?** If you install everything into
/usr/lib/python2.7/site-packages (or whatever your platform's standard location is),
it's easy to end up in a situation where you unintentionally upgrade an
application that shouldn't be upgraded.

Or more generally, what if you want to install an application and leave it be ?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you can't install packages into the global site-packages directory ?
For instance, on a shared host.

In all these cases, virtualenv can help you. It creates an environment that has
its own installation directories, that doesn't share libraries with other
virtualenv environments (and optionally doesn't access the globally installed
libraries either).


Virtualenv source code
=======================

.. seealso::

   - https://github.com/pypa/virtualenv
   - https://github.com/qwcode/virtualenv


Working with virtualenv
=======================

.. seealso:: 

   - http://blog.adamdklein.com/?p=416
   - http://www.michaelpollmeier.com/eclipse-pydev-and-virtualenv/

You should have installed:

- :ref:`virtualenv`
- :ref:`pip <pip>`
- :ref:`virtualenvwrapper <virtualenvwrapper>`

by now.

mkvirtualenv -h
----------------

::

    Usage: mkvirtualenv [-a project_path] [-i package] [-r requirements_file] [virtualenv options] env_name

    -a project_path

    Provide a full path to a project directory to associate with
    the new environment.

    -i package

    Install a package after the environment is created.
    This option may be repeated.

    -r requirements_file

    Provide a pip requirements file to install a base set of packages
    into the new environment.

    virtualenv help:

    Usage: virtualenv [OPTIONS] DEST_DIR

    Options:
    --version             show program's version number and exit
    -h, --help            show this help message and exit
    -v, --verbose         Increase verbosity
    -q, --quiet           Decrease verbosity
    -p PYTHON_EXE, --python=PYTHON_EXE
                        The Python interpreter to use, e.g.,
                        --python=python2.5 will use the python2.5 interpreter
                        to create the new environment.  The default is the
                        interpreter that virtualenv was installed with
                        (/usr/bin/python)
    --clear               Clear out the non-root install and start from scratch
    --no-site-packages    Don't give access to the global site-packages dir to
                        the virtual environment (default)
    --system-site-packages
                        Give access to the global site-packages dir to the
                        virtual environment
    --unzip-setuptools    Unzip Setuptools or Distribute when installing it
    --relocatable         Make an EXISTING virtualenv environment relocatable.
                        This fixes up scripts and makes all .pth files
                        relative
    --distribute, --use-distribute
                        Use Distribute instead of Setuptools. Set environ
                        variable VIRTUALENV_DISTRIBUTE to make it the default
    --no-setuptools       Do not install distribute/setuptools (or pip) in the
                        new virtualenv.
    --no-pip              Do not install pip in the new virtualenv.
    --setuptools          Use Setuptools instead of Distribute.  Set environ
                        variable VIRTUALENV_SETUPTOOLS to make it the default
    --extra-search-dir=SEARCH_DIRS
                        Directory to look for setuptools/distribute/pip
                        distributions in. You can add any number of additional
                        --extra-search-dir paths.
    --never-download      Never download anything from the network.  Instead,
                        virtualenv will fail if local distributions of
                        setuptools/distribute/pip are not present.
    --prompt=PROMPT       Provides an alternative prompt prefix for this
                        environment



.. _mkvirtualenv_python_2:

Creating a virtualenv is easy for python2
=========================================

::

    mkvirtualenv PROJECTNAME

.. note:: this will not create a project directory.
  You need to do this yourself

::

    mkdir -p PROJECTDIR


Very often, you will like to modify PYTHONPATH to include your project
directory in it.

This depends on layout of your project of course. More on this later.

::

    add2virtualenv $(pwd)/PROJECTDIR

Deactivating virtualenv
=======================

To deactivate or log out of a virtualenv, simply type::

    deactivate

Or switch to another project::

    workon ANOTHERPROJECT

Installing dependencies
=======================

Once you have activated your virtualenv by mkvirtualenv
above or manually by::

    workon PROJECT

you can start installing dependencies with pip.
Let's install the Django trunk with the now very popular South::

    pip install -e svn+http://code.djangoproject.com/svn/django/trunk#egg=django
    pip install -e hg+http://bitbucket.org/andrewgodwin/south#egg=south

Make sure you check out the pip documentation for more.
You may still want to and can install packages globally and the virtualenv
will recognize it.




Virtualenvwrapper
=================

.. toctree::
   :maxdepth: 3

   virtualenvwrapper/index










