

.. index::
   pair: Python ; Pss
   pair: Search ; Pss
   ! Pss


.. _pss:

====================
pss
====================


.. seealso::

   - https://github.com/eliben/pss/
   - https://raw.github.com/eliben/pss/master/README.rst
   - https://github.com/eliben/pss/wiki/Usage-samples


.. contents::
   :depth: 3

Introduction: what is pss ?
===========================

**pss** is a power-tool for searching inside source code files. **pss**
searches recursively within a directory tree, knows which extensions and
file names to search and which to ignore, automatically skips directories
you wouldn't want to search in (for example ``.svn`` or ``.git``), colors
its output in a helpful way, and does much more.

If you're familiar with the **ack** tool, then you will find **pss** very
similar (see https://github.com/eliben/pss/wiki/pss-and-ack).

Pre-requisites
===============

**pss** needs only Python to run. 

It works with with Python versions 2.6, 2.7 and 3.2+ on Linux and Windows. 

Some testing was done on Mac OS X and FreeBSD as well.

Installing
==========

**pss** can be installed from PyPi (Python package index)::

    > pip install pss

Alternatively, you can download the source distribution either from PyPi or
go to the *Downloads* tab on the `pss project page <https://github.com/eliben/pss>`_
and pick the version you're interested in from *Tags*. When you unzip the
source distribution, run::

    > python setup.py install

Running without installing
==========================

**pss** supports direct invocation even without installing it. 

This may be useful if you're on a machine without administrator rights, or 
want to experiment with a source distribution of **pss**.

Just unzip the **pss** distribution into some directory. Let's assume its full
path is ``/path/to/pss``. You can now run::

    > /path/to/python /path/to/pss

And this will invoke **pss** as expected. This command can also be tied to an
alias or placed in a shell (or batch) script for convenience.

How to use it?
==============

**pss** is meant to be executed from the command line. Running it with no
arguments or with ``-h`` will print a detailed usage message. 

For some detailed usage examples, check out the 
Usage wiki page - https://github.com/eliben/pss/wiki/Usage-samples

License
=======

**pss** is open-source software. Its code is in the public domain. See the
``LICENSE`` file for more details.


pss and ack
============

pss was inspired by :ref:`ack`, a similar tool written in Perl. 

Prior to writing pss, I've been using and enjoying ack for many years, thanks 
to ack's author Andy Lester for that!

pss clones ack's functionality (implementing most of the features). 

The reason I decided to write and release it is mainly that Python is my language 
of choice, and installing Perl to run ack became a chore (chiefly on Windows 
machines, since on Linux Perl is usually installed by default). 

Really, the only reason I've been installing Perl on Windows boxes I had to work 
on in the past couple of years was to enable them to run ack.

Moreover, pss comes with a terminal-color library built-in, so unlike ack it 
doesn't require to install any additional modules to nicely color its output 
on Windows (ack requires Win32::Console::ANSI).

I have some ideas for extending pss with extra features, and wanted to be able 
to do that in Python, without having to dust off my Perl skills. 

Other Pythonistas may find pss attractive for the same reason. 

pss is implemented in a very modular manner, the main script is just a thin 
wrapper over a library which can be used programmatically for a variety of 
purposes. In other words, pss is quite hackable.

Finally, pss just seemed like a cool project to do. 

Its existence is not meant to detriment ack in any way.



