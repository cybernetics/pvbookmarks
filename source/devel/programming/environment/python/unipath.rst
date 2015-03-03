

.. index::
   pair: Unipath; Path
   pair: Universal; Path
   ! Unipath

.. _unipath:

==========================
Unipath (universal path)
==========================

.. seealso::

   - https://github.com/mikeorr/Unipath


.. contents::
   :depth: 3


Pypi presentation
==================

Object-oriented alternative to os/os.path/shutil

Unipath is an object-oriented front end to the file/directory functions 
scattered throughout several Python library modules. 

It's based on Jason Orendorff's path.py but does not adhere as strictly 
to the underlying functions' syntax, in order to provide more user 
convenience and higher-level functionality. 

Unipath is stable, well-tested, and has been used in production since 2008.

Version 1.0 was released in April 2013 and includes Python 3 support. 
No API changes were made.

Introduction
============

Unipath is an object-oriented front end to the file/directory functions
scattered throughout several Python library modules.  It's based on Jason
Orendorff's *path.py* but does not adhere as strictly to the underlying
functions' syntax, in order to provide more user convenience and higher-level
functionality. 

Unipath is stable, well-tested, and has been used in production since 2008.

Version 1.0 runs on Python 2.6, 2.7, 3.2, and 3.3. Older Python versions should
stick to Unipath 0.2.

Users may also want to consider 'pathlib' (PEP 428), a more recent path library
which is being considered for inclusion in Python 3.4. It has a more modern
API, and I'm evaluating it as a potential successor to Unipath.  However, as of
March 2013 pathlib's API is still in flux, it has not been widely tested yet,
and it has fewer features than Unipath.

The ``Path`` class encapsulates the file/directory operations in Python's
``os``, ``os.path``, and ``shutil`` modules. (Non-filesystem operations are in
the ``AbstractPath`` superclass, but users can ignore this.)

The API has been streamlined to focus on what the application developer wants
to do rather than on the lowest-level operations; e.g., ``.mkdir()`` succeeds
silently if the directory already exists, and ``.rmtree()`` doesn't barf if the
target is a file or doesn't exist.  This allows the developer to write simple
calls that "just work" rather than entire if-stanzas to handle low-level
details s/he doesn't care about.  This makes applications more self-documenting
and less cluttered.

Convenience methods: 

  * ``.read_file`` and ``.write_file`` encapsulate the open/read/close pattern.
  * ``.needs_update(others)`` tells whether the path needs updating; i.e., 
    if it doesn't exist or is older than any of the other paths.
  * ``.ancestor(N)`` returns the Nth parent directory, useful for joining paths.
  * ``.child(\*components)`` is a "safe" version of join.
  * ``.split_root()`` handles slash/drive/UNC absolute paths in a uniform way.

Sample usage for pathname manipulation::

    >>> from unipath import Path
    >>> p = Path("/usr/lib/python2.5/gopherlib.py")
    >>> p.parent
    Path("/usr/lib/python2.5")
    >>> p.name
    Path("gopherlib.py")
    >>> p.ext
    '.py'
    >>> p.stem
    Path('gopherlib')
    >>> q = Path(p.parent, p.stem + p.ext)
    >>> q
    Path('/usr/lib/python2.5/gopherlib.py')
    >>> q == p
    True

Sample usage for filesystem access::

    >>> import tempfile
    >>> from unipath import Path
    >>> d = Path(tempfile.mkdtemp())
    >>> d.isdir()
    True
    >>> p = Path(d, "sample.txt")
    >>> p.exists()
    False
    >>> p.write_file("The king is a fink!")
    >>> p.exists()
    True
    >>> print(p.read_file())
    The king is a fink!
    >>> d.rmtree()
    >>> p.exists()
    False

Path objects subclass ``str`` (Python 2 ``unicode``), so they can be passed
directly to fuctions expecting a string path. They are also immutable and can
be used as dictionary keys.

The name "Unipath" is short for "universal path". It was originally intended to
unify the competing path APIs as of PEP 334. When the PEP was rejected, Unipath
added some convenience APIs.  The code is implemented in layers, with
filesystem-dependent code in the ``Path`` class and filesystem-independent code
in its ``AbstractPath`` superclass.


Example
=======

::

    >>> a=Path(os.environ['APPDATA'], 'Eurocopter')
    
::
    
    >>> a
    Path(u'C:\\Users\\pvergain\\AppData\\Roaming\\Eurocopter')
    
    
::

    >>> db_eurocopter=Path(os.environ['APPDATA'], 'Eurocopter', 'DB_Eurocopter.sqlite')
    
::
    
    >>> db_eurocopter
    Path(u'C:\\Users\\pvergain\\AppData\\Roaming\\Eurocopter\\DB_Eurocopter.sqlite')    



